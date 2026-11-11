class  ShoppingCart:
    def __init__(self):
        self.__cart_items=[]

    def add_items(self,product,price,quantity):
        d={'product':product,'price':price,'quantity':quantity}
        self.__cart_items.append(d)

    def get_cart_details(self):
#        return self.__cart_items  use self.__cart_items.copy() so the original list will not clear
        return self.__cart_items.copy()

cart = ShoppingCart()

cart.add_items("Mouse", 1500, 2)

items = cart.get_cart_details()
print(items)

items.clear()

items = cart.get_cart_details()
print(items) 

# learnings
# When you don't want external code or a function to modify your original mutable data, pass a copy instead of sharing the original object.
# here -get_cart_details returns original data  [return self.__cart_items] instead do this - return self.__cart_items.cpy()