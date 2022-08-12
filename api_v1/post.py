from flask import jsonify, request
from models import Post, Comment, db
from datetime import datetime

from . import api


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
            return jsonify({'error': 'No arguments!'}), 400

        post = Post()
        post.id = id
        post.username = username
        post.title = title
        post.content = content
        post.password = password
        db.session.add(post)
        db.session.commit()

        return jsonify(data), 201

    posts = Post.query.all()
    return jsonify([post.serialize for post in posts])


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
            return "게시글의 비밀번호가 틀렸습니다.", 400

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
        return '게시글의 비밀번호가 틀렸습니다.', 400


@api.route("/posts/<pid>/comments", methods=["GET", "POST"])
def create_comment(pid):
    if request.method == 'POST':
        post = Post.query.get_or_404(pid)
        data = request.get_json()
        username = data.get('username')
        content = data.get('content')
        parent_id = data.get('parent_id')
        comment = Comment(username=username, content=content, parent_id=parent_id, created_at=datetime.now())
        post.comment_set.append(comment)
        db.session.commit()
        return jsonify(comment.serialize), 201

    comments = Comment.query.filter(Comment.postid == pid)
    return jsonify([cmt.serialize for cmt in comments])