# -*- coding: UTF-8 -*-

import pymysql

# 兼容MySQLdb
pymysql.install_as_MySQLdb()


class DB(object):
    # 初始化对象，产生一个mysql连接
    def __init__(self, ip, user, passwd, db, port=3306, charset='utf8'):
        self._ip = ip
        self._user = user
        self._passwd = passwd
        self._db = db
        self._port = port
        self._charset = charset
        self._conn = None
        self._cursor = None
        try:
            self._conn = pymysql.connect(
                host=self._ip,
                user=self._user,
                password=self._passwd,
                database=self._db,
                charset=self._charset,
                port=self._port,
                autocommit=True
            )
        except Exception as err:
            format_err = f"ERROR - {self._ip} db init failed: {err}" + "\n"
            raise Exception(format_err)

    # 调用with方法的入口
    def __enter__(self):
        return self

    # 调用with方法结束时启动
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    # 查询函数
    def query(self, sql):
        """
        :param sql: 查询语句
        :return: result-查询结果;
        """
        cursor = self._conn.cursor(pymysql.cursors.DictCursor)
        try:
            result = []
            rows = cursor.execute(sql)
            if rows > 0:
                sql_result = cursor.fetchall()
                # result = [list(i) for i in sql_result]
                result = sql_result
            cursor.close()
            return result
        except Exception as err:
            format_err = f"ERROR - {self._ip} query failed: {err} - {sql}" + "\n"
            raise Exception(format_err)
        finally:
            cursor.close()

    # 单条dml语句
    def change(self, sql):
        """
        :param sql: dml语句
        :return : rows-改动的记录条数
        """
        cursor = self._conn.cursor()
        try:
            rows = cursor.execute(sql)
            return rows
        except Exception as err:
            format_err = f"ERROR - {self._ip} change failed: {err} - {sql}" + "\n"
            raise Exception(format_err)
        finally:
            cursor.close()

    # 多条dml语句
    def change_many(self, sql, value_list):
        """
        :param sql: 修改语句
        :param value_list: 参数值列表
        :return:rows-改动的记录条数
        """
        cursor = self._conn.cursor()
        try:
            rows = cursor.executemany(sql, value_list)
            return rows
        except Exception as err:
            format_err = f"ERROR - {self._ip} change_many failed: {err} - {sql}" + "\n"
            raise Exception(format_err)
        finally:
            cursor.close()

# if __name__ == "__main__":
#     with DB(ip="127.0.0.1", user="root", passwd="root", db="yiliangou") as db:
#         sql = 'select * from xy_staff where staff_id=5'
#         row = db.query(sql)
#         print(row)

# sql_insert_many = 'insert into test.test (name) values (%s)'
# value_list = ["chen", "zc"]

# row = db.change_many(sql_insert_many, value_list)

# r1 = db.query("select * from test.test")
# print(r1)

# row2 = db.change(f"insert into test (name) values ('zhang')")
# print(row2)
#
# r2, row3 = db.query("select * from test.test")
# print(r2)
