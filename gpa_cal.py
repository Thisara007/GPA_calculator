GVP_=[]  #List for add Grade point Values
CRv=[]  #List for credit values
T=0
d=0
OGPA=float()
def cr_value(X):    #function for chek grade point value
    cr_val=float()
    if X in ["A+","A","A-","B+","B","B-","C+","C-","C","D+","D","E"]: #validating results
        if (X == "A+" or X =="A"):
            cr_val=4.00
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
        elif (X == "A-"):
            cr_val=3.70
            GVP_.append(cr_val)
        elif (X == "B+"):
            cr_val=3.30
            GVP_.append(cr_val)
        elif (X == "B"):
            cr_val=3.00
           # print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
        elif (X == "B-"):
            cr_val=2.70
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
            return cr_val
        elif (X == "C+"):
            cr_val=2.30
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
        elif (X == "C"):
            cr_val=2.00
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
        elif (X == "C-"):
            cr_val=1.70
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
        elif (X == "D+"):
            cr_val=1.305
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
        elif (X == "D"):
            cr_val=1.00
            #print("creadit value of subject:",cr_val)
        elif (X == "E"):
            cr_val=0.00
            #print("creadit value of subject:",cr_val)
            GVP_.append(cr_val)
    else:
        print("Not a valid Result,Please Enter again.\n\n")
        return 0 

def BF_():
    res1=input("Enter your result of SUBJECT 1(A+,A,A-,B+,B,B-,C+,C-,c,D+,D,E) :")
    while cr_value(res1)== 0:
         res1=input("Enter your result of SUBJECT 1(A+,A,A-,B+,B,B-,C+,C-,c,D+,D,E) :")
    while True:   
            credit_1=int(input("Enter credit value for SUBJECT 1:"))
            CRv.append(credit_1)
            try:    
                credit_1=int(credit_1)
                CRv.append(credit_1)
                break
            except ValueError:    
                    print("Please Enter  valid credit mark..")
                    print("Creadit value should be less than 10 & greter than 0")
     
GVP_.clear()
CRv.clear()  
while(True):
    sub_c=int(input("How many subject doyou face::::"))
    i=0
    while(sub_c>0):
            BF_()
            T=T+(GVP_[i]*CRv[i]) 
            d=d+CRv[i]
            sub_c=sub_c-1
            i=i+1
    OGPA=T/d
    print("Your Overall GPA :",OGPA)
    print("-+"*40) 
    GVP_.clear()
    CRv.clear()                           
 #calculate Over all GPA
          
                    

