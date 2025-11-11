# Problem: Car Mileage Analysis

def analyzeCarMileage(cars):
    # Handle empty list case
    if not cars:
        return {
            "averageMileage": 0,
            "highestMileageCar": None,
            "lowestMileageCar": None,
            "totalMileage": 0
        }

    total_mileage = 0
    count = 0

    # Initialize min and max with the first car
    highestMileageCar = cars[0]
    lowestMileageCar = cars[0]

    # Loop through all cars
    for car in cars:
        mileage = car["mileage"]
        total_mileage += mileage
        count += 1

        # Check highest mileage
        if mileage > highestMileageCar["mileage"]:
            highestMileageCar = car

        # Check lowest mileage
        if mileage < lowestMileageCar["mileage"]:
            lowestMileageCar = car

    # Calculate average
    if count > 0:
        average_mileage = round(total_mileage / count, 2)
    else:
        average_mileage = 0

    # Return the result as an object (Python dict)
    return {
        "averageMileage": average_mileage,
        "highestMileageCar": highestMileageCar,
        "lowestMileageCar": lowestMileageCar,
        "totalMileage": total_mileage
    }


# ==========================
# Example Test
# ==========================
cars = [
    { "make": "Toyota", "model": "Corolla", "year": 2020, "mileage": 25000 },
    { "make": "Honda", "model": "Civic", "year": 2019, "mileage": 30000 },
    { "make": "Ford", "model": "Mustang", "year": 2021, "mileage": 15000 }
]

analysis = analyzeCarMileage(cars)

print(analysis)
# Output:
# {
#   'averageMileage': 23333.33,
#   'highestMileageCar': {'make': 'Honda', 'model': 'Civic', 'year': 2019, 'mileage': 30000},
#   'lowestMileageCar': {'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'mileage': 15000},
#   'totalMileage': 70000
# }
