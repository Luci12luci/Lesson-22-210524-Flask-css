from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    year = 0
    return render_template("index.html", year = year)

@app.route("/order-coffee")
def order_coffee():
    return render_template("order_coffee.html")

if __name__ == "__main__":
    app.run()
