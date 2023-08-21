"""
lab_inventory_management.py
Author: Victoria Langley
Description: This script manages the inventory of lab supplies and reagents.
"""

class LabInventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        print(f"Added {quantity} units of {item_name} to inventory.")

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                print(f"Removed {quantity} units of {item_name} from inventory.")
            else:
                print(f"Insufficient {item_name} in inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    def check_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")

if __name__ == "__main__":
    inventory_manager = LabInventory()
    
    inventory_manager.add_item("Petri dishes", 50)
    inventory_manager.add_item("Agar plates", 100)
    inventory_manager.add_item("Pipette tips", 500)
    
    inventory_manager.check_inventory()
    
    inventory_manager.remove_item("Agar plates", 30)
    inventory_manager.remove_item("Pipette tips", 200)
    
    inventory_manager.check_inventory()
