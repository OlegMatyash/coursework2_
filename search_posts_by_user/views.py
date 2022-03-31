from flask import Blueprint, render_template, request
import utils


# Затем создаем новый блюпринт, выбираем для него имя
posts_by_user_blueprint = Blueprint('posts_by_user_blueprint', __name__, template_folder='templates')

# возвращает посты определенного пользователя
@posts_by_user_blueprint.route('/user-feed/<poster_name>')
def search_post_user(poster_name):
    poster_name = poster_name
    all_posts_user_name = utils.get_posts_by_user(poster_name)
    return render_template('user-feed.html', all_posts_user_name=all_posts_user_name, poster_name=poster_name)
