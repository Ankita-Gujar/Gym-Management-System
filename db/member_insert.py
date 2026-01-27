from db.db_connection import get_connection

def insert_member(data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO members
            (first_name, last_name, gender, dob, email, contact, join_date, membership, address)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(query, data)
        conn.commit()

        return True

    except Exception as e:
        print("DB Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()
