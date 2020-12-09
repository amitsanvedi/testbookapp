from flask_restful import Resource,Api,reqparse
import DB

class User(Resource):
    # @jwt_required()
    def get(self):
        arrAllData = DB.fetchAllData()
        print(arrAllData)
        return {"Message":arrAllData}
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("id",
                            type=int,
                            required=True,
                            help="This field should not be blank")
        parser.add_argument("username",

                            required=True,
                            help="This field should not be blank")
        parser.add_argument("password",

                            required=True,
                            help="This field should not be blank")
        parser.add_argument("email",

                            required=True,
                            help="This field should not be blank")
        parser.add_argument("phone",
                            type=int,
                            required=True,
                            help="This field should not be blank")
        data = parser.parse_args()
        #data1 = request.get_json()
        #print(data)
        DB.insertData(data)
        return  {"Message":"User Registered Successfully"}

    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument("id",
                            type=int,
                            required=True,
                            help="This field should not be blank")
        parser.add_argument("email",

                            required=True,
                            help="This field should not be blank")
        parser.add_argument("phone",
                            type=int,
                            required=True,
                            help="This field should not be blank")
        data = parser.parse_args()
        #data1 = request.get_json()
        #print(data)
        DB.updateUserData(data)
        return  {"Message":"User Updated Successfully"}