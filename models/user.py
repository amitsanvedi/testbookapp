import sqlite3
from flask_restful import Resource, reqparse


class User():
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password,email,phone):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('book.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = User(row[0],row[1],row[2],row[3],row[4])#{"id":row[0],"username":row[1],"password":row[2],"email":row[3],"phone":row[4]}#cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('book.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            #user = {"id":row[0],"username":row[1],"password":row[2],"email":row[3],"phone":row[4]}#cls(*row)
            user = User(row[0],row[1],row[2],row[3],row[4])
        else:
            user = None

        connection.close()
        return user