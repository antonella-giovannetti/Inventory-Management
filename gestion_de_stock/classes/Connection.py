import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class Connection:
    def __init__(self):
        self.password = os.getenv("PASSWORD")
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=self.password,
            database="boutique"
        )
        self.cursor = self.connection.cursor()

