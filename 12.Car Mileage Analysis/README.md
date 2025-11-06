# Problem: Car Mileage Analysis

## Instructions
You are given an array of car objects, each containing information about a car's make, model, year, and mileage. Your goal is to perform some analysis on the car mileage data using high order array methods.
Implement a function called analyzeCarMileage which takes in an array of car objects and performs the following tasks:
1.	Calculate the average mileage of all cars.
2.	Find the car with the highest mileage.
3.	Find the car with the lowest mileage.
4.	Calculate the total mileage of all cars combined.
The function should return an object containing the calculated values as properties.
Here is an object that you can use to test your function in the run file:
```
const cars = [
  { make: 'Toyota', model: 'Camry', year: 2020, mileage: 30800 },
  { make: 'Honda', model: 'Civic', year: 2019, mileage: 32000 },
  { make: 'Chevrolet', model: 'Impala', year: 2021, mileage: 17500 },
  { make: 'Audi', model: 'R8', year: 2020, mileage: 13000 },
  { make: 'Tesla', model: 'Model 3', year: 2018, mileage: 50000 },
];
```

## Examples
```
const cars = [
  { make: 'Toyota', model: 'Corolla', year: 2020, mileage: 25000 },
  { make: 'Honda', model: 'Civic', year: 2019, mileage: 30000 },
  { make: 'Ford', model: 'Mustang', year: 2021, mileage: 15000 },
];

const analysis = analyzeCarMileage(cars);
console.log(analysis);
// Output:
// {
//   averageMileage: 23333.33,
//   highestMileageCar: { make: "Honda", model: "Civic", year: 2019, mileage: 30000 },
//   lowestMileageCar: { make: "Ford", model: "Mustang", year: 2021, mileage: 15000 },
//   totalMileage: 70000
// }

```

## Constraints
•	The input array cars will contain at most 100 car objects.
•	Each car object's mileage property will be a positive integer.
•	Result should be rounded to 2 decimal places.
