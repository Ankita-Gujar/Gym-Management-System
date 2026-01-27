from db.db_connection import get_connection  


def search_member_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
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
        WHERE email = %s
    """

    cursor.execute(query, (email,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
