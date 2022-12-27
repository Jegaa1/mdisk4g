from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'JAsuran'


if __name__ == "__master__":
    app.run()
