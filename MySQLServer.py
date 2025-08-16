#!/usr/bin/env python3
import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        # connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # replace with your MySQL username
            password="password" # replace with your MySQL password
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
