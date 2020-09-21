from flask import Flask, render_template
app = Flask(__name__)


# Homepage (Index)
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Verkefni 2.1
@app.route("/verkefni2-1")
def Verkefni21():
    return render_template("Verkefni2-1.html")

@app.route("/KTSum/<int_KT>")
def KT(int_KT):
    kennitala = int_KT
    result = sum(int(digit) for digit in str(int_KT))
    return render_template("KTSum.html", endSum = result, KT = kennitala) 

# Verkefni 2.2

frettir = [
    ["0", "Irma veldur usla á Flórída", "Það er bara helv... vesen á Irmu í Flórída. Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "thha@frettir123.is"],
    ["1", "Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "gsh@frettir123.is"],
    ["2", "Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "ope@frettir123.is"],
    ["3", "Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli. Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "thha@frettir123.is"]
]

@app.route("/verkefni2-2")
def Verkefni22():
    return render_template("frettir.html", frettir=frettir)

@app.route('/frett/<int:id>')
def frett(id):
    return render_template("frett.html", frett=frettir[id])

# Error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error500.html'), 500


if __name__ ==  "__main__":
    app.run(debug=True)
 