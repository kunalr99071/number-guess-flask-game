from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

MAX_ATTEMPTS = 5


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/start")
def start():
    session["number"] = random.randint(1,100)
    session["attempts"] = 0
    return redirect(url_for("game"))


@app.route("/game", methods=["GET","POST"])
def game():

    if "number" not in session:
        return redirect(url_for("home"))

    message = ""

    if request.method == "POST":

        guess = int(request.form["guess"])
        session["attempts"] += 1

        number = session["number"]
        attempts = session["attempts"]
        difference = abs(number - guess)

        if guess == number:
            return redirect(url_for("result", status="win"))

        elif guess < number:
            if difference <= 10:
                message = "Too Small 🔥 Very Close!"
            elif difference <= 30:
                message = "Small"
            else:
                message = "Too Small ❄️ Far Away"

        elif guess > number:
            if difference <= 10:
                message = "Too Large 🔥 Very Close!"
            elif difference <= 30:
                message = "Large"
            else:
                message = "Too Large ❄️ Far Away"

        if attempts >= MAX_ATTEMPTS and guess != number:
            return redirect(url_for("result", status="lose"))

    return render_template(
        "game.html",
        message=message,
        attempts=session["attempts"],
        max_attempts=MAX_ATTEMPTS
    )


@app.route("/result")
def result():

    status = request.args.get("status")
    number = session.get("number")

    if status == "win":
        message = "🎉 You Won!"
    else:
        message = f"Better Luck Next Time! The number was {number}"

    return render_template("result.html", message=message)


@app.route("/quit")
def quit():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)