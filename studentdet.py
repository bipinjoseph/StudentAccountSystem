stulist=[]

class Studentaccount:
    def __init__(self,name,admnum,std,address,dob,email,email2,tele):
        self.name=name
        self.admnum=admnum
        self.std=std
        self.address=address
        self.dob=dob
        self.mk1=0
        self.mk2=0
        self.mk3=0
        self.mk4=0
        self.mk5=0
        self.total=0
        self.result=""
        self.cgpa=0
        self.gmk1=""
        self.gmk2=""
        self.gmk3=""
        self.gmk4=""
        self.gmk5=""
        self.grade=""
        self.email=email
        self.email2=email2
        self.tele=tele



    def addmark(self,m1,m2,m3,m4,m5):
        self.mk1=m1
        self.mk2=m2
        self.mk3=m3
        self.mk4=m4
        self.mk5=m5
        self.total=self.mk1+self.mk2+self.mk3+self.mk4+self.mk5 
        self.cgpa=(self.total/500)*10

    def updatemark(self,m1,m2,m3,m4,m5):
        self.mk1=m1
        self.mk2=m2
        self.mk3=m3
        self.mk4=m4
        self.mk5=m5
        self.total=self.mk1+self.mk2+self.mk3+self.mk4+self.mk5  
        self.cgpa=(self.total/500)*10


    def calculate(self):


        def mk(mark):


            g=""

            if(100>=mark>=90):
                g="A"
            elif(89>=mark>=80):
                g="B"
            elif(79>=mark>=70):
                g="C"
            elif(69>=mark>=60):
                g="D"
            elif(59>=mark>=50):
                g="E"

            elif(mark<50):
                g="F"
            
            return g
        
        self.gmk1=mk(self.mk1)
        self.gmk2=mk(self.mk2)
        self.gmk3=mk(self.mk3)
        self.gmk4=mk(self.mk4)
        self.gmk5=mk(self.mk5)





        
        def tmark(m):


            gr=""
            status=""


            if(500>=m>=450):
                gr="A"
                status="Passed"
            elif(449>=m>=400):
                gr="B"
                status="Passed"
            elif(399>=m>=350):
                gr="C"
                status="Passed"
            elif(349>=m>=200):
                gr="D"
                status="Passed"
            elif(199>=m>=151):
                gr="E"
                status="Passed"

            elif(m<=150):
                gr="F"
                status="Failed"
            
            return gr,status
        
        self.grade=tmark(self.total)




        self.result =f'''             STUDENT RESULT
        ------------------------------------------------------------------------------
   
NAME :  {self.name}                        ADMISSION  NO: {self.admnum}
CLASS:  {self.std}                          PLACE: {self.address}

--------------------------------------------------------------------------------------
SL NO        SUBJECT           MARKS SCORED       TOTAL MARKS           GRADE 
--------------------------------------------------------------------------------------

1.          PHYSICS            {self.mk1}            100            {self.gmk1}
2.          CHEMISTRY          {self.mk2}            100            {self.gmk2}
3.          ENGLISH            {self.mk3}            100            {self.gmk3}
4.          MATHS              {self.mk4}            100            {self.gmk4}
5.          BIOLOGY            {self.mk5}            100            {self.gmk5}

-----------------------------------------------------------------------------------
                        MARKS OBT :{self.total}        TOTAL: 500     {self.grade[0]}
                                                       STATUS:{self.grade[1]}
                        CGPA OUT 10: {self.cgpa}
----------------------------------------------------------------------------------                        


                                                                        '''
        print(self.result)


    def Studetails(self,):
        print(f'''
                    Student Details:
                    ------------------------------------------------------------
                    Student Name:{self.name}
                    Student Class:{self.std}
                    Admission Number :{self.admnum}
                    Student Address: {self.address}
                    ------------------------------------------------------------
                    Mark Details:
                    ------------------------------------------------------------
                    1. Physics:{self.mk1}
                    2. Chemistry:{self.mk2}
                    3. English:{self.mk3}
                    4. Maths:{self.mk4}
                    5. Biology:{self.mk5}

                    Total Marks Of 5 Subjects:{self.total}
                   -------------------------------------------------------------       ''')
        






    


def select():

    choice=int(input('''
                        
                        1. Add New Student
                        2. Login Into Student Account
                        3. List All Students
                        4. Exit
                        
                        Select Any Option To Proceed : '''))
    


    if(choice==1):
        print("Student Added")

        name=input("Enter the name of the student: ")
        adm=int(input("Enter the admission number of the student: "))
        std=int(input("Enter the the class of the student: "))
        addr=input("Enter the address of the student: ")
        dob=input("Enter you date of birth in ddmmyyyy format: ")
        em=input("Enter the email of the student: ")
        em2=input("Enter the email of the parent: ")
        phone=(input("Enter the phone number of the student: "))
        newstudent=Studentaccount(name,adm,std,addr,dob,em,em2,phone)
        stulist.append(newstudent)

        newstudent.Studetails()
        
        select()

    elif(choice==2):    #1. student details 2.add marks 3.generate result 4. update marks 5. send result 6. delete student 7. logout
        print("Logged In")
        l=int(input("Enter the student's admission number: "))
        bir=input("Enter the studnts' date of birth in ddmmyyyy format: ")
        for w in stulist:
            if(w.admnum==l and w.dob==bir):
                print("Successfully Loged In")
                print(f"Welcome{w.name} and your admission number is{w.admnum} ")

                def sel():

                    l2=int(input(''' 
                                    1. Student Details
                                    2. Add Marks
                                    3. Generate Result
                                    4. Update Mark
                                    5. Send Result
                                    6. Delete Student
                                    7. Logout
                                    
                                    Select your option to proceed: '''))
                    
                    if(l2==1):
                        print("Fetching Student Details")
                        w.Studetails()

                        sel()

                    elif(l2==2):
                        print("Add Marks")
                        m1=int(input("Enter the marks of Physics: "))
                        m2=int(input("Enter the marks of Chemistry : "))
                        m3=int(input("Enter the marks of English : "))
                        m4=int(input("Enter the marks of Maths : "))
                        m5=int(input("Enter the marks of Biology : "))

                        
                        w.addmark(m1,m2,m3,m4,m5)



                        sel()
                    
                    elif(l2==3):
                        print("Generate Result")

                        w.calculate()

                        sel()


                    elif(l2==4):
                        print("Update Mark")

                        m1=int(input("Enter the marks of Physics: "))
                        m2=int(input("Enter the marks of Chemistry : "))
                        m3=int(input("Enter the marks of English : "))
                        m4=int(input("Enter the marks of Maths : "))
                        m5=int(input("Enter the marks of Biology : "))
                        w.updatemark(m1,m2,m3,m4,m5)

                        sel()


                    elif(l2==5):
                        print("Send Result")


                        import smtplib
                        from email.mime.text import MIMEText
                        subject = f"Result of the Student {w.name} "
                        body = f'''The result of the student {w.name}
                                    Having admission number {w.admnum} is published below
                                    {w.result}
                                        '''

                        sender = "bipinjoseph2003@gmail.com"
                        recipients = [w.email,w.email2]
                        password = "drfpqwhpyvdualib" # passwrod generated to use smtp service


                        def send_email(subject, body, sender, recipients, password):
                                msg = MIMEText(body)
                                msg['Subject'] = subject
                                msg['From'] = sender
                                msg['To'] = ', '.join(recipients)
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                                 smtp_server.login(sender, password)
                                 smtp_server.sendmail(sender, recipients, msg.as_string())
                                print("Message sent!")


                        send_email(subject, body, sender, recipients, password)



                        from twilio.rest import Client
                        account_sid = 'AC2862d58c2efcf4a767aeae61bb31dce5'
                        auth_token = 'c81b9b584878262f52224b71b26ed917'
                        client = Client(account_sid, auth_token)
                        message = client.messages.create(
                        messaging_service_sid='MGda4b100daeee215fef5a4e14898ea299',
                        body=f'''The result of the student {w.name}
                                    Having admission number {w.admnum} is published below
                                    {w.result}''',
                        to=w.tele
                        )
                        print(message.sid)






                        sel()




                    elif(l2==6):
                     print("Delete Student")
                     stulist.remove(w)


                     select()

                    elif(l2==7):
                        print("Log Out")
                        select()

                    else:
                        print("Invalid Choice ")
                        sel()




                sel()
        select()

    elif(choice==3):
        print("Listing All Students")
        for stu in stulist:
            print(f"The name of the student is {stu.name} and admission number is {stu.admnum} studying in {stu.std} standard. ")


        select()

    elif(choice==4):
        print("Exited")
        
              
    else:
        print("Invalid Input")
        select()
        

select()

    
 