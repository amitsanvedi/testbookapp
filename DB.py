import sqlite3





def create_Table():
    db = sqlite3.connect("postgres://jvcloxdykhdrkz:6905f4a01a36158bde1579aaf6537bed6ec635dcb0ea28ba27324987388b14f4@ec2-54-243-67-199.compute-1.amazonaws.com:5432/dafdms6cep8kta
                         ")
    cursor = db.cursor()
    createUserTable = "CREATE TABLE IF NOT EXISTS users(id Integer,username Text,password Text,email Text,Phone Integer)"
    cursor.execute(createUserTable)

    createTable = "CREATE TABLE IF NOT EXISTS books(id Integer,name Text,userId Integer)"
    cursor.execute(createTable)
    createAuthTable = "CREATE TABLE IF NOT EXISTS author(id Integer,name Text,bookId Integer)"
    cursor.execute(createAuthTable)
    db.commit()
    db.close()

def insertData(userData):
    print(userData)
    db = sqlite3.connect("book.db")
    cursor = db.cursor()
    insert_query = "INSERT INTO users VALUES(?,?,?,?,?)"
    userTuple = (userData["id"],userData["username"],userData["password"],userData["email"],userData["phone"])
    cursor.execute(insert_query,userTuple)
    db.commit()
    db.close()
    print("Test")

def updateUserData(userData):
    print(userData)
    db = sqlite3.connect("book.db")
    cursor = db.cursor()
    insert_query = "UPDATE users set email=?,phone=? where id=?"
    userTuple = (userData["email"],userData["phone"],userData["id"])
    cursor.execute(insert_query,userTuple)
    db.commit()
    db.close()
    print("Test")

def fetchAllData():
    db = sqlite3.connect("book.db")
    cursor = db.cursor()
    allData_Query = "SELECT * from users"
    arrAllData = []
    result = cursor.execute(allData_Query)
    for row in result:
        if row:
            arrAllData.append({"id":row[0],"username":row[1],"password":row[2],"email":row[3],"phone":row[4]})

    db.commit()
    db.close()
    return arrAllData

def insertBook(bookData):
    print(bookData)
    db = sqlite3.connect("book.db")
    curser = db.cursor()
    insertQuery = "INSERT INTO books VALUES(?,?,?)"
    usertuple = (bookData['id'], bookData['name'],bookData['userId'])
    curser.execute(insertQuery, usertuple)
    db.commit()
    db.close()

def fetchAllBooks():
    allBooks = []
    db = sqlite3.connect("book.db")
    curser = db.cursor()
    allDataQuery = "SELECT * from books"
    result = curser.execute(allDataQuery)
    for row in result:
        allBooks.append({"id":row[0],"name":row[1],"userId":row[2]})

    return allBooks

def login(user):
    db = sqlite3.connect("book.db")
    cursor = db.cursor()
    validateQuery = "SELECT * FROM users where username = ? AND password =?"
    loginTuple = (user['username'],user['password'])
    result = cursor.execute(validateQuery,loginTuple)
    row = result.fetchone()
    if row:
        return {"Message":"Login Successfully","data":{"userId":row[0],"username":row[1]}}

    return  {"Message":"Credentials are invalid"}
    db.close()
def docheckUser(username):
    db = sqlite3.connect("book.db")
    cursor = db.cursor()
    validateQuery = "SELECT * FROM users where username = ?"
    result = cursor.execute(validateQuery,(username,))
    row = result.fetchone()
    if row:
        return {"id":row[0],"username":row[1],"password":row[2],"email":row[3],"phone":row[4]}

    return  {"Message":"Credentials are invalid"}
    db.close()

def docheckUserid(username):
    db = sqlite3.connect("book.db")
    print("id found")
    print(username)
    cursor = db.cursor()
    validateQuery = "SELECT * FROM users where id = ?"
    result = cursor.execute(validateQuery,(username,))
    row = result.fetchone()
    db.close()
    if row:
        return {"id":row[0],"username":row[1],"password":row[2],"email":row[3],"phone":row[4]}

    return  {"Message":"Credentials are invalid"}
