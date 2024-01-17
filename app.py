from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/products')
def about():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def products():
    return render_template("about.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    address = request.args.get('address')
    phone = request.args.get('phone')
    email = request.args.get('email')
    props = {
        "name": name,
        "email": email,
        "address": address,
        "phone": phone

    }
    return render_template("confirmation.html",data=props)


if __name__ == '__main__':
    app.run(debug=True,port=3000)