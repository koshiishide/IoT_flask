from flask import Flask,request,render_template,url_for
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('index.html')

#「/templates」へアクセスがあった場合に、index.htmlを返す
@app.route("/templates", methods=["GET"])
def index():
    return render_template("index.html")

#「/nextpage」へアクセスがあった場合に、next_index.htmlを返す
@app.route("/nextpage", methods=["GET"])
def nextpage():
    return render_template("next_index.html")

@app.route("/temp", methods=["GET"])
def temp():
    return render_template("temp.html")

@app.route("/nextpage2", methods=["GET"])
def nextpage2():
    return render_template("next_index2.html")

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)