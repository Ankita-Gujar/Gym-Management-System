from db.db_connection import get_connection

def delete_member_by_email(email):
    conn = get_connection()
    if conn is None:
        return False

    cursor = conn.cursor()

    # check if member exists
    cursor.execute(
        "SELECT * FROM members WHERE email=%s",
        (email,)
    )
    data = cursor.fetchone()

    if not data:
        return False

    # delete member
    cursor.execute(
        "DELETE FROM members WHERE email=%s",
        (email,)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return True
