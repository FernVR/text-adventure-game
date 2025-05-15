from flask import Flask, render_template, request, redirect, session, url_for
from scenes import scenes

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

    current_scene = session.get('progress', 'start')
    scene = scenes.get(current_scene, {"text": "Scene not found.", "next": {}})
    message = scene["text"]

    if request.method == "POST":
        choice = request.form.get("choice", "").lower()

        next_scene = scene["next"].get(choice)
        if next_scene:
            session['progress'] = next_scene
            return redirect(url_for("game"))
        elif choice == "quit":
            return redirect(url_for("quit"))
        else:
            message = "Invalid choice. Try again."
    
    return render_template("index.html", message=message)


@app.route("/quit")
def quit():
    session.clear()
    return redirect(url_for('menu'))


if __name__ == "__main__":
    app.run(debug=True)
