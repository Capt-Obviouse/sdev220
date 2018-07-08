'''
Jesse Duncan
SDEV 220
Programming Exercise: 15.4
Due July 8, 2018
'''

def main():
    for i in range(1, 10 + 1):
        print(m(i))

def m(i):
    if i == 1:
      return 1.0 / 3
    else:
      return m(i - 1) + i * 1.0 / (2 * i + 1)

main()
