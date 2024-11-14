number = int(input("Choose a number from 1-10: ")) # made input int
while number > 10 or number == 0:
    print("Input Error: Number must be a literal between 1 and 10")
    
    
while number % 2 == 0: # I state that if input is modulo 2 with 0 remainder = even
        print("Inputed number is even")
        break
else:
        print("Inputed number is odd")

# if number > 10 or number == 0:
#     print("Input Error: Number must be a literal between 1 and 10")
