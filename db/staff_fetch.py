from db.db_connection import get_connection


def get_all_staff():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            id,
            first_name,
            last_name,
            gender,
            dob,
            email,
            contact,
            join_date,
            state,
            city
        FROM staff
        ORDER BY id DESC
    """

    cursor.execute(query)
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records
