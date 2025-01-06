
# try:
#     x = int(input("What's x?"))
   
# except ValueError:
#     print("X is not an integer")
# else:
#      print(f"x is {x}") 
     

# print("Hello world")
# I am robot I dont have feelings

def main():

    x = get_int("what's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:
            pass
        


main()