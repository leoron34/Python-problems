def Fizzbuzz():
 for i in range(51):
    if i%3==0:
        print(i,"=","Fizz")
    else:
        if(i%5==0):
            print(i,"=","buzz")
        else:
            if(i%3==0 and i%5==0):
                print(i,"=","Fizzbuzz")
            else:
                print(i,"=","None")
                
Fizzbuzz()
                
