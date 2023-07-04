import mysql.connector as connector

class DBHelper:

    global data_dict 
    data_dict = {"ID":"", "Name":"", "Phone Number":""}
    def __init__(self):
        self.conn = connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = 'Ritika@1900',
            database = 'pythontest',
        )
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.conn.cursor()
        cur.execute(query)
        print("created")
    
    def insert_user(self, userID, userName, phone):
        query = "insert into user(userID, userName, phone) values({},'{}','{}')".format(userID, userName, phone)
        cur = self.conn.cursor()
        cur.execute(query)
        result = self.conn.commit()
        print(result)
        self.conn.commit()

    def fetch_all(self):
        query = 'select * from user'
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
           data_dict['ID'] = row[0]
           data_dict['Name'] = row[1]
           data_dict['Phone Number'] = row[2]
           print(data_dict)

    def delete_user(self, userID):
        query = """
            delete from user 
            where userID = {}
        """.format(userID)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Data deleted for userID : {} and updated data is as follows:".format(userID))
        self.fetch_all()

    def update_data(self, userID, name, phone):
        query = "update user set userName = '{}', phone = '{}' where userID = {}".format(name, phone, userID)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Data is updated for userID : {} and updated table is as follows : ")
        self.fetch_all()
