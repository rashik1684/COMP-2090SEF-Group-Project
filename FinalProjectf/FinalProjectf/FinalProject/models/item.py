from datetime import datetime
from abc import ABC, abstractmethod


class BaseItem(ABC): # abstract base class that inherits from ABC
    def __init__(self, item_id, description, location, contact): #Defines constructor for BaseItem
        self._id = item_id
        self._description = description # stores item's description
        self._location = location
        self._contact = contact
        self._date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #sets current date and time for object
        self._status = "pending" #sets initial status to show that its not claimed
    
    @abstractmethod
    def get_id(self): 
        ...

    @abstractmethod
    def get_description(self):
        ...

    @abstractmethod
    def get_location(self):
        ...

    @abstractmethod
    def get_status(self):
        ...
    
    @abstractmethod
    def get_date(self):
        ...

    @abstractmethod
    def claim(self):
        ...

    @abstractmethod
    def get_type(self):
        return "base" # placeholder
    
#all abstract methods declared

    def to_dict(self): #non-abstract method
        return {
            "id": self._id,
            "description": self._description,
            "location": self._location,
            "contact": self._contact,
            "date": self._date,
            "status": self._status,
            "type": self.get_type()
        } 
    #returns a dictionary of item