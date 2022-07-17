import mysql.connector as connector
import pickle
mydb=connector.connect(user='root',
                       password='himanshu@123',
                       host="localhost",
                       auth_plugin='mysql_native_password',
                       database='bankdb')

mycursor=mydb.cursor(buffered=True)
# created databased bankdb
# mycursor.execute('create database bankdb')
def Menu():
    print("*"*140)
    print("main menu".center(140))
    print("1. Insert Records as per Account Number".center(140))
    print("2. Display Record as per Account Number ".center(140))
    print("   a. Sorted as per Account Number ".center(140))
    print("   b. Sorted as per Customer Name ".center(140))
    print("   c. Sorted as per Customer Balance ".center(140))
    print("3. Search Record Details as per Account Number ".center(140))
    print("4. Update Record".center(140))
    print("5. Delete Record ".center(140))
    print("6. Transaction Debit/Withdraw and Credit from the Account".center(140))
    print("   a.Debit/Withdraw from the Account ".center(140))
    print("   b.Credit into the Account  ".center(140))
    print("7. Exit".center(140))
    print("*"*140)

def MenuSort():
    print("   a. Sorted as per Account Number ".center(140))
    print("   b. Sorted as per Customer Name ".center(140))
    print("   c. Sorted as per Customer Balance ".center(140))
    print("   d. Back".center(140))

def MenuTransaction():
    print("   a.Debit/Withdraw from the Account ".center(140))
    print("   b.Credit into the Account  ".center(140))
    print("   c.Back".center(140))

def Create():
    # try:
        mycursor.execute('create table if not exists sbi(ACCNO varchar(10), NAME varchar(20), MOBILE varchar(10), EMAIL varchar(20), ADDRESS varchar(20), CITY varchar(20), COUNTRY varchar(10), BALANCE varchar(20))')
        print("table created")
        Insert()
    # except:
    #     print("table exist")
    #     Insert()


#insert records
def Insert():
    while True:
        Acc=input("Enter account no ")
        Name=input("Enter Name ")
        Mob=input("enter Mobile ")
        email=input("enter email ")
        Add=input("enter Address")
        City=input("enter city")
        Country=input("enter Country ")
        Bal=float(input("enter balance "))
        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into sbi values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("do you want to enter more records")
        if ch=='N'  or ch=='n':
            break

 #function to display record as per ascending order of account no.      
def DispSortAcc():
    try:
        cmd="select * from sbi order by ACCNO"
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in s:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("table does not exist")

#function to display record as per ascending order of account name
def DispSortName():
    try:
        cmd="select * from sbi order by NAME"
        mycursor.execute(cmd)
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("table does not exist")


#function to display record as per ascending order by Balance
def DispSortBal():
    try:
        cmd="select * from sbi order by BALANCE"
        mycursor.execute(cmd)
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("table does not exist")

#function to search for the record 
def DispSearchAcc():
    try:
        cmd="select * from sbi "
        mycursor.execute(cmd)
        ch=input("enter the account no. to be searched ")
        for i in mycursor:
            if i[0]==ch:
                print("="*125)
                F="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*125)
                for j in i:
                    print("%14s" % j, end=' ')
                print()
                break
        else:
            print("records not found")
    except:
        print("table does not exist")


#function to change detail of a customer 
def Update():
    try:
        cmd="select * from sbi"
        mycursor.execute(cmd)
        A=input("enter the account no. whose detail to be changed")
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                ch=input("change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("enter Name ")
                    i[1]=i[1].upper()
                
                ch=input("change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("enter Mobile ")
                    i[2]=i[2].upper()

                ch=input("change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("enter Email ")
                    i[3]=i[3].upper()

                ch=input("change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("enter Address ")
                    i[4]=i[4].upper()
                
                ch=input("change City(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("enter City ")
                    i[5]=i[5].upper()

                ch=input("change Country(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("enter Country ")
                    i[6]=i[6].upper()
            

                ch=input("change Balance(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("enter Balance "))
                cmd="UPDATE sbi SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account updated")
                break
            else:
                print("record not found")
    except:
        print("no such table")

def Delete():
    try:
        cmd="select * from sbi "
        mycursor.execute(cmd)
        ch=input("enter the account no. whose details to be changed  ")
        for i in mycursor:
            i = list(i)
            if i[0]==A :
                cmd="delete from sbi where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account deleted ")
                break
        else:
            print("record not found")
    except:
        print("no such table")

def Debit():
    try:
        cmd=" select * from sbi"
        mycursor.execute(cmd)
        print("please note that money can only be debited if min bal of rs 5000 exist")
        acc=input("enter the account no from which money is to be debited ")
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("enter the amount to be withdrawl"))   
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE sbi SET BALANCE=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("amount debited")
                    break
                else:
                    print("there must be min bal of rs 5000")
                    break
        else:
            print("record not found ")
    except:
        print("table does not found")                


def Credit():
    try:
        cmd=" select * from sbi"
        mycursor.execute(cmd)
        #S = mycursor.fetchall()
        acc=input("enter the account no from which money credited ")
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("enter the amount to be withdrawl"))   
                i[7]+=Amt
                cmd="UPDATE sbi SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("amount debited")
                break
            
        else:
            print("record not found ")
    except:
        print("table does not found") 
while True:
    Menu()
    ch=input("enter your choice")
    if ch=='1':
        Create()
    elif ch=='2':
        while True:
            MenuSort()
            ch1=input("enter choice a/b/c/d")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("back to the main menu")
                break
            else:
                print("invalid choice") 
    elif ch=='3':
        DispSearchAcc()     
    elif ch=='4':
        Update()     
    elif ch=='5':
        Delete()     
    elif ch=='6':
        while True:
            MenuTransaction()
            ch1=input("enter choice a/b/c")
            if ch1 in ['a','A']:
                Debit()
            elif ch1 in ['b','B']:
                Credit()
            elif ch1 in ['c','C']:
                print("back to the main menu")
                break
            else:
                print("invalid choice")
    elif ch=="7":
        print("Exiting....")
        break
    else:
        print("wrong choice entered")      


            



            



            



            

