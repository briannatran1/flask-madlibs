from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, STORIES_DICT

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_homepage():
    """shows homepage with story selection dropdown"""

    return render_template("index.html", stories_dict=STORIES_DICT)


@app.get("/questions")
def show_form():
    """Shows form based story instance"""
    selected_story = STORIES_DICT[request.args["story_name"]]

    return render_template("questions.html", prompts=selected_story.prompts)


@app.get("<story_code>/results")
def show_story():
    """Generates story based on form input values"""

    story_text = selected_story.get_result_text(request.args)

    return render_template("results.html", story=story_text)
