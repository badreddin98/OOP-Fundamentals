# Task 1: Vehicle Registration System

class Vehicle:
        def __init__(self, reg_num, vehicle_type, owner):
            self.registration_number = reg_num
            self.type = vehicle_type
            self.owner = owner
        
        def update_owner(self, new_owner):
            self.owner = new_owner
            print(f"Owner updated to {self.owner} for vehicle {self.registration_number}")
            
vehicle1 = Vehicle("ABC123", "BMW", "Bader yazi")
vehicle2 = Vehicle("ABM234", "Hyun", "Khal yazi")
        
print(f"Vehicle 1: Reg#: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: Reg#: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

vehicle1.update_owner("Moh yazi")
vehicle2.update_owner("taha yazi")

print(f"Vehicle 1: Reg#: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: Reg#: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
