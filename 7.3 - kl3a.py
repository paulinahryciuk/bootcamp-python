class Contcts:
    all_contacts = []

    def search(self,name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
            return matching_contacts


    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


    def __repr__(self):
        return f"({self.__class__.__name__} {self.name} {self.email}"

