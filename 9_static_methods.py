
class School:

    # static variable - same for all obj
    __counter=1

    def __init__(self):
        #instance variable - new for every obj

        self.__roll_no=School.__counter
        School.__counter+=1
        self.__register=[]

    def add_std_details(self,name,ph):
        details={'name':name,'phone':ph,'roll_no':self.__roll_no}
        self.__register.append(details)

    @staticmethod
    def get_counter():
     return School.__counter
    
    @staticmethod
    def set_counter(new):
     if(type(new)==int):
        School.__counter=new
     else:
        print("Not Allowed ")
    
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


print(s3.set_counter(10))
print(s1._School__counter)
print(s3._School__counter)
print(s2.get_counter())


