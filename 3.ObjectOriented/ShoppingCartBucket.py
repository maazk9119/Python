from Task02 import ShoppingCart


class ShoppingCartBucket(ShoppingCart):

    def __init__(self):
        pass


    def Add_Item(self, Item):

        length = len(ShoppingCartBucket.Cart)
        if(length < 10):
            ShoppingCartBucket.Cart.append(Item)
        else:
            print("\t\t '----Sorry you have only purchased 10 items once----' ")



s1 = ShoppingCartBucket()
