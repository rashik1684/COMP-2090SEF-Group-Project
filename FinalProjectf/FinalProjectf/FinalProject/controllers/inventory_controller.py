import random
from models.lost_item import LostItem
from models.found_item import FoundItem


class InventoryController:
    def __init__(self, storage_service):
        self.storage = storage_service
        self.items = []

    def load_items(self): 
        self.items = self.storage.load() #load stored data

    def save_items(self):  
        self.storage.save(self.items) 

    def add_item(self, item_type, description, location, contact):
        new_id = random.randint(100000, 999999) 

        if item_type == "lost":
            item = LostItem(new_id, description, location, contact) #method to add a new lost item
        else:
            item = FoundItem(new_id, description, location, contact) #method to add a found item

        self.items.append(item)
        self.save_items()
        return new_id

    def get_available_items(self):
        return [item for item in self.items if item.get_status() != "claimed"] #claiming an item

    def claim_item(self, item_id):
        for item in self.items:
            if item.get_id() == item_id:
                item.claim()
        self.save_items() #updating claimed items