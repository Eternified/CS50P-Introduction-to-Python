def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            pass

main()