# A list is a data structure
# 1,2,3,4,5,6,7,8,9,10
# "Simo", "Houda", "Aya"
# 0.34, 123, 200
#  input ---> [[[[print all elements of a list]]] ----> output

l = ["Simo", "Houda", "Aya", "Ayoub"] # list of 3 strings 

# How to access "Houda" :
print(l[1])
# How to access last element :
print(l[-1])
# How to get a list's length : (length = Toul)
print("toul dyal la list houa :", len(l))
# How to change a member of the list : (member = 3oudw)
l[3] = "Abdullah" # the list becomes : ["Simo", "Houda", "Aya", "Abdullah"]
print (l[3])

#print all elements one by one
print(l[0])
print(l[1])
print(l[2])
print(l[3])

#print all elements in a loop
def print_list(l):
    print ("---------------")
    i = 0
    while (i < len(l)):
        print(l[i])
        i+=1
    print ("---------------")

print_list(l)
notes = [1.2, 10.5, 18.5]
print_list(notes)
