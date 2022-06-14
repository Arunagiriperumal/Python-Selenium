file = open("Test.txt")
#read file, it is more like a generator it starts reading a line from where the previous command ends.
#print(file.read(1))
#print(file.read(1))
#print(file.readline())

#this read.lines command create a list and make every line of the file a list element.
line = file.readlines()
file.close()


""" this way of opening a file will create an object named 'file', once the conditon on the object is over it will close the object
 so we do not want to close the file explicitly """
with open("Test.txt", "r") as file:

