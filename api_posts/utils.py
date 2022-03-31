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


# возвращает один пост по его идентификатору
def get_post_by_pk(pk):
    posts = get_posts_all_from_json()
    for post in posts:
        if post['pk'] == pk:
            return post

