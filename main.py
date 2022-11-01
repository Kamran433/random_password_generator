# import random
# import RPD_letters
# import RPD_numbers
# import RPD_symbols
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# password=[]
# passwords=""
# for letter in range(1,nr_letters+1):
#   c=random.choice(RPD_letters.letters)
#   password+=c
# for symbol in range(1,nr_symbols+1):
#   b=random.choice(RPD_symbols.symbols)
#   password+=b
# for number in range(1,nr_numbers+1):
#   a=random.choice(RPD_numbers.numbers)
#   password+=a
# random.shuffle(password)
# for m in password:
#   passwords+=m
# print(f"Your password is:\n{passwords}")
