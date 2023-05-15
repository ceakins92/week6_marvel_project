from flask import request, jsonify

from . import bp
from app.models import Post, User
from app.blueprints.api.helpers import token_required

@bp.get('/posts')
@token_required
def api_posts(user):
    result = []
    posts = Post.query.all()
    for post in posts:
        result.append({
            'id':post.id,
            'char_name':post.char_name,
            'char_description':post.char_description,
            'char_super_powers':post.char_super_powers,
            'comics_app_in':post.comics_app_in,
            'movies_app_in':post.movies_app_in,
            'timestamp':post.date_created, 
            'author':post.user_id
            })
    return jsonify(result), 200

@bp.get('/posts/<username>')
@token_required
def user_posts(user,username):
    user = User.query.filter_by(username=username).first()
    if user:
      return jsonify([{
            'id':post.id,
            'char_name':post.char_name,
            'char_description':post.char_description,
            'char_super_powers':post.char_super_powers,
            'comics_app_in':post.comics_app_in,
            'movies_app_in':post.movies_app_in,
            'timestamp':post.date_created, 
            'author':post.user_id
              } for post in user.posts]), 200
    return jsonify([{'message':'Invalid Username'}]), 404 

@bp.get('/post/<id>')
@token_required
def get_post(user,post_id):
    try:
      post = Post.query.get(post_id)
      return jsonify([{
              'id':post.id,
            'char_name':post.char_name,
            'char_description':post.char_description,
            'char_super_powers':post.char_super_powers,
            'comics_app_in':post.comics_app_in,
            'movies_app_in':post.movies_app_in,
            'timestamp':post.date_created, 
            'author':post.user_id
                }])
    except: 
      return jsonify([{'message':'Invalid Post Id'}]), 404
    
@bp.post('/post')
@token_required
def make_post(user):
    try:
        content = request.json
        post = Post(char_name=content.get('char_name'),user_id=user.user_id)
        post.commit()
        return jsonify([{'message':'Post Created','body':post.body}])
    except:
       jsonify([{'message':'invalid form data'}]), 401

