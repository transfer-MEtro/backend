import pymysql


class SingletonDatabase():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', port=8200, user='root',
                                  passwd='root', charset='utf8')
        self.init_db()

    def init_db(self):
        print("Intializing database...")

        with self.db.cursor() as cursor:
            db_sql = '''CREATE DATABASE IF NOT EXISTS pbj_db default CHARACTER SET UTF8;'''
            table_sql = '''CREATE TABLE IF NOT EXISTS pbj_db.Score
                    (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,
                        score INT NOT NULL
                    ) ENGINE = INNODB DEFAULT CHARSET=utf8mb4;'''
            cursor.execute(db_sql)
            cursor.execute(table_sql)
            # result = cursor.fetchall()
            cursor.connection.commit()
            # return str(result)


def get_db():
    return SingletonDatabase().db
