import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print('no such file exist')
    except  Exception as err:
        print(f"an error occured {err}")


    def createaccount(self):
        pass

user = Bank()
print('Press 1 for creating an account')
print('Press 2 for depositing the money in the account')
print('press 3 for withdraw the money')
print('press 4 for details')
print('press 5 for updating the details')
print('press 6 for deleting your account')

check = int(input('tell your response :- '))

if check == 1:
    user.createaccount()