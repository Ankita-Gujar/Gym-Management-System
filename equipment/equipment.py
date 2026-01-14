from db.db_connection import get_connection

def add_equipment(equipment_name, description, muscles_used, delivery_date, cost):
    conn = get_connection()
    if conn is None:
        return False, "DB Connection Failed"

    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO equipment 
        (equipment_name, description, muscles_used, delivery_date, cost)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (equipment_name, description, muscles_used, delivery_date, cost)
        )
        conn.commit()
        return True, "✅ Equipment added successfully"
    except Exception as e:
        return False, f"❌ Error: {e}"
    finally:
        cursor.close()
        conn.close()


def get_all_equipment():
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, equipment_name, description, muscles_used, delivery_date, cost 
            FROM equipment
        """)
        return cursor.fetchall()
    except Exception as e:
        print("❌ Fetch Error:", e)
        return []
    finally:
        cursor.close()
        conn.close()
