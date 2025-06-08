from flask import Flask, url_for, send_file
from flask import render_template, request

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='$$',
        block_end_string='$$',
        variable_start_string='$=',
        variable_end_string='=$',
        comment_start_string='$#',
        comment_end_string='#$',
    ))


app = CustomFlask(__name__, static_url_path='/static')
ndic = {}

@app.route('/')
def index():
    return render_template('index.html')

# todo: handle this by eme-flask / nginx
@app.route('/get_wasm')
def wasm():
    return send_file('static/aes/wasm/aes.wasm',  mimetype='application/wasm')


app.run(host="0.0.0.0", port=80, threaded=True)
