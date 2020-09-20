import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html", language='Python', lang=False, framework='Flask')

# Error handler fyrir 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/verkefni2-1")
def Verkefni21():
    return render_template("Verkefni2-1.html", language='Python', lang=False, framework='Flask')

@app.route("/KTSum/<int_KT>")
def KT(int_KT):
    kennitala = int_KT
    result = sum(int(digit) for digit in str(int_KT))
    return render_template("KTSum.html", language='Python', lang=False, framework='Flask', endSum = result, KT = kennitala)

@app.route("/verkefni2-2")
def Verkefni22():
    return render_template("Verkefni2-2.html", language='Python', lang=False, framework='Flask')

if __name__ ==  "__main__":
    app.run(debug=True)
 