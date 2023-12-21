import pymysql


class SingletonDatabase():
    _instance = None
    _db = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
            cls._db = pymysql.connect(host='127.0.0.1', port=8200, user='root',
                                      passwd='root', charset='utf8')
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        print("Initializing database...")

        with self._db.cursor() as cursor:
            db_sql = '''CREATE DATABASE IF NOT EXISTS metro_db default CHARACTER SET UTF8;'''
            table_sql = '''CREATE TABLE metro_db.subway (
                    `btrainNo` varchar(100) NOT NULL,
                    `subwayId` int NOT NULL,
                    `statnFid` int NOT NULL,
                    `statnTid` int NOT NULL,
                    `statnId` int NOT NULL,
                    `statnNm` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
                    `barvlDt` int NOT NULL,
                    PRIMARY KEY (`btrainNo`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;'''
            cursor.execute(db_sql)
            cursor.execute(table_sql)
            # result = cursor.fetchall()
            cursor.connection.commit()
            # return str(result)

    def get_db(self):
        return self._db


def get_db():
    return SingletonDatabase().get_db()
