import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('default.html')

@app.route('/kt-sida/<kt>')
def ktsida(kt):
    summa=0
    for item in kt:
        summa=summa+int(item)
    return render_template('kt-sum.html',kt=kt, summa=summa)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

if __name__ == '__main__':
    app.run(debug=True)