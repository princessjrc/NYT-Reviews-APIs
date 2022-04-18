from Project2_Flask import app, forms, api_methods
from flask import render_template, request

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/titleWord', methods=["GET","POST"])
def titleWord():
    form = forms.MovieReviewForms(request.form)
    if request.method == "POST":
        selected_word = request.form['word']
        word = api_methods.request_word(selected_word)
        list_reviews = []
        for i in word["results"]:
            movies_and_reviews = (i["display_title"], i["summary_short"], i["link"]["url"])
            list_reviews.append(movies_and_reviews)
        return render_template("title_word_results.html", response=list_reviews)
    return render_template("title_word.html", form=form)

@app.route('/typeReviewer', methods=["GET","POST"])
def typeReviewer():
    form = forms.MovieReviewForms(request.form)
    if request.method == "POST":
        selected_reviewer = request.form["reviewer"]
        type_reviews = api_methods.request_reviewers(selected_reviewer)
        list_reviewers = []
        for i in type_reviews["results"]:
            reviewer_names = i["display_name"]
            list_reviewers.append(reviewer_names)
        return render_template("typeReviewer_results.html", response=list_reviewers)
    return render_template("typeReviewer.html", form=form)

@app.route('/criticsPicks', methods=["GET","POST"])
def criticsPicks():
    form = forms.MovieReviewForms(request.form)
    if request.method == "POST":
        selected_picks = request.form["picks"]
        if_picks = api_methods.request_picks(selected_picks)
        list_movies = []
        for i in if_picks["results"]:
            movies = (i["display_title"], i["summary_short"], i["link"]["url"])
            list_movies.append(movies)
        return render_template("critics_picks_results.html", response=list_movies)
    return render_template("critics_picks.html",form=form)