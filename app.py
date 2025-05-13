from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    message = "You are standing at the entrance of a dark cave. What do you do?"

    if request.method == "POST":
        choice = request.form.get("choice").lower()
        if "enter" in choice:
            message = "You step into the cave and hear eerie sounds..."
        elif "run" in choice:
            message = "You run away safely. The adventure ends here!"
        else:
            message = "I don't understand that choice. Try something else."
    
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
