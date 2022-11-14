from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, get_posts_by_pk, search_for_posts
import logging

app = Flask(__name__)


@app.route('/')
def page_index():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:uid>')
def page_posts(uid):
    posts = get_posts_by_pk(uid)
    comments = get_comments_by_post_id(uid)
    return render_template('post.html', posts=posts, comments=comments, len=len(comments))


@app.route('/search/')
def search_page():
    query = request.args.get('s', '')
    posts = search_for_posts(query)

    return render_template("search.html", posts=posts, count=len(posts))


@app.route('/user/<username>')
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html')


@app.route('/api/posts', methods=['GET'])
def get_all_posts():
    all = get_posts_all()
    return jsonify(all)

@app.route('/api/posts/<uid>') ### Не пойму почему не работает, хотя эта же функция корректно выдает посты выше(
def post_by_id(uid):
    post = get_posts_by_pk(uid)
    return jsonify(post)

logging.basicConfig(
    level=logging.DEBUG,
    filename='api.log',
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt='%H:%M:%S',
    ) ## С этим тоже не уверен, что именно это требовалось(


app.run()
