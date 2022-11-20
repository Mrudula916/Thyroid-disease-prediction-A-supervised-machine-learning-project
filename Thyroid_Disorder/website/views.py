from flask import Flask, render_template, url_for, request, redirect, Response, session, jsonify, Blueprint
from website.feedParser import ParseFeed, dict_parse
from model.model import model, predict
website = Blueprint('website', __name__, static_folder='static',
                    template_folder='templates', static_url_path='/website/static/')


__form_response__ = {
    "onthyroxine": 0,
    "antithyroidmed":0,
    "hypothyroid":0,
    "goitre":0,
    "psych":0,
    "pregnant":0,
    "tsh":0,
    "t3":0, 
    "tt4":0,
    "fti":0,
    }

@website.route("/")
@website.route("/home")
def home():
    return render_template("td.html")

@website.route("/info")
def info():
    return render_template("info.html")

@website.route('/news')
def news(temp="gen"):
    url = 'https://news.google.com/rss/search?q=chronic+thyroid+disease&hl=en-IN&gl=IN&num=10&ceid=US:en'
    
    feed = ParseFeed(url)
    feeds_list = feed.parse()
    return render_template('news.html', results = feeds_list)

@website.route("/test")
def form():
    return render_template("form.html")


@website.route("/predict", methods=["POST"])
def pred():
    dis = ["notthydis","thydis"]
    stage = ["Negative","Positive"]

    global __form_response__
    for key in __form_response__:
        __form_response__[key] = request.form[key]
    __form_response__ = dict_parse(__form_response__)
    result, type = predict(__form_response__)
    return render_template('form.html', prediction = dis[int(result)], result = stage[result], type = type)


