import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost',database='test_python',user='root',password='acpt')
    cursor = conn.cursor()
except:
    print("something went wrong")

finally:
    if conn.is_connected():
        conn.close()

