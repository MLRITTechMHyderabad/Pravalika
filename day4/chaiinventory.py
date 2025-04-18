from abc import ABC,abstractmethod
class Chai(ABC):
    def __init__(self,name,base_price,quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock
    @abstractmethod 
    def calculate_price(self):
        pass
    @abstractmethod
    def display_info(self):
        pass
class MasalaChai(Chai):
    def calculate_price(self):
        return self.base_price+10
    def display_info(self):
        print(f"name: {self.name} | price per cup: {self.calculate_price()} | stock: {self.quantity_in_stock}")
    
class GingerChai(Chai):
    def calculate_price(self):
        return self.base_price+8
    def display_info(self):
        print(f"name: {self.name} | price per cup: {self.calculate_price()} | stock: {self.quantity_in_stock}")
    
class ElaichiChai(Chai):
    def calculate_price(self):
        return self.base_price+12
    def display_info(self):
        print(f"name: {self.name} | price per cup: {self.calculate_price()} | stock: {self.quantity_in_stock}")
    
class ChaiInventory():
    def __init__(self):
        self.chailist=[]
    def add_chai(self,chai_obj):
        self.chailist.append(chai_obj)
    def show_inventory(self):
        for chai in self.chailist:
            chai.display_info()
    def get_total_inventory_value(self):
        total_value = 0
        for chai in self.chailist:
            total_value += chai.calculate_price() * chai.quantity_in_stock
        return total_value
                
if __name__ == "__main__":
    inventory=ChaiInventory()
    c1=MasalaChai("masala chai", 20,50)
    c2=GingerChai("Ginger chai", 18,40)
    c3=ElaichiChai("Elaichi chai", 25,30)
    inventory.add_chai(c1)
    inventory.add_chai(c2)
    inventory.add_chai(c3)
    inventory.show_inventory()
    print("Total Inventory value: ",inventory.get_total_inventory_value())
        
            
    
