from db.db_connection import get_connection

def search_member(email):
    conn = get_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members WHERE email=%s", (email,))
        data = cursor.fetchone()
        return data

    except Exception as e:
        print(e)
        return None

    finally:
        conn.close()
