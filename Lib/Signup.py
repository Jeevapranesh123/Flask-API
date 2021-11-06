import pymongo

client = pymongo.MongoClient('localhost')
db=client.API
Users=db.Users


class Signup:

    def __init__(self):
        pass


    # @staticmethod
    def createuser(self, username,email, password):
        data = {
            'username':username,
            'email': email,
            'Password': password
        }
        a = Users.find()

        for i in a:
            # print(i)
            if i['email'] == email:
                print('Email already exists')
                return False
        else:
            Users.insert_one(data)
            return True

    def verifytoken(self,username,password):
        pass




