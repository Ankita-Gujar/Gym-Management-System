from db.db_connection import get_connection

def fetch_dashboard_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Total members
    cursor.execute("SELECT COUNT(*) FROM members")
    total = cursor.fetchone()[0]

    # Active members
    cursor.execute("""
        SELECT COUNT(*) FROM members
        WHERE
        (
            (membership='Monthly' AND join_date >= CURDATE() - INTERVAL 30 DAY)
         OR (membership='Quarterly' AND join_date >= CURDATE() - INTERVAL 90 DAY)
         OR (membership='Yearly' AND join_date >= CURDATE() - INTERVAL 365 DAY)
        )
    """)
    active = cursor.fetchone()[0]

    # Inactive members
    cursor.execute("""
        SELECT COUNT(*) FROM members
        WHERE
        (
            (membership='Monthly' AND join_date < CURDATE() - INTERVAL 30 DAY)
         OR (membership='Quarterly' AND join_date < CURDATE() - INTERVAL 90 DAY)
         OR (membership='Yearly' AND join_date < CURDATE() - INTERVAL 365 DAY)
        )
    """)
    inactive = cursor.fetchone()[0]

    # Expiring in 7 days
    cursor.execute("""
        SELECT COUNT(*) FROM members
        WHERE
        (
            (membership='Monthly' AND join_date BETWEEN CURDATE() - INTERVAL 23 DAY AND CURDATE() - INTERVAL 30 DAY)
         OR (membership='Quarterly' AND join_date BETWEEN CURDATE() - INTERVAL 83 DAY AND CURDATE() - INTERVAL 90 DAY)
         OR (membership='Yearly' AND join_date BETWEEN CURDATE() - INTERVAL 358 DAY AND CURDATE() - INTERVAL 365 DAY)
        )
    """)
    expiring = cursor.fetchone()[0]

    # Joined today
    cursor.execute("""SELECT COUNT(*) FROM members
    WHERE DATE(join_date) = CURDATE()""")
    joined_today = cursor.fetchone()[0]

    # Attendance (assume active members present)
    attendance = active

    cursor.close()
    conn.close()

    return total, active, inactive, expiring, joined_today, attendance
