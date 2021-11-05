frst = "@"
scnd = "."
def is_it_valid(a):
    if frst and scnd in a:
        return True

x = input("Enter your email: ")
if is_it_valid(x):
    print("Valid Email.")
else:
    print("Invalid Email.")





