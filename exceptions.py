def additoin(x,y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as excep:
    print("The Type Exception :", excep.__class__)
    print("Error: The variable 'b' is not defined")
else:
    print("the operation is successful")