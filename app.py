from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from resources.book import Book
from resources.user import User
import DB

app = Flask(__name__)
api = Api(app)
app.secret_key = "rkg"
jwt = JWT(app,authenticate,identity)

@app.before_first_request
def docreateTable():
    DB.create_Table()


api.add_resource(User,"/user")
api.add_resource(Book,"/book")
app.run(port=5000)