# 这是py连接mysql的所有函数

import pymysql


def get_db_connection():
    """获取数据库连接"""
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="040708",
        database="web",
        cursorclass=pymysql.cursors.DictCursor
    )

def Add_User(name, pswd):
# 注册时添加用户信息
    connection = pymysql.connect(
        host="127.0.0.1",  # 数据库服务器地址
        user="root",  # MySQL用户名
        password="040708",  # MySQL用户密码
        database="web",  # 要连接的数据库名
        cursorclass=pymysql.cursors.DictCursor  # 使用字典游标
    )
    cursor = connection.cursor()

    sql = "INSERT INTO users (username, pswd) VALUES (%s, %s)"
    cursor.execute(sql, (name, pswd))
    connection.commit()  # 提交事务

    if connection and connection.open:
        connection.close()
        print("MySQL连接已关闭")

def Edit_User(name, pswd, pre_name):
# 注册时添加用户信息
    connection = pymysql.connect(
        host="127.0.0.1",  # 数据库服务器地址
        user="root",  # MySQL用户名
        password="040708",  # MySQL用户密码
        database="web",  # 要连接的数据库名
        cursorclass=pymysql.cursors.DictCursor  # 使用字典游标
    )
    cursor = connection.cursor()

    sql = """UPDATE users
            SET username = (%s), pswd = (%s)
            WHERE username = (%s)"""
    cursor.execute(sql, (name, pswd, pre_name))
    connection.commit()  # 提交事务

    if connection and connection.open:
        connection.close()
        print("MySQL连接已关闭")

def Is_Existed(name, pswd):
    connection = pymysql.connect(
        host="127.0.0.1",  # 数据库服务器地址
        user="root",  # MySQL用户名
        password="040708",  # MySQL用户密码
        database="web",  # 要连接的数据库名
        cursorclass=pymysql.cursors.DictCursor  # 使用字典游标
    )
    cursor = connection.cursor()

    sql = "SELECT * FROM users"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    if connection and connection.open:
        connection.close()
        print("MySQL连接已关闭")

    for row in results:
        if name == row['username'] and pswd ==row['pswd']:
            print('成功')
            return True

def Find_Data(name):
    connection = pymysql.connect(
        host="127.0.0.1",  # 数据库服务器地址
        user="root",  # MySQL用户名
        password="040708",  # MySQL用户密码
        database="web",  # 要连接的数据库名
        cursorclass=pymysql.cursors.DictCursor  # 使用字典游标
    )
    cursor = connection.cursor()

    sql = """SELECT * FROM health_index
            where 姓名=(%s) """
    cursor.execute(sql, (name))
    results = cursor.fetchall()

    if connection and connection.open:
        connection.close()
        print("MySQL连接已关闭")

    return results

def test_Data():
    connection = pymysql.connect(
        host="127.0.0.1",  # 数据库服务器地址
        user="root",  # MySQL用户名
        password="040708",  # MySQL用户密码
        database="web",  # 要连接的数据库名
        cursorclass=pymysql.cursors.DictCursor  # 使用字典游标
    )
    cursor = connection.cursor()

    sql = """SELECT * FROM health_index
            where 姓名=(%s) """
    cursor.execute(sql, ('小张'))
    results = cursor.fetchall()

    for row in results:
        print(row)

    if connection and connection.open:
        connection.close()
        print("MySQL连接已关闭")


if __name__ == "__main__":
    test_Data()

# datas=[{'姓名': '小张', '血压': '137/85', '空腹血糖': '5.8', 
#         '胆固醇': '4.8', '肝功能': '肝功能指标异常', 
#         '尿酸': '340', '白细胞': '7.2', '日期': '2023-01-01'}]