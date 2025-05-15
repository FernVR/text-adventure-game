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
    session['inventory'] = []
    session['decisions'] = []
    session['score'] = 0
    session['player_name'] = request.form.get("player_name", "Player")

    return redirect(url_for('game'))


@app.route("/game", methods=["GET", "POST"])
def game():

    player_name = session.get('player_name', 'Player')
    current_scene = session.get('progress', 'start')
    scene = scenes.get(current_scene, {"text": "Scene not found.", "next": {}})
    message = scene["text"].replace("{player}", player_name)

    inventory = session.get('inventory', [])
    score = session.get('score', 0)

    if request.method == "POST":
        choice = request.form.get("choice", "").lower()
        next_scene = scene["next"].get(choice)

        if next_scene:
            # Track Decision
            decisions = session.get('decisions', [])
            decisions.append({"scene": current_scene, "choice": choice})
            session['decisions'] = decisions
            
            # EXAMPLE add custom logic for scene + choice
            if current_scene == "cave" and choice == "investigate":
                inventory.append("torch")
                session['score'] = session.get('score', 0) + 10

            # Update session
            session['inventory'] = inventory
            session['score'] = score

            # Progress to next scene
            session['progress'] = next_scene
            return redirect(url_for("game"))

        elif choice == "quit":
            return redirect(url_for("quit"))
        else:
            message = "Invalid choice. Try again."
    
    return render_template("index.html", message=message, inventory=inventory, score=score)


@app.route("/quit")
def quit():
    session.clear()
    return redirect(url_for('menu'))


if __name__ == "__main__":
    app.run(debug=True)
