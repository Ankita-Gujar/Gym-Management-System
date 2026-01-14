from db.db_connection import get_connection


def add_member(first_name, last_name, gender, dob, email,
               contact, join_date, time_slot, membership_type, address):

    conn = get_connection()
    if conn is None:
        return False, "DB Connection Failed"

    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO members
        (first_name, last_name, gender, dob, email, contact,
         join_date, time_slot, membership_type, address)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            first_name,
            last_name,
            gender,
            dob,
            email,
            contact,
            join_date,
            time_slot,
            membership_type,
            address
        ))

        conn.commit()
        return True, "✅ Member added successfully"

    except Exception as e:
        return False, str(e)

    finally:
        conn.close()


def get_all_members():
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        return cursor.fetchall()

    except Exception as e:
        print(e)
        return []

    finally:
        conn.close()
