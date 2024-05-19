from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data to store products
products = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        itemName = request.form['itemName']
        amount = request.form['amount']
        itemID = len(products) + 1
        products.append({'itemID': itemID, 'itemName': itemName, 'amount': amount})
        return render_template('index.html', products=products)
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)