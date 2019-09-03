#       A program takes user name that is already hardcoded then ask to continoue
#       the program or quit it, after continoue the program it takes table no to the
#       user then print it but if there is VALUEERROR then it alert then take input
#       again.  KEYS in use(function,lowercase,loops,input,error handling)

def tableno(a):
        for i in range(1,10):
                print(f"{a} * {i} = {i*a}")

name = str(input("Enter Name:\t"))
if name.lower() == "boss":
        a = ()
        try:
              while a != "q":
                print("\n")
                a = str(input("Enter to continou / Q to Quit:\t"))
                print("\n")
                if a != "q":    # it will quit program in lowercase 'q' only
                        table = int(input("Enter Table no:\t"))
                        print("\n")
                        tableno(table)
        except ValueError:
                print("///Input table in numbers")
                errortable = int(input("Enter Table no:\t"))
                tableno(errortable)  
                                     
else:
        print("Sorry, You are not my boss")
