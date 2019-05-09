from pymongo import MongoClient

def connection():
    client = MongoClient()
    db = client.Myapp # Database
    return db

def signup(users):
    usr = input("Usuario: ")
    data = users.find_one({'username': usr})
    if data is not None:
        print("Ya existe un usuario con ese nombre")
        signup(users)
    psw = input("Password: ")
    result = users.insert_one({'username':usr, 'password': psw})
    print(result)

def login(users):
    usr = input("Usuario: ")
    data = users.find_one({'username': usr})
    if data is None:
        print("Ese usuario no existe")
        login(users)
    while True:
        psw = input("Password: ")
        data = users.find_one({'username':usr, 'password': psw})
        if data is None:
            print("Clave incorrecta")
            continue
        print(data)
        return True


def main():
    db = connection()
    users = db.users
    while True:
        option = input("1. Login - 2. Signup : ")
        if option is "1":
            login(users)
        else:
            signup(users)

main()
