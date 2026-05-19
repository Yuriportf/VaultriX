from django.db import connection


def create_transaction(user_id, description, amount, date, category_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO transactions (user_id, description, amount, date, category_id)
            VALUES (%s, %s, %s, %s, %s)
        """, [user_id, description, amount, date, category_id])