from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


from stories import STORIES_DICT
# import stories

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
    story_title = request.args["story_name"]

    return render_template("questions.html",
                           prompts=selected_story.prompts,
                           story_name=story_title)


@app.get("/<story_name>/results")
def show_story(story_name):
    """Generates story based on form input values"""

    story_text = STORIES_DICT[story_name].get_result_text(request.args)

    return render_template("results.html",
                           story=story_text)
