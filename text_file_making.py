i = ()
while i != 'q':
        try:    
                i = ()
                while i != "q":
                        i = input("Enter to continue or Q to Quit\t")
                        if i != "q":
                                option = int(input('\n1: Create File\n2: Append File\n3: Read File\n4: Add new content\n\n\n--------'))
                                
                                if option == 1:
                                        filename = input("Enter File name:\t")
                                        with open(f'{filename}', 'w') as f:
                                                print("File has successfully created:")
                                                writefile = input("Write text to add or C to Close file:\t")
                                                if writefile != "c":
                                                        f.write(writefile)
                                if option == 2:
                                        opfile = input('Enter file name to open:\t')
                                        apend = input("Enter text:\t")
                                        with open(f'{opfile}', 'a') as a:
                                                a.write(apend)
                                                print('Text has successfully updated:')
                                
                                if option == 3:
                                        openfile = input("Enter file name to open:\t")
                                        with open(f'{openfile}' , 'r') as r:
                                                readcontent = r.read()
                                                print(readcontent)                  
                                if option == 4:
                                        writename = input("Enter file name:\t")
                                        with open(f'{writename}','w') as w:
                                                newcontent = input('New Content:\t')
                                                w.write(newcontent)
                                                print("New content added Successfully:")

        except FileNotFoundError:
                print(">>>Please Enter file name with extension")
