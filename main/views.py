from flask import Blueprint, render_template, request
import utils


# представление для всех постов - это главная страница.
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def page_index():
    posts = utils.get_posts_all_from_json()
    comments = utils.get_comment_all_from_json()
    return render_template('index.html', posts=posts, comments=comments)