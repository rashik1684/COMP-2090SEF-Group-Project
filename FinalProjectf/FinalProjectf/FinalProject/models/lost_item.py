from models.item import BaseItem

class LostItem(BaseItem): #inherits from BaseItem

    def __init__(self, item_id, description, location, contact):
        super().__init__(item_id, description, location, contact)

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def get_location(self):
        return self._location

    def get_status(self):
        return self._status
    
    def get_date(self):
        return self._date

    def claim(self):
        self._status = "claimed"
   
    def get_type(self):
        return "lost"
    
#implementations of abstract methods