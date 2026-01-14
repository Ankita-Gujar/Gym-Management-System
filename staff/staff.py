from db.db_connection import get_connection


def add_staff(first_name, last_name, gender, dob, email, contact, join_date, state, city):
    conn = get_connection()
    if conn is None:
        return False, "DB Connection Failed"

    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO staff 
        (first_name, last_name, gender, dob, email, contact, join_date, state, city)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            first_name,
            last_name,
            gender,
            dob,
            email,
            contact,
            join_date,
            state,
            city
        ))
        conn.commit()
        return True, "✅ Staff added successfully"

    except Exception as e:
        return False, str(e)

    finally:
        conn.close()


def get_all_staff():
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM staff")
        return cursor.fetchall()

    except Exception as e:
        print(e)
        return []

    finally:
        conn.close()
