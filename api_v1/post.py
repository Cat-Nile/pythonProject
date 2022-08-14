from flask import jsonify, request
from models import Post, Comment, Word, db
from datetime import datetime
import re
from . import api
from . import notify


@api.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        data = request.get_json()
        id = data.get('id')
        username = data.get('username')
        title = data.get('title')
        content = data.get('content')
        password = data.get('password')
        created_at = data.get('created_at')
        updated_at = data.get('updated_at')

        if not (username and title and content and password):
            return jsonify({'error': 'Missing arguments!'}), 400

        post = Post()
        post.id = id
        post.username = username
        post.title = title
        post.content = content
        post.password = password
        db.session.add(post)
        db.session.commit()

        words = Word.query.all()

        for word in words:
            alarm_list = []
            word_lists = word.word.split(',')
            for word_list in word_lists:
                word_list = word_list.strip()
                if word_list in post.title or word_list in post.content:
                    message = {word.username: post.id}
                    alarm_list.append(message)
                    break

            if alarm_list:
                notify.send_nofi(alarm_list)
        return jsonify(data), 201

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per-page", 5, type=int)

    # query
    posts = Post.query.paginate(page, per_page)

    # combine results with pagination
    results = {
        "results": [{"id": post.id, "username": post.username, "title": post.title, "content": post.content,
                     "created_at": post.created_at, "updated_at": post.updated_at} for post in posts.items],
        "pagination": {
            "page": page,
            "per_page": per_page
        },
    }
    return jsonify(results)

    # posts = Post.query.all()
    # return jsonify([post.serialize for post in posts])


@api.route('/posts/<pid>', methods=['GET', 'PUT', 'DELETE'])
def post_detail(pid):
    if request.method == 'GET':
        post = Post.query.filter(Post.id == pid).first()
        return jsonify(post.serialize)
    elif request.method == 'DELETE':
        post = Post.query.filter(Post.id == pid).first()
        data = request.get_json()
        password = data.get('password')
        if password == post.password:
            Post.query.filter(Post.id == pid).delete()
            return jsonify(), 204
        else:
            return jsonify({'error': 'Did not match with password!'})

    post = Post.query.filter(Post.id == pid).first()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    title = data.get('title')
    content = data.get('content')
    updated_at = datetime.now()

    if password == post.password:
        updated_data = {}
        if username:
            updated_data['username'] = username
        if title:
            updated_data['title'] = title
        if content:
            updated_data['content'] = content
        updated_data['updated_at'] = updated_at
        Post.query.filter(Post.id == pid).update(updated_data)
        return jsonify(updated_data)
    else:
        return jsonify({'error': 'Did not match with password!'})


@api.route("/posts/<pid>/comments", methods=["GET", "POST"])
def create_comment(pid):
    if request.method == 'POST':
        post = Post.query.get_or_404(pid)
        data = request.get_json()
        id = data.get('id')
        username = data.get('username')
        content = data.get('content')
        parent_id = data.get('parent_id')
        comment = Comment(id=id, username=username, content=content, parent_id=parent_id, created_at=datetime.now())
        post.comment_set.append(comment)
        db.session.commit()

        words = Word.query.all()

        for word in words:
            alarm_list = []
            word_lists = word.word.split(',')
            for word_list in word_lists:
                word_list = word_list.strip()
                if word_list in content:
                    message = {word.username: comment.id}
                    alarm_list.append(message)
                    break

            if alarm_list:
                notify.send_nofi(alarm_list)

        return jsonify(comment.serialize), 201

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per-page", 5, type=int)

    # query
    comments = Comment.query.paginate(page, per_page)

    # combine results with pagination
    results = {
        "results": [
            {"id": comment.id, "postid": comment.postid, "username": comment.username, "content": comment.content,
             "parent_id": comment.parent_id, "created_at": comment.created_at} for comment in comments.items],
        "pagination": {
            "page": page,
            "per_page": per_page
        },
    }
    return jsonify(results)


@api.route('/keywords', methods=['GET', 'POST'])
def keywords():
    if request.method == 'POST':
        data = request.get_json()
        id = data.get('id')
        username = data.get('username')
        keyword = data.get('word')

        word = Word()
        word.id = id
        word.username = username
        word.word = keyword
        db.session.add(word)
        db.session.commit()

        return jsonify(data), 201

    words = Word.query.all()
    return jsonify([word.serialize for word in words])
