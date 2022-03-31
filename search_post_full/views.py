from flask import Blueprint, render_template, request
import utils


# Затем создаем новый блюпринт, выбираем для него имя
post_full_blueprint = Blueprint('post_full_blueprint', __name__, template_folder='templates')

# выбор поста по идентификатору
# Создаем вьюшку, используя в декораторе блюпринт вместо app
@post_full_blueprint.route('/posts/<int:pk>')
def get_post(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)