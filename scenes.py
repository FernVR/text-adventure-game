scenes = {
    "start": {
        "text": "You find yourself at the entrance to a dark cave. Do you ENTER or RUN?",
        "next": {
            "enter": "cave",
            "run": "escape"
        }
    },
    "cave": {
        "text": "You are inside the cave. It's damp and eerie. You hear a noise. Do you HIDE or INVESTIGATE?",
        "next": {
            "hide": "hidden_chamber",
            "investigate": "monster"
        }
    },
    "escape": {
        "text": "You run away safely, but miss out on the adventure. The end.",
        "next": {}
    },
    "hidden_chamber": {
        "text": "You find a hidden chamber filled with gold! Do you TAKE it or LEAVE it?",
        "next": {
            "take": "trap",
            "leave": "safe_exit"
        }
    },
    "monster": {
        "text": "A monster jumps out and eats you. The end.",
        "next": {}
    },
    "trap": {
    "text": "It was a trap! You're trapped forever.",
    "next": {}
    },
    "safe_exit": {
    "text": "You leave the gold and escape safely. You live to tell the tale!",
    "next": {}
    }
}
