from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple dictionary for user accounts (for demonstration purposes).
# In a real-world application, you'd use a secure database.
user_accounts = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"},
}

# Sample offers data
offers = [
    {
        "title": "Special Savings Account",
        "description": "Open a savings account with us and enjoy a high interest rate."
    },
    {
        "title": "Credit Card Promotion",
        "description": "Apply for our credit card and get a cashback on your first purchase."
    },
    {
        "title": "Mortgage Offer",
        "description": "Low-interest rates on mortgages for a limited time."
    }
]

@app.route("/")
def home():
    return render_template("index.html", offers=offers)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in user_accounts and user_accounts[username]["password"] == password:
        return "Login successful. Welcome, " + username + "!"
    else:
        return "Login failed. Please check your credentials."

if __name__ == "__main__":
    app.run(debug=True)
