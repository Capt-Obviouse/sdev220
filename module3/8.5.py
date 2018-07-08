'''
Jesse Duncan
SDEV 220
Programming Assignment: 8.5
Due June 17, 2018
'''

def count(s1, s2):
    count = s1.count(s2)
    return count


s1 = input("Please enter a string: ")
s2 = input("Please enter a second string: ")
s1 = s1.lower()
s2 = s2.lower()

print(count(s1, s2))
