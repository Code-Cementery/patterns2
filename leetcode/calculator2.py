import re

TOKEN_SPEC = [
    ('NUMBER', r'\d+(\.\d*)?'),  # Integer or decimal number
    ('PLUS', r'\+'),             # Addition operator
    ('MINUS', r'-'),             # Subtraction operator
    ('TIMES', r'\*'),            # Multiplication operator
    ('DIVIDE', r'/'),            # Division operator
    ('LPAREN', r'\('),           # Left parenthesis
    ('RPAREN', r'\)'),           # Right parenthesis
    ('SKIP', r'[ \t]+'),         # Skip over spaces and tabs
    ('MISMATCH', r'.'),          # Any other character
]
token_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC))


def tokenize(code):
    tokens = []
    for match in token_regex.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Unexpected character: {value}")
        else:
            tokens.append((kind, value))
    return tokens


class NumberNode:
    def __init__(self, value):
        self.value = int(value)

    def evaluate(self):
        return self.value


class BinaryOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        if self.operator == 'PLUS':
            return left_val + right_val
        elif self.operator == 'MINUS':
            return left_val - right_val
        elif self.operator == 'TIMES':
            return left_val * right_val
        elif self.operator == 'DIVIDE':
            return left_val // right_val

        raise NotImplementedError(self.operator)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self, expected_type):
        token = self._peek()
        if token and token[0] == expected_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {expected_type} but got {token}")

    def _parse_factor(self):
        token = self._peek()
        if token[0] == 'NUMBER':
            self._consume('NUMBER')
            return NumberNode(token[1])
        elif token[0] == 'LPAREN':
            self._consume('LPAREN')
            expr = self.parse_expr()
            self._consume('RPAREN')
            return expr
        else:
            raise SyntaxError("Invalid factor")

    def _parse_term(self):
        node = self._parse_factor()
        while self._peek() and self._peek()[0] in ('TIMES', 'DIVIDE'):
            op = self._consume(self._peek()[0])
            right = self._parse_factor()
            node = BinaryOpNode(node, op[0], right)
        return node

    def parse_expr(self):
        node = self._parse_term()
        while self._peek() and self._peek()[0] in ('PLUS', 'MINUS'):
            op = self._consume(self._peek()[0])
            right = self._parse_term()
            node = BinaryOpNode(node, op[0], right)
        return node


code = "14/3*2"
parser = Parser(tokenize(code))
ast = parser.parse_expr()

print(ast.evaluate())
