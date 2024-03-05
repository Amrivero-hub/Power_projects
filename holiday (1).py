#Task 14

#Your task will be to calculate an user’s total holiday cost, which includes the plane cost, hotel cost, and car-rental cost.

# Get the user inputs for the city, the number of nights, and the number of rental days
city_flight = input("Which city will you be flying to? (Choose from: London,Paris,New York,Tokyo):")
num_nights = int(input("How many nights will you be staying at a hotel?"))
rental_days = int(input("How many days will you be hiring a car?"))

#Define some constants for the flight costs and the hotel and car rental rates
flight_cost = {"London": 200, "Paris": 150, "New York": 300, "Tokyo": 400}
hotel_rate = 100 # per night
car_rental_rate = 50 # per day

# Create a function that takes num_nights as an argument and returns the hotel cost
def hotel_cost(num_nights):
  return num_nights * hotel_rate

# Create a function that takes city_flight as an argument and returns the plane cost
def plane_cost(city_flight):
  # Use if/else if statements to check the city and return the corresponding cost
  # Check if the city is valid; if not, return 0
  if city_flight in flight_cost:
    return flight_cost[city_flight]
  else:
    print("Invalid city. Please choose from:London, Paris, New York, Tokyo.")
    return 0
  
# Create a function that takes rental_days as an argument and returns the car rental cost
def car_rental(rental_days):
  return rental_days * car_rental_rate

# Create a function that takes the three arguments hotel_cost, plane_cost, car_rental
# and returns the total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
  # Call the three functions with the respective arguments and add them up
  return hotel_cost + plane_cost + car_rental

# Print out the details and the total cost of the holiday
print(f"You are flying to {city_flight} for {num_nights} nights.")
print(f"You are renting a car for {rental_days} days.")
print(f"The total cost of your holiday is {holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))} dollars.")