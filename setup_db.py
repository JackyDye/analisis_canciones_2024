import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("HOSTNAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    port=os.getenv("PORT")
)

cursor = connection.cursor()

with open("sql/spotify_2024_database.sql", "r", encoding="utf8") as f:
    sql = f.read()

for result in connection.cmd_query_iter(sql):
    pass

connection.commit()
cursor.close()
connection.close()

print("Base de datos creada exitosamente.")