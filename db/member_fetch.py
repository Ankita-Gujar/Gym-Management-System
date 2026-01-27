from db.db_connection import get_connection


def get_all_members():
    conn = get_connection()
    cursor = conn.cursor()

    query = """ SELECT * FROM members ORDER BY id ASC;"""


    cursor.execute(query)
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records
