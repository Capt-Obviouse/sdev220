'''
Jesse Duncan
SDEV 220
Programming Exercise: 5.4
Due June 17, 2018
'''
print("{0:<15s}{1:>10s}".format("Miles", "Kilometers"))
print("\n")

miles = 1
while miles <= 10:
    print("{0:<15d}{1:<10.3f}".format(miles, miles * 1.609))
    miles += 1
