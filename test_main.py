import pytest
import json
import utils
from flask import Flask

from app import app


def test_get_posts():
    response = app.test_client().get('/api/posts')
    post_keys = ['short', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk', 'content']
    assert response.status_code == 200
    assert isinstance(response.json, list)

    for element in response.json:
        if set(element.keys()) != set(post_keys):
            assert False


def test_get_posts_user():
    response = app.test_client().get('/api/posts/1')
    post_keys = ['short', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk', 'content']
    assert response.status_code == 200

    if set(response.json.keys()) != set(post_keys):
        assert False