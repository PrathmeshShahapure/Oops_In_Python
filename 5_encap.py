# Shopping Cart Management
# Noting in py is truely private 
# Encapsulation is a concept that involves protecting and hiding an object's internal data (data members) from being accessed or modified directly from outside the class 

class ShoppingCart:

    def __init__(self,owner,discount=0):

        self.__owner_name=owner
        self.__discount_percent=discount
        self.__discount_amount=0
        self.__cart_items=[]

    def add_product(self,product, price, quantity):
        if(product.strip() != ""):
            if(price>0):
                if(quantity>0):

                    for i in self.__cart_items:
                        if i['product']==product:
                            i['quantity']+=quantity
                            return
                        
                    item={'product':product,'price':price,'quantity':quantity}
                    self.__cart_items.append(item)

                else:
                    print("Please enter valid Quantity")
            else:
                print("Please enter valid Price")
        else:
              print("Please enter valid Product name")

    def remove_product(self,product):
        for i in self.__cart_items:
            if(i['product']==product):
                self.__cart_items.remove(i)
                print(product, "removed")
                return

        print("Product not Found ")

    def update_quantity(self,product, quantity):

        if(quantity>0):

            for i in self.__cart_items:
                if(i['product']==product):
                    i['quantity']=quantity
                    print("Quantity Updated of",i['product'])
                    return
            print("Product not Found ")

        else:
            print("Please Enter a valid Quantity")



    def get_total(self):
        total=0
        for i in self.__cart_items:
            total+=i['price']*i['quantity']
        print(total)
        self.__discount_amount=(total*self.__discount_percent)/100

        print("Congrats you save", self.__discount_amount)
        print("Your final amount is ",total-self.__discount_amount)

    def get_cart_details(self):
        print(" Name: ",self.__owner_name)
        
        for i in self.__cart_items:
            print(f" {i['product']} {i['price']} {i['quantity']} = {i['price']*i['quantity']} ")
        self.get_total()
        print()
        print("***THANK YOU VISIT AGAIN ***")
        


cart = ShoppingCart("Prath", 10)

cart.add_product("MacBook", 150000, 1)
cart.add_product("Mouse", 1500, 2)
cart.add_product("Keyboard", 3000, 1)

cart.update_quantity("Mouse", 3)

cart.get_cart_details()