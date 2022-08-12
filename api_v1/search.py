from flask import jsonify, request
from models import Post

from . import api


@api.route('/search', methods=['GET'])
def do_search():
    q = request.args.get('q')
    if q:
        search = '%%{}%%'.format(q)
        posts = Post.query.filter(Post.username.ilike(search)|Post.title.ilike(search)).distinct().all()
        return jsonify([post.serialize for post in posts])