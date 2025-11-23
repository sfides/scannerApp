from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/classify", methods=["POST"])
def classify():
    item_type = request.form.get("item_type")
    return f"You selected: {item_type}"

if __name__ == "__main__":
    app.run(debug=True)

