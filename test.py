print("Welcome to the blind auction!")
ans = "Y"
total_bidder = []
while ans == "Y":
    name = input("What's your name? ")
    bid = int(input("What's your bid amount? $"))
    total_bidder.append(bid)
    ans = input("Are there any bidder?(Y/N) ").upper()
 
