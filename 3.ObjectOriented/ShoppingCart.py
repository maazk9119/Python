
class  ShoppingCart:
    Cart = []
    def __init(self):
        ShoppingCart.Cart = []
        print("This is the Shopping cart class")


    def Add_Item(self, Item):
        ShoppingCart.Cart.append(Item)


    def Remove_Item(self,Item):
        
        for item in ShoppingCart.Cart:
            if item == Item:
                self.Cart.remove(Item)
        
    
    def Check_Out(self):
        length = len(ShoppingCart.Cart)
        if(length ==0):
            print("Empty list")
        else:
            for items in ShoppingCart.Cart:
                print(items)


