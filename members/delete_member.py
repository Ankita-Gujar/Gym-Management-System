from db.db_connection import get_connection

def delete_member(email):
    conn = get_connection()
    if conn is None:
        return False, "DB Connection Failed"

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM members WHERE email=%s", (email,))
        conn.commit()

        if cursor.rowcount == 0:
            return False, "❌ No member found with this email"

        return True, "✅ Member deleted successfully"

    except Exception as e:
        return False, str(e)

    finally:
        conn.close()
