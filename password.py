 
import pickle
import os,sys

password=""


lst=[]
if os.path.isfile('password_storage.pkl'):            
    f=open('password_storage.pkl','rb')
    lst=pickle.load(f)
    password=pickle.load(f)

    vpass=input("Enter Password : ")
    while vpass!=password:
        vpass=input("Enter Password : ")    


    f.close()
else:

    password1="password"
    cnfpasswrod="cnfpassword"
    while password1!=cnfpasswrod:
        password1=input("Create Password : ")
        cnfpasswrod=input("confirm password : ")
        if(password1==cnfpasswrod):
            password=password1


    print("You Are New Here !!")
    print('''What We Provide :- 
                - store password on local storage 
                - provide security and privecy
                - easy to use and mantain you password     ''')        
    print(''''Note :- You found a file named 'password_storage.pkl' in which your all password is saved 
                        so keep the file along with the app to access your password .... ''')

    print("To Get Help About commands type 'help'")                    
    f=open('password_storage.pkl','wb+')
    f.close()
    



def save():
    f=open('password_storage.pkl','wb')
    pickle.dump(lst,f)
    pickle.dump(password,f)
    f.close()




def help():
    print("This is Help window ")
    print("*"*30)
    print("helo                 :   open help menu")
    print("add                  :   save new password")
    print("show                 :   show all account's name you have saved ")
    print("update               :   update/edit account details ")
    print("account              :   print account details of passed id")
    print("exit                 :   Exit \n")





def show():
    print("-------Accounts-------------")
    count=0
    for i in lst:
       print(str(count)  +"   "+ i['name'])
       count+=1
    print("*"*50)   

def printdata(id):
    print("-------account details-------")
    id=int(id)
    try:
        for key,value in lst[id].items():
            print(key + ':' + value)
        return True
    except:
        print("Account ID is invalid")
        return False
    finally:
        print("*"*50)    
               

def addnew():
    name=input("Website Name/url/app name  : ")
    userid=input("Enter userId : ")
    password=input("Enter Password : ")
    lst.append({'name':name,'userid':userid,'password':password})
    print("*"*50)
    save()

def update(id):
    verif=printdata(id)
    if(verif==True):    
        print("Enter Key:value to update a value ")
        x,y=input().split(':')
        d={x:y}
        id=int(id)
        lst[id].update(d)
        save()
    print("*"*50)

choice='null'
while(choice!='exit'):
    choice=input(">>> ")
    if(choice=='add'):
        addnew()
    elif(choice=='account'):
        x=input("ID : ")
        printdata(x)
    elif(choice=='update'):
        x=input("ID : ")
        update(x)    
    elif(choice=='exit'):
        exit  
    elif(choice=='help'):
        help()
    elif(choice=='show'):
        show()    

    
save()

'''about  :
   version -- v1.0 #
  
next:-
   version -- v1.1
       feature :
       - last updated date 
       - account date
       -login
       
   '''