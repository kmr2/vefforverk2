import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#verkhluti A

@app.route('/a-hluti')
def ahlut():
    return render_template('kennitala.html')

@app.route('/kt-sida/<kt>')
def ktsida(kt):
    summa=0
    for item in kt:
        summa=summa+int(item)
    return render_template('kt-sum.html',kt=kt, summa=summa)

#verkhluti B
#id, yfirsögn, fréttir, email
frettir=[
    ['0','Karl vignir sigurðsson er labbandi',
    'stór hommi lítil homo, eða kanski geimvera er hannhver veit spyrjum hann sigmund davíð til að fata það',
    'donathantrumb@gmail.com '],
    ['1', 'Veiðin er dræm þetta haustið', 
    'Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið... ', 
    'donathantrumb@gmail.com'],
    ['2', 'Hákar talar um sína tök á ugg veiðingu', 
    'ugga veiðing í kína er ógeðslegt eina sem þeir gera er að veiða hákarali og skera uggina af svo henda aftur hákarlinum út í vatnið til að deyja hægt svo er okkar uggi notað í einvherja helvítis súpu', 
    'donathantrumb@gmail.com'],
    ['3', 'Lorem Ipsum ', 
    'Hann lorem ipsum stefán karlsson hefur sagt að hann hefur verið ástæðan erfiða leikan í Hong Kong', 
    'donathantrumb@gmail.com']
]   

@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html', frettir=frettir)

@app.route('/frett/<int:id>')
def frett(id):
    return render_template('frett.html', frett=frettir[id], nr=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

if __name__ == '__main__':
    app.run(debug=False)