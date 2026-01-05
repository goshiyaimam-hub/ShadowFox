#You have a list of superheroes representing the Justice League. justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Initial Justice League:", justice_league)

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3.Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

# 4. Separate Aquaman and Flash
# Move Superman between Aquaman and Flash
justice_league.remove("Superman")

flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")

print("After separating Aquaman and Flash:", justice_league)

# 5. Replace with new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("After Superman forms new team:", justice_league)

#Sort alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)

print("New leader (0th index):", justice_league[0])