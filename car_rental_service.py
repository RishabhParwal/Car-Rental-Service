class Vehicle:
    vehicle_type = 'Car'

    def __init__(self, vehicle_id, make, model, year, rental_rate, availability = True):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.availability = availability
    
    def print_vehicle_details(self):
        if self.availability == True:
            print(f"Vehicle ID: {self.vehicle_id}")
            print(f"Vehicle type: {self.vehicle_type}")
            print(f"Make: {self.make}")
            print(f"Model: {self.model}")
            print(f"Year: {self.year}")
            print(f"Rental rate: {self.rental_rate}")
            print(f"Availability: {self.availability}")

            if type(self)==LuxuryVehicle:
                print(f"Sunroof: {self.sunroof}")
                print(f"Alcantara interior: {self.alcantara}")
        else:
            pass

class LuxuryVehicle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, rental_rate, availability = True, sunroof=True, alcantara=True):
        self.sunroof = sunroof
        self.alcantara = alcantara
        Vehicle.__init__(self, vehicle_id, make, model, year, rental_rate, availability = True)
        self.rental_rate = int(self.rental_rate*1.2)
            
Vehicles = []
Vehicles.append(Vehicle(1, "Honda", "Civic", 2021, 5000, True))
Vehicles.append(LuxuryVehicle(2, "Skoda", "Superb", 2023, 8000, True))

Customers = []



class Customer():
    def __init__(self, customer_id, name, contact_info, rental_history = []):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = rental_history

    def input_customer_details():
        if input("Are you an existing customer (y/n): ")=="y": existing = True
        else: existing = False
        customer_id = -1
        if existing:
            existing_id = input("Please enter your ID: ")
            for x in Customers:
                if x.customer_id == existing_id:
                    customer_id = x.customer_id
                    return customer_id
            if customer_id <0:
                print("You are not an existing customer. Proceed to create your ID.")
                print("")
        customer_id = len(Customers)+1
        name = input("Please enter your name: ")
        contact_info = int(input("Please enter your mobile number: "))
        print(f"Your customer ID is: {customer_id}")
        print("")
        rental_history = []
        Customers.append(Customer(customer_id, name, contact_info, rental_history))
        return customer_id

    def print_customer_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Mobile number: {self.contact_info}")

    class rental_info():
        def __init__(self, vehicle_id, rent_duration, returned = False):
            self.vehicle_id = vehicle_id
            self.rent_duration = rent_duration
            self.returned = returned

    def print_rental_history(self):
        i=1
        for x in self.rental_history:
            print(f"{i} Vehicle ID: {x.vehicle_id}, Duration: {x.rent_duration} days, Returned: {x.returned}")
            i+=1



def rent_vehicle(Customer):
    id = int(input("Enter the vehicle ID of the vehicle you want to rent: "))
    if id <= len(Vehicles):
        rent_duration = int(input("Enter the number of days you want to rent the vehicle for: "))
        current_vehicle = Vehicles[id-1]
        if current_vehicle.availability == True:
            print(f"Vehicle avilable. Total cost for {rent_duration} days will be: {current_vehicle.rental_rate*rent_duration}")
            current_vehicle.availability = False
            Customer.rental_history.append(Customer.rental_info(current_vehicle.vehicle_id, rent_duration, False))
        else:
            print("The chosen vehicle is not available at the moment. Please choose another vehicle.")
            rent_vehicle(Customer)
        print("")
    else: 
        print("Enter a valid Vehicle ID.")
        print("")
        rent_vehicle(Customer)


def return_vehicle(Customer):
    rent_ID = int(input("Enter the vehicle ID of the vehicle you want to return: "))
    for x in Customer.rental_history:
        if rent_ID == x.vehicle_id:
            if rent_ID <= len(Vehicles):
                current_vehicle = Vehicles[rent_ID-1]
                if current_vehicle.availability == False:
                    print(f"Thanks for returning the vehicle")
                    current_vehicle.availability = True
                for x in Customer.rental_history:
                    if x.vehicle_id == rent_ID:
                        x.returned = True
                print("")
                return
    
    print("You have not rented this Vehicle.")
    print("")

def print_vehicles():
    for x in Vehicles:
        Vehicle.print_vehicle_details(x)
        print("")


# ASK user number of filters, name of filters one by one, sort by, make filters as a list of filters, even when only one filter given
def filter_vehicles(Vehicles: list, filters: list, sort_by = "rental_rate"): # by default sort by rental rate if user doesnt specify
    # function directly prints to console, directly call fn with given arguments in main program
    found = [] 
    f = filters.pop(0)
    if f == "vehicle_id":
            vid = int(input("Enter vehicle id: "))
            for vehicle in Vehicles:
                if vehicle.vehicle_id == vid:
                    found.append(vehicle)
    elif f == "make":
            m = input("Enter make: ")
            for vehicle in Vehicles:
                if vehicle.make == m:
                    found.append(vehicle)
    elif f == "model":
            m = input("Enter make: ")
            for vehicle in Vehicles:
                if vehicle.make == m:
                    found.append(vehicle)
    elif f == "rental_rate":
            m = input("Enter rental rate: ")
            for vehicle in Vehicles:
                if vehicle.rental_rate == m:
                    found.append(vehicle)
    elif f == "year":
            m = input("Enter year: ")
            for vehicle in Vehicles:
                if vehicle.year == m:
                    found.append(vehicle)
    elif f == "availability":
            for vehicle in Vehicles:
                if vehicle.availability:
                    found.append(vehicle)
    if filters:
        return filter_vehicles(found, filters, sort_by)
    if not Vehicles:
        print("No such vehicles found.")
    if sort_by == "rental_rate":
        filters.sort(key = lambda v: v.rental_rate)
    elif sort_by == "year":
        filters.sort(key=lambda v: v.year)
    elif sort_by == "make":
        filters.sort(key = lambda v: v.make)
    elif sort_by == "model":
        filters.sort(key = lambda v: v.model)
    elif sort_by == "vehicle_id":
        filters.sort(key = lambda v: v.vehicle_id)
    elif sort_by == "availability":
        filters.sort(key = lambda v: v.availability)
    else:
        print("Not a valid sorting criteria.")
    for v in found:
        v.print_vehicle_details()
        print("")
    
class RentalManager():
    print("")
    print("*"*100)
    print("")
    print("Welcome to Car rental service.")
    print("")
    cus_id = Customer.input_customer_details()
    def __init__(self, Vehicles=[], Customers = []):
        self.Vehicles = Vehicles
        self.Customers = Customers

    for x in Customers:
        if cus_id == x.customer_id:
            current_customer = x
            break

    def add_vehicles():
        while True:
            user_input = input("Press N to enter new vehicle to list: ")
            if user_input == "N":
                vehicle_id = input("Vehicle ID: ")
                vehicle_type = input("Vehicle type: ")
                make = input("Make: ")
                model = input("Model: ")
                year = input("Year: ")
                rental_rate = int(input("Rental rate: "))
                luxury = (input("Luxary: "))
                if luxury == "Yes":
                    Vehicles.append(LuxuryVehicle(vehicle_id, make, model, year, rental_rate, True, True, True))
                else:
                    Vehicles.append(Vehicle(vehicle_id, make, model, year, rental_rate, True))
            else: 
                break

    def remove_vehicles():
        user_input = input("Enter ID of vehicle to be removed: ")
        for x in Vehicles:
            if x.vehicle_id == user_input:
                Vehicles.remove(x)

    def generate_rental_report():
        print("")
        for x in Customers:
            print(f"Customer ID: {x.customer_id}, Customer Name: {x.name}")
            Customer.print_rental_history(x)
            print("")

    while(True):
        user_input = input("Please enter R for rent, Re for return, V for list of Vehicles, F to filter Vehicles, Q for quit, L for logout: ")
        if user_input == "R": rent_vehicle(current_customer)
        elif user_input == "Re": return_vehicle(current_customer)
        elif user_input == "V": print_vehicles()
        elif user_input == "F": 
            print(f"Available filters are: ")
            print("vehicle_Id, make, model, rental_rate, year, availability")
            filters = int(input("How many filters do you want to apply: "))
            f_arr = []
            for f in range(filters):
                fin = input(f"Enter filter {f + 1}: ")
                f_arr.append(fin)
            print("Available sorting criteria are: ")
            print("vehicle_id, make, model, rental_rate, year, availability")
            sby = input("Enter sorting criteria: ")
            filter_vehicles(Vehicles, f_arr, sby)
        elif user_input == "A": add_vehicles()
        elif user_input == "D": remove_vehicles()
        elif user_input == "G": generate_rental_report()
        elif user_input == "L": 
            print("Please login again or create a new ID.")
            cus_id = Customer.input_customer_details()
            for x in Customers:
                if cus_id == x.customer_id:
                    current_customer = x
                    break
        elif user_input == "Q": break


RentalManager(Vehicles, Customers)