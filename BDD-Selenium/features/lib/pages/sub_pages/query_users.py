import pymysql
from dotenv import load_dotenv
import os


class DataBase:

    def __init__(self):

        load_dotenv(os.getcwd() + "/../../data/.env.wordpress")

        host = os.getenv('HOST')
        user = os.getenv('USER_DB')
        password = os.getenv('PASSWORD')
        db = os.getenv('DATABASE')

        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        self.cursor = self.connection.cursor()

    def get_employee_by_id(self, user_name):

        try:
            sql = 'SELECT * FROM wp_users WHERE user_nicename=%s'
            value = user_name
            self.cursor.execute(sql, value)
            result = self.cursor.fetchone()

            return result

        except Exception as e:
            self.connection.rollback()
            print(f'Exception to get employee: {e}')

        finally:
            self.connection.close()



