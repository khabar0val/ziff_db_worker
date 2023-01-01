from connector import connection

import src.db.methods.auth.add_user as add
import src.db.methods.auth.check_user as check

def sign_up(username, password):
    with connection.cursor() as cursor:
        query = cursor.execute(check.check_user_query, username)
        user = query.fetchone()

        if user:
            print("username is already taken")

        else:
            cursor.execute(add.add_user_query, username, password)

def login(username, password):
    with connection.cursor() as cursor:
        query = cursor.execute(check.check_user_query, username)
        user = query.fetchone()

        if user:
            if password == user.password:
                print("200")

            else:
                print("password is incorrect")

        else:
            print("bad request")

