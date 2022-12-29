from connector import connection

from src.models.methods.auth.add_user import add_user_query
from src.models.methods.auth.check_user import check_user_query

def sign_up(username, password):
    with connection.cursor() as cursor:
        query = cursor.execute(check_user_query, username)
        user = query.fetchone()

        if user:
            print("username is already taken")

        else:
            cursor.execute(add_user_query, username, password)

def login(username, password):
    with connection.cursor() as cursor:
        query = cursor.execute(check_user_query, username)
        user = query.fetchone()

        if user:
            if password == user.password:
                print("200")

            else:
                print("password is incorrect")

        else:
            print("bad request")

