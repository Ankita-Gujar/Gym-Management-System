from db.db_connection import get_connection

def get_all_equipment():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM equipment")
    rows = cursor.fetchall()

    conn.close()
    return rows
