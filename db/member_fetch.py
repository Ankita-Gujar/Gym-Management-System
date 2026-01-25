from db.db_connection import get_connection


def get_all_members():
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
            membership,
            address
        FROM members
        ORDER BY id DESC
    """

    cursor.execute(query)
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records
