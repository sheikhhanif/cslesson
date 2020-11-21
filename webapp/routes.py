from webapp import app
import os
from flask import render_template, url_for, flash, redirect, request, abort
from webapp.models import Video
from os import path
from sqlalchemy.sql import text

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    videos = Video.query.order_by(Video.channel.desc())
    return render_template('home.html', videos=videos)


@app.route("/video/<title>/", methods=['GET', 'POST'])
def video_post(title):
    videos = Video.query.filter_by(title=title).all()
    all_videos = Video.query.order_by(Video.channel.desc())

    for v in videos[:1]:
        title_name = v.title
    return render_template("video.html", videos=videos, title_name=title_name, all_videos=all_videos)

@app.route("/video-post/<fil>", methods=['GET', 'POST'])
def filter(fil):
    if fil == 'all':
        page = request.args.get('page', 1, type=int)
        videos = Video.query.order_by(Video.channel.desc()).paginate(page=page, per_page=20)        
        return render_template("category.html", videos=videos, fil=fil, title_name='All Courses')

    elif fil == 'Geeks Lesson':
        videos = Video.query.filter_by(channel="Geek's Lesson").all()
        return render_template("category.html", videos=videos, title_name=fil+' Courses')

    elif fil == 'My CS':
        videos = Video.query.filter_by(channel=fil).all()
        return render_template("category.html", videos=videos, title_name=fil+' Courses')

    elif fil == 'Academic Lesson':
        videos = Video.query.filter_by(channel=fil).all()
        return render_template("category.html", videos=videos, title_name=fil+' Courses')

    else:
        videos = Video.query.filter_by(category=fil).all()
        return render_template("category.html", videos=videos, title_name=fil+' Courses')

@app.route("/partners")
def partners():
    videos = Video.query.order_by(Video.channel.desc())
    return render_template('partners.html', videos=videos, title_name = 'Our Partners')


@app.route("/contact")
def contact():
    videos = Video.query.order_by(Video.channel.desc())
    return render_template('contact.html', videos=videos, title_name = 'Contact Us')

