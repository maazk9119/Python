from Calculator import Calculator
from ShoppingCart import ShoppingCart
from ShoppingCartBucket import ShoppingCartBucket

#Task 01:
c1 = Calculator()
ans1 = c1.Addition(1,2)
ans2 = c1.Subtraction(5,3)
ans3 = c1.Multiplication(5,5)
ans4 = c1.Division(12,4)
print("After execution of addtion function the answer is:", ans1)
print("After execution of subtraction function the answer is:", ans2)
print("After execution of multiplication function the answer is:", ans3)
print("After execution of Division function the answer is:", ans4)


#Task 02:
x = ShoppingCart()
x.Add_Item("shirt")
x.Add_Item("pent")
x.Add_Item("tie")
x.Remove_Item("pent")
x.Check_Out()

#Task 03:
x = ShoppingCartBucket()

x.Add_Item("shirt1")
x.Add_Item("shirt2")
x.Add_Item("shirt3")
x.Remove_Item("shirt1")
x.Check_Out()