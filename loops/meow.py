def main():
    num = get_number()
    meow(num)

def get_number():
    while True:
        num = int(input("What is your number? "))
        if num > 0:
            break
    return num

def meow(n):
    for _ in range(n):
        print("Meow!")

main()
