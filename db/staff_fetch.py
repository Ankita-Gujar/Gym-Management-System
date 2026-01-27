from db.db_connection import get_connection


def get_all_staff():
    conn = get_connection()
    cursor = conn.cursor()

    query = """ SELECT * FROM staff ORDER BY id ASC;"""


    cursor.execute(query)
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records
