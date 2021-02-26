# ///PATRICK KURTH 1592681/// #

# ///class ContactDump/// #
# ///methods for organizing and updating/// #

class ContactDump:

    def __init__ (self, sqlconnector):
        self.sqlconnector = sqlconnector

    
    def getcontacts(self):
        records = self.sqlconnector.execute_read_query("SELECT * FROM contacts")
        result = []
        
        for record in records:
            result.append(record[1])
        
        return result

    def alphabetizecontacts(self):
        records = self.sqlconnector.execute_read_query("SELECT * FROM contacts ORDER BY contactDetails ASC")
        result = []

        for record in records:
            result.append(record[1])
        
        return result

    def creationdatecontacts(self):
        records = self.sqlconnector.execute_read_query("SELECT * FROM contacts ORDER BY creationDate ASC")
        result = []

        for record in records:
            result.append(record[1])

        return result

    def createcontact(self, name, date):
        self.sqlconnector.execute_query(f'INSERT INTO contacts (contactDetails, creationDate) VALUES ("{name}", "{date}")')

    def deletecontact(self, name):
        self.sqlconnector.execute_query(f'DELETE FROM contacts WHERE contactDetails = "{name}"')

    def updatecontact(self, updatedname, oldname):
        self.sqlconnector.execute_query(f'UPDATE contacts SET contactDetails = "{updatedname}" WHERE contactDetails = "{oldname}"')
