#1 File handling
with open("C:/Users/User/Desktop/File1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")    
myfile.close()

#r = reading mode
#r+ =  reading + writing
#w =writing (erasing the old content and writing new)
#a = appending to the file


