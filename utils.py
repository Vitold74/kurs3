import json


def get_posts_all():
    """
    Создает дикт со всеми постами
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        all_posts = json.load(file)
    return all_posts


def get_posts_by_user(user_name):
    """
    Сортирует посты по имени пользователя
    """
    all_posts = get_posts_all()
    posts = []

    for post in all_posts:
        if post['poster_name'] == user_name.lower():
            posts.append(post)

    if len(posts) > 0:
        return posts
    raise ValueError('No posts by this user')


def get_comments_by_post_id(post_id):
    """
    Создает дикт со всеми комментариями и сортирует их по id
    """
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)

    comments_by_id = []

    for comment in comments:
        if comment['post_id'] == post_id:
            comments_by_id.append(comment)

    if len(comments_by_id) > 0:
        return comments_by_id
        raise ValueError('No comments here')


def search_for_posts(query):
    """
    Сортирует посты по поисковому слову
    """
    posts = get_posts_all()
    posts_by_word = []

    for post in posts:
        if query.lower() in post['content'].lower():
            posts_by_word.append(post)

    if len(posts_by_word) > 0:
        return posts_by_word
    raise ValueError('Posts not found')


def get_posts_by_pk(uid):
    """
    Выводит пост по его pk
    """
    posts = get_posts_all()
    post_by_pk = []

    for post in posts:
        if post["pk"] == uid:
            post_by_pk.append(post)

    if len(post_by_pk) > 0:
        return post_by_pk
        raise ValueError('No posts')

