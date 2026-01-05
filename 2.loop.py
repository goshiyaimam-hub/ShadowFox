#Imagine you are doing a workout routine, and you have to complete 100
#jumping jacks.
#Write a program that:
#Asks you to perform 10 jumping jacks at a time.
#After each set, it asks, "Are you tired?"

total_jumps = 0
target = 100

while total_jumps < target:
    total_jumps += 10
    print("You completed", total_jumps, "jumping jacks")

    if total_jumps == target:
        print("Congratulations! You completed all 100 jumping jacks!")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of", total_jumps, "jumping jacks.")
            break
    else:
        remaining = target - total_jumps
        print(remaining, "jumping jacks remaining")