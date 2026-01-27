from db.db_connection import get_connection

def add_staff(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO staff
        (first_name, last_name, gender, dob, email, contact, join_date, state, city)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, data)
    conn.commit()

    cursor.close()
    conn.close()
