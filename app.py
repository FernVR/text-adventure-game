from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route("/")
def menu():
    return render_template("menu.html")


@app.route("/start", methods=["POST"])
def start():
    session['progress'] = 'start'
    return redirect(url_for('game'))


@app.route("/game", methods=["GET", "POST"])
def game():
    message = ""

    if session.get('progress') == 'start':
        message = "You are at the cave entrance. What do you do?"


    if request.method == "POST":
        choice = request.form.get("choice").lower()

        if "enter" in choice:
            message = "You step into the cave and hear eerie sounds..."
            session['progress'] = 'cave'
        elif "run" in choice:
            message = "You run away safely. The adventure ends here!"
            session['progress'] = 'ran'
        elif "quit" in choice:
            return redirect(url_for('quit'))
        else:
            message = "I don't understand that choice. Try something else."
    
    return render_template("index.html", message=message)


@app.route("/quit")
def quit():
    session.clear()
    return redirect(url_for('menu'))


if __name__ == "__main__":
    app.run(debug=True)
