import pymysql

def get_connection():
    try:
        print("Connecting to database...")
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Pavan@8010",
            database="gym_management",
            port=3306,
            connect_timeout=3
        )
        print("Database connected")
        return conn
    except Exception as e:
        print("Database connection failed")
        print(e)
        return None
