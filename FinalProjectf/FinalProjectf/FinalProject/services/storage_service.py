import json
from models.lost_item import LostItem
from models.found_item import FoundItem


class StorageService: #class that handles storing data in files for items
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, items): #expects a list of item objects
        with open(self.file_path, "w") as f:
            json.dump([item.to_dict() for item in items], f, indent=2) #changes each item into dictionary

    def load(self): #takes no arguments
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)

            items = [] #creates an empty list to hold item objects
            for d in data: #loops through the dictionary
                if d["type"] == "lost":
                    item = LostItem(d["id"], d["description"], d["location"], d["contact"])
                else:
                    item = FoundItem(d["id"], d["description"], d["location"], d["contact"])

                item._status = d.get("status", "pending")
                items.append(item) #if status missing, defaults back to pending

            return items

        except:
            return [] #prevents failure