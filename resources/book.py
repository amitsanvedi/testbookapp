from flask import Flask,request
from flask_restful import Resource,Api,reqparse
import sqlite3
import DB
from flask_jwt import JWT,jwt_required


class Book(Resource):
    def get(self):
        arrAllData = DB.fetchAllBooks()
        return {"Data":arrAllData}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id",
                            type=int,
                            required = True,
                            help="This field should not be blank")
        parser.add_argument("name",

                            required = True,
                            help="This field should not be blank")
        parser.add_argument("userId",
                            type=int,
                            required = True,
                            help="This field should not be blank")
        data = parser.parse_args()
        DB.insertBook(data)
        return {"Message":"Book Inserted"}