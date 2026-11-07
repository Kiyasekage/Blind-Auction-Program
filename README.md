# Blind Auction Program

A simple Python blind auction simulation where multiple participants can submit their bids without seeing other participants' offers. The program stores each bidder's name and bid amount in a dictionary, then uses a custom function to identify the winner with the highest bid.

## Features

- **Blind Bidding:** Allows multiple participants to submit their bids.
- **Bidder Registration:** Collects each participant's name and bid amount.
- **Dynamic Data Storage:** Stores bidder information in a dictionary.
- **Highest Bid Detection:** Uses a custom function to compare bid amounts and determine the winner.
- **Interactive Input:** Allows users to continue submitting bids until no more participants remain.
- **Winner Announcement:** Displays the winning bidder's name and highest bid amount.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the code in a file named `blind_auction.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python blind_auction.py
   ```

5. Enter each participant's name and bid amount.
6. Enter `Y` to allow another participant to bid or `N` to finish the auction.
7. The program will announce the highest bidder.

## Example

**Example Input:**

```text
Welcome to the blind auction!

What's your name? John
What's your bid amount? $150
Are there any bidder? (Y/N) Y

What's your name? Alice
What's your bid amount? $250
Are there any bidder? (Y/N) Y

What's your name? Michael
What's your bid amount? $200
Are there any bidder? (Y/N) N
```

**Output:**

```text
The winner is Alice with a bid of 250
```

## Concepts Practiced

- **Dictionaries:** Storing bidder names and their corresponding bid amounts.
- **Functions:** Creating `highest_bidder()` to determine the auction winner.
- **For Loops:** Iterating through dictionary keys to compare bid amounts.
- **While Loops:** Repeatedly collecting bids until participants finish.
- **Conditional Statements:** Comparing bids to identify the highest value.
- **String Methods:** Using `.capitalize()` and `.upper()` to standardize user input.
- **Formatted Strings:** Displaying the winner's information using an f-string.

## Language

Python 3
