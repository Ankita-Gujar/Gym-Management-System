from db.db_connection import get_connection

def add_equipment(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO equipment
        (equipment_name, description, muscles_used, delivery_date, cost)
        VALUES (%s, %s, %s, %s, %s) """

    cursor.execute(query, data)
    conn.commit()
    conn.close()
