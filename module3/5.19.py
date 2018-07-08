'''
Jesse Duncan
SDEV 220
Programming Assignment: 5.19
Due June 17, 2018
'''
num = eval(input("Enter the number of lines: "))

def as_str(i):
    s = ""
    if i <10: s = " "
    return s + str(i)

allrows = ""
for j in range(1,num+2):

    # Leading Spaces
    row = " "*3*(num-j+1)

    # Backwards
    for i in range(j-1,1,-1):
        s = as_str(i)
        row+=s + " "

    # Forward
    for i in range(1,j):
        s = as_str(i)
        row+=s + " "

    row +="\n"
    allrows +=row

print(allrows)
