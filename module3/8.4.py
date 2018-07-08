'''
Jesse Duncan
SDEV 220
Programming Exercise: 8.4
Due June 17, 2018
'''
def main():
    s = input("Enter a string: ").strip()
    ch = input("Enter a character: ").strip()

    print(count(s, ch))

def count(s, ch):
    count = 0
    for c in s:
        if ch == c:
            count += 1

    return count

main()
