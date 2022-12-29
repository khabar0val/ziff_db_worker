from connector import connection

from src.models.methods.posts.add_post import add_post_query
from src.models.methods.posts.check_post import check_post_query

def add_post(url, data):
    with connection.cursor() as cursor:
        query = cursor.execute(check_post_query, url)
        post = query.fetchone()

        if post:
            print("this post is already exist")

        else:
            cursor.execute(add_post_query, url, data)

