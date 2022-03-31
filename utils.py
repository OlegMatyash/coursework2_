import json


# список всех постов
def get_posts_all_from_json():

    with open('data.json', 'r', encoding='utf-8') as file:
        posts_old = json.load(file)
        posts = []
    for post in posts_old:
        post_del = post['content'].split(' ')
        content_short = post_del[0]+' '+post_del[2]+' '+post_del[3]+'...'
        new_rec_dict = {'short':f'{content_short}'}
        post.update(new_rec_dict)
        posts.append(post)
    return posts

# все комментарии к постам
def get_comment_all_from_json():

    with open('comments.json', 'r', encoding='utf-8') as file1:
        comments = json.load(file1)

    return comments


# возвращает посты определенного пользователя
def get_posts_by_user(poster_name):

    posts = get_posts_all_from_json()
    all_posts_user_name = []
    user_name_lower = poster_name.lower()
    for post in posts:
        if user_name_lower == post['poster_name'].lower():
            all_posts_user_name.append(post)
    return (all_posts_user_name)


# возвращает комментарии определенного поста
def get_comments_by_post_id(post_id):

    comments = get_comment_all_from_json()
    all_comments_post = []
    for comment in comments:
        if comment['post_id'] == post_id:
            all_comments_post.append(comment)
    return all_comments_post


# возвращает список постов по вхождению query
def search_for_posts(query):
    query_lower = query.lower()
    posts = get_posts_all_from_json()
    all_posts = []
    for post in posts:
        if query_lower in post['content'].lower():
            all_posts.append(post)

    return all_posts


# возвращает один пост по его идентификатору
def get_post_by_pk(pk):
    posts = get_posts_all_from_json()
    for post in posts:
        if post['pk'] == pk:
            return post

