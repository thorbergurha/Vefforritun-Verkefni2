import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html", language='Python', lang=False, framework='Flask')

# Loadar 404 template þegar síða finnst ekki, þ.e. þegar serverinn skilar 404.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/verkefni2-1", methods=["GET"])
def Verkefni21():
    return render_template("Verkefni2-1.html", language='Python', lang=False, framework='Flask')

@app.route("/KT/<int_KT>")
def KT(int_KT):
    kennitala = int_KT
    result = sum(int(digit) for digit in str(int_KT))
    #return "{0}".format(result)
    return render_template("KT.html", language='Python', lang=False, framework='Flask', endSum = result, KT = kennitala)

@app.route("/verkefni2-2", methods=["GET"])
def Verkefni22():
    return render_template("Verkefni2-2.html", language='Python', lang=False, framework='Flask')

if __name__ ==  "__main__":
    app.run(debug=True)
