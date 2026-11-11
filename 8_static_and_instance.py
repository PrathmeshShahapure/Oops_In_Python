
class School:

    # static variable - same for all obj
    counter=1

    def __init__(self):
        #instance variable - new for every obj

        self.__roll_no=School.counter
        School.counter+=1
        self.__register=[]

    def add_std_details(self,name,ph):
        details={'name':name,'phone':ph,'roll_no':self.__roll_no}
        self.__register.append(details)

    def get_cart_details(self):
     return self.__register.copy()

    
s1=School()
s1.add_std_details("Prath","123")

    
s2=School()
s2.add_std_details("PratiK","456")

    
s3=School()
s3.add_std_details("Teja","789")

print(s1._School__roll_no) #accessing private attribute
print(s2._School__roll_no)
print(s3._School__roll_no)

print()

print(s1.counter,end="\n")
print(s3.counter)
print(s3.counter)
print(School.counter)


