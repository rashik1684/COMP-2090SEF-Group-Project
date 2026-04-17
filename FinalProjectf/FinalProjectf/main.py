from services.storage_service import StorageService
from controllers.inventory_controller import InventoryController
from ui.main_window import MainWindow

def main(): #puts all code together (service, storage, controller and UI)
    storage = StorageService("data.json")
    controller = InventoryController(storage)

    controller.load_items()

    app = MainWindow(controller) #window can call methods from controller
    app.run()

if __name__ == "__main__": #makes sure code is running independently
    main() #starts app