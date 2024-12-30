from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask framework"


@app.route("/success/<score>")
def success(score):
    return "The marks you got is "+score


if __name__=="__main__":
    app.run()


