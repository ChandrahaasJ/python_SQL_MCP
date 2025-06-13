from dotenv import load_dotenv
import os
import gspread
from google.oauth2.service_account import Credentials
import mysql.connector

class Auth:
    sheetid=""
    DBuser="" 
    DBpass=""
    DBname=""
    path=r"C:\EAG\session8\tests\sheetsapi\credentials.json"
    def __init__(self,path_to_env):
        load_dotenv(dotenv_path=path_to_env)
        self.DBname=os.getenv("DBNAME")
        self.DBpass=os.getenv("DBPASS")
        self.DBuser=os.getenv("DBUSER")
        self.sheetid=os.getenv("SHEET")#the sheet you want to connect with
        #self.path=os.getenv("CRED_PATH")#sheets_api credentials path
    
    def initialize_sheets(self):
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        creds=Credentials.from_service_account_file(self.path, scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(self.sheetid)
        return sheet.worksheets()
    
    def initialize_database(self):
        conn = mysql.connector.connect(
            host="localhost",       # or remote IP/domain
            user=self.DBuser,
            password=self.DBpass,
            database=self.DBname
        )
        cursor=conn.cursor()
        return cursor,conn