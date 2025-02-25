class BMW:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return "25000 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return "35 km/h"

def display_car_details(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")

# Example usage
if __name__ == "__main__":
    bmw_car = BMW()
    ferrari_car = Ferrari()
    
    print("BMW Details:")
    display_car_details(bmw_car)
    
    print("\nFerrari Details:")
    display_car_details(ferrari_car)
