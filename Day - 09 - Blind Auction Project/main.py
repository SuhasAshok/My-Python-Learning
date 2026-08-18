# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The highest bidder is {winner} with a bid of ${highest_bid}")

blind_auction =  {}

should_continue = True

while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    blind_auction[name] = bid
    continue_auction = input("Are there any other bidders type 'yes' or 'no': ").lower()

    if continue_auction == "no":
        should_continue = False
        find_highest_bidder(blind_auction)

    elif continue_auction == "yes":
        print("\n" * 100)
