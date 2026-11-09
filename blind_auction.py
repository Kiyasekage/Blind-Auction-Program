def highest_bidder(x):
    highest = 0
    name = ""
    for names in x:
        if x[names]>highest:
            highest = x[names]
            name = names
    print(f"The winner is {name} with a bid of {highest}")
    
print("Welcome to the blind auction!")
ans = "Y"
total_bidder = {}
while ans == "Y":
    name = input("What's your name? ").capitalize()
    bid = int(input("What's your bid amount? $"))
    total_bidder[name] = bid
    ans = input("Are there any bidder?(Y/N) ").upper()


highest_bidder(total_bidder)

