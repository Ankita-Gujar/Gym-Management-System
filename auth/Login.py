import bcrypt
from db.db_connection import get_connection


def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT password FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result:
        stored_password = result[0].encode()
        if bcrypt.checkpw(password.encode(), stored_password):
            return True
    return False
