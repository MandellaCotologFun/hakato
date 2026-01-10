from flask import Flask, render_template
import random

app = Flask(__name__)

facts_list = [
    "Белые медведи теряют лёд.",
    "Глобальное потепление разрушает их среду обитания.",
    "Медведям приходится далеко плыть."
]

memes_list = [
    "memes/medved.png",
    "memes/meme2.png",
    "memes/meme3.png"
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        fact=random.choice(facts_list),
        meme=random.choice(memes_list)
    )

app.run(debug=True)
