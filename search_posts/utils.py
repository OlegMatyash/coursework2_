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


# возвращает список постов по вхождению query
def search_for_posts(query):
    query_lower = query.lower()
    posts = get_posts_all_from_json()
    all_posts = []
    for post in posts:
        if query_lower in post['content'].lower():
            all_posts.append(post)

    return all_posts

