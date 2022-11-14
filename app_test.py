import pytest
from app import app

### Почему-то не работает с debug=True(

def test_all_posts():
    response = app.test_client().get("/api/posts")
    return response.json

def test_one_post():
    response = app.test_client().get("/api/posts/<uid>")
    return response.json