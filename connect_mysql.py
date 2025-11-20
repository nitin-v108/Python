import mysql.connector
from mysql.connector import Error


def get_connection(
    host: str = "localhost",
    user: str = "root",
    password: str = "",
    database: str | None = None,
):
    """Return a mysql.connector connection or None on error.

    Replace the default args with your MySQL credentials before running.
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )
        if conn.is_connected():
            print("Connected to MySQL server")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None


if __name__ == "__main__":
    # Example usage: update with real credentials
    mydb = get_connection(host="localhost", user="root", password="", database="python")
    if mydb:
        # do work with `mydb` (create cursor, execute queries, etc.)
        mydb.close()
