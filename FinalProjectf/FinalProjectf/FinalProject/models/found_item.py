from models.item import BaseItem

class FoundItem(BaseItem): #inherits from BaseItem

    def __init__(self, item_id, description, location, contact): #defines constructor with 4 parameters
        super().__init__(item_id, description, location, contact)

    def get_id(self):
        return self._id #uses encapsulation for getter method

    def get_description(self):
        return self._description

    def get_location(self):
        return self._location

    def get_status(self):
        return self._status
    
    def get_date(self):
        return self._date

    def claim(self):
        self._status = "claimed" #changes the items status

    def get_type(self):
        return "found" #updates and reports the type of an item
