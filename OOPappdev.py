from datetime import datetime

class lostandfound:
    def __init__(self):
        self.items = []
        
    def genID(self):
        while True:
            ID=random.randint(100000,999999)
            if not any(item["ID"]==newID for item in self.items):
                return newID
                
    def reportItem(self,itemType:str,description:str, location:str, contact:str):
        if itemType not in("lost","found"):
            raise ValueError("itemType must be 'lost' or 'found'")
            
            desc = description.strip()
            loc = location.strip()
            cont = contact.strip()
            if not (desc and loc and cont):
                raise ValueError("Description, location and contact are required")
             
             newItem = {
                 "id": self.genID(),
                 "type": itemType,
                 "description": desc,
                 "location": loc,
                 "contact": cont,
                 "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 "status": "pending"
             }
            
    self.items.append(newItem)
    return newItem
    def search(self,query:str="")-> list:
        query = query.strip().lower()
        if not query:
            return self.items.copy()



