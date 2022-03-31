from flask import Flask, request, render_template, send_from_directory

from main.views import main_blueprint
from search_post_full.views import post_full_blueprint
from search_posts.views import search_posts_blueprint
from search_posts_by_user.views import posts_by_user_blueprint
from api_posts.views import api_posts_blueprint



app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(post_full_blueprint)
app.register_blueprint(search_posts_blueprint)
app.register_blueprint(posts_by_user_blueprint)
app.register_blueprint(api_posts_blueprint)


if __name__ == "__main__":
    app.run()