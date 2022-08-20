from flask import render_template, request
from keep_alive import app
from flask import Flask

app = Flask("calculator")


@app.route('/')

def title():
    return render_template('calculator.html')

@app.route('/result',methods=["POST","GET"])
def calculate():
    lucrobruto = float(request.form["lucro_bruto"])
    gasto = float(request.form["gastos"])
    saldo = float(lucrobruto-gasto)
    lucrop = float(saldo/lucrobruto*100)
    margemp = float(100-lucrop)
    data = { 'saldo': round(saldo, 2), 'lucrop': round(lucrop, 2), 'margemp': round(margemp, 2) }
    return render_template('calculator.html', data=data)
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
