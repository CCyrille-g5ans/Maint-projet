from flask import Flask

app = Flask(__name__)

# Mon premier programme Flask
@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/test/')
def test():
    return home() + " vous êtes sur "


if __name__ == '__main__':
    app.run(debug=True)
