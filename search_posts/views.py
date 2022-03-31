from flask import Blueprint, render_template, request
import utils


# Затем создаем новый блюпринт, выбираем для него имя
search_posts_blueprint = Blueprint('search_posts_blueprint_blueprint', __name__, template_folder='templates')

# выбор постов по ключевому полю
# Создаем вьюшку, используя в декораторе блюпринт вместо app
@search_posts_blueprint.route('/search')
def search_posts():
    s = request.args.get('s', '')
    posts = utils.search_for_posts(s)
    return render_template('search.html', posts=posts, s=s)