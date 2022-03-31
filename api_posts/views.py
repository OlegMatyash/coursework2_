from flask import Flask, Blueprint, render_template, request
import utils
from flask import jsonify


# Затем создаем новый блюпринт, выбираем для него имя
api_posts_blueprint = Blueprint('api_posts_blueprint', __name__)


# возвращает полный список постов в виде JSON-списка.
@api_posts_blueprint.route('/api/posts')
def get_posts():
    posts = utils.get_posts_all_from_json()
    return jsonify(posts)

# возвращает один пост в виде JSON-словаря
@api_posts_blueprint.route('/api/posts/<int:pk>')
def get_posts_by_pk(pk):
    post = utils.get_post_by_pk(pk)
    return jsonify(post)