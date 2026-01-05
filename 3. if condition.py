#Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
else:
    print("They don't belong to the same country")