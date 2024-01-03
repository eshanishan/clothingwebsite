from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    return redirect ('/advanced')
  return render_template("index.html")

@app.route("/advanced", methods=['GET', 'POST'])
def advanced():
  if request.method == 'POST':
    return redirect ('/result')
  return render_template("advanced.html")

@app.route("/result", methods=['GET', 'POST'])
def result():
  return render_template("result.html")

if __name__ == "__main__":
  app.run(debug=True, port=4000)