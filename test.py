def highest_bidder(x):
    name = ""
    highest = 0
    for total in x:
        if x[total]>highest:
            highest = x[total]
    return highest
print("Welcome to the blind auction!")
ans = "Y"
total_bidder = {}
while ans == "Y":
    name = input("What's your name? ").capitalize()
    bid = int(input("What's your bid amount? $"))
    total_bidder[name] = bid
    ans = input("Are there any bidder?(Y/N) ").upper()
print(highest_bidder(total_bidder))
