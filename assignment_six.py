import random
def get_birthdays():
    list_one = []
    for x in range(23):
        r = random.randint(1, 365)
        list_one.append(r)
    return list_one
def is_duplicates(list_one):
    for x in range(22):
        for y in range(x+1, 23):
            if list_one[x] == list_one[y]:
                return True
    return False
def main():
    runs = input("How many times would you like to simulate this problem?")
    duplicate = 0
    for x in range(int(runs)):
        birthdays = get_birthdays()
        if is_duplicates(birthdays):
            duplicate = duplicate + 1
    print(duplicate, "times there were two of the same birthday. This is about", duplicate/int(runs), "percent of the time.")
if __name__ == '__main__':
    main()