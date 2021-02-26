# ///PATRICK KURTH 1592681/// #

from ContactDump import ContactDump
from SQLConnect import SqlConnector
from datetime import date

# ///Make a menu///
# ///Have menu options with input///
# ///Options will use methods from ContactDump///#


class UserMenu:
    
    def __init__(self):
        s = SqlConnector("db-cis3368.cszpibyejcfq.us-east-2.rds.amazonaws.com", "admin", "Water123cool456", "testcis3368")
        self.cd = ContactDump(s)

    def menu(self):
 
        print ("""              [a] - Add contact
              [d] - Remove contact
              [u] - Update contact details
              [b] - Ouput all contacts in alphabetical order
              [c] - Output all contacts by creation date
              [o] - Output all contacts
              [q] - Quit""")



    def runmenu(self):

    
        menuchug = True

        while menuchug == True:
            
            self.menu()
        
            option = input("Enter your option: ")

            if option == "a":
                today = date.today()
                name = input("Contact Name: ")
                self.cd.createcontact(name, today)

            elif option == "d":
                name = input("Enter Contact Name to Delete: ")
                self.cd.deletecontact(name)

            elif option == "u":
                oldname = input("Enter Contact Name to Update: ")
                updatedname = input("Enter New Contact Name: ")
                self.cd.updatecontact(updatedname, oldname)

            elif option == "b":
                output = self.cd.alphabetizecontacts()
                print(output)

            elif option == "c":
                output = self.cd.creationdatecontacts()
                print(output)
        
            elif option == "o":
                output = self.cd.getcontacts()
                print(output)
    
            elif option == "q":
                menuchug = False
    
            else:
                print("Invalid option.")