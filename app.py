from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_form():
    """Shows form based story instance"""

    return render_template("questions.html", prompts=silly_story.prompts)


@app.get("/results")
def show_story():
    """Generates story based on form input values"""

    story_text = silly_story.get_result_text(request.args)

    return render_template("results.html", story=story_text)
