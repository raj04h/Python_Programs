from flask import Flask

app=Flask(__name__)
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Hello, welcome to My Journey</h1>"

@app.route("/Start", methods=["GET"])
def Start():
    return "Let's begins the Vehicle"

@app.route("/Pass/<int:Score>")
def Pass(Score):
    return "Score Card: "+ str(Score)

@app.route("/Fail/<int:Score>")
def Fail(Score):
    return "Score Card: "+ str(Score)


if __name__=="__main__":
    app.run(debug=True)
