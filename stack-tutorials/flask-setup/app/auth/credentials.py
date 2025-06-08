import bcrypt

from dal import UserRepository, User

user_repo = UserRepository()

def validate_user(username: str, password: str) -> User | None:

    user = user_repo.find_by(username)

    if bcrypt.checkpw(password.encode('utf-8'), user.password):
        return user

    return None
