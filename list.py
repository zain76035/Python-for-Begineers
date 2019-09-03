# A program that has list hardcoded then check your name in the list, where its locate

l = ["he","she","it","they","we","our"]
r = 1
name = str(input("Name:\t"))
for i in l:
        if name == i:
                print(f"{r}: {i}")
                break
        elif name != i:
                print(f"{r}: None")
                r += 1
       
