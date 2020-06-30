from flask import Flask,jsonify
from ebay import ebay_scrap

app = Flask(__name__)


@app.route('/')
def hello():
    return "Witaj. Aby skorzystać z api scrapera serwisu Ebay, dodaj do paska adresu ciąg znaków   /api/element    zastępując słowo element modelem telefonu np /api/samsung+galaxy"


@app.route('/api/<item>')
def page(item):
    return jsonify(ebay_scrap(item))


if __name__ == "__main__":
    app.run(  )

