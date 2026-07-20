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

    
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num =random.choices(string.digits,k=3)
        spchar = random.choices("! @#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)



    def createaccount(self):
        info ={
            "name":input("Tell your name :- "),
            "age":int(input("tell your age :- ")),
            "email" : input("tell your email :- "),
            "pin" : int(input("tell your 4 digit pin:- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance":0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print('sorry you can not create your account')
        else:
            print('account has been create succeessfully')
            for i in info:
                print(f"{i} : {info[i]}")
            print('please note down your account number')
            Bank.data.append(info)
            Bank.__update()

    def  depositemoney(self):
        accnumber = input("please tell your account number:- ")
        pin = int(input("please tell your pin number :-"))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print(userdata)
        if not userdata :
            print('userdata not found')
        else:
            amount = int(input("how much you  want to deposit:- "))
            if amount > 10000 or amount < 0 :
                print('sorry the deposite amount must in ramge of 1-10000')
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print('Amount Deposite Successfully')

    def  withdrawemoney(self):
        accnumber = input("please tell your account number:- ")
        pin = int(input("please tell your pin number :-"))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print(userdata)
        if not userdata :
            print('userdata not found')
        else:
            amount = int(input("how much you  want to withdraw:- "))
            if amount > 10000 or amount < 0 :
                print('sorry the withdraw amount must in ramge of 1-10000 ')
            elif  amount > userdata[0]['balance']:
                print('Sorry insufficient balance')
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print('Amount Withdraw Successfully')

    def  showdetails(self):
        accnumber = input("please tell your account number:- ")
        pin = int(input("please tell your pin number :-"))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print(userdata)
        if not userdata :
            print('userdata not found')
        else:
            print( f"your data showing successfully :- \n\n {userdata[0]}")

    def updatedetails(self):
        accnumber = input("please tell your account number:- ")
        pin = int(input("please tell your pin number :-"))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if not userdata :
            print('userdata not found')
        else:
            print( f"you can change age , accountNo. balance")
            print( f"Fill the details for change or leave it empty if no change")

            newData = {
                "name" : input("please tell your new name or press enter to skipp"),
                "email" : input("please tell your new email or press enter to skipp"),
                "pin" : input("please tell your new pin or press enter to skipp"),
            }
            if newData["name"] == "":
                newData['name'] = userdata[0]['name']
            if newData["email"] == "":
                newData['email'] = userdata[0]['email']
            if newData["pin"] == "":
                newData['pin'] = userdata[0]['pin']
            
            newData['age'] = userdata[0]['age']
            newData['accountNo.'] = userdata[0]['accountNo.']
            newData['balance'] = userdata[0]['balance']
            if type(newData['pin']) == int:
                newData['pin'] = int[newData['pin']]   
            
            for i in newData:
                if newData[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newData[i]

            Bank.__update()
            print("details updated succefully")
                


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

if check == 2:
    user.depositemoney()

if check == 3:
    user.withdrawemoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()