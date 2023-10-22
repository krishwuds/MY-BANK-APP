# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

accounts = {
    "user1": {"balance": 1000},
    "user2": {"balance": 2000},
}

@app.route("/")
def home():
    return render_template("index.html", accounts=accounts)

@app.route("/transfer", methods=["POST"])
def transfer():
    from_account = request.form.get("from_account")
    to_account = request.form.get("to_account")
    amount = float(request.form.get("amount"))

    if from_account in accounts and to_account in accounts and accounts[from_account]["balance"] >= amount:
        accounts[from_account]["balance"] -= amount
        accounts[to_account]["balance"] += amount
    else:
        return "Transfer failed. Please check the accounts and balance."

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
