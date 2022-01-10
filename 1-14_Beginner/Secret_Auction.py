from replit import clear

def find_highest_bidder(bidders_dict):
    highest_bid = 0
    winner = ""
    for bidder in bidders_dict:
        if bidders_dict[bidder] > highest_bid:
            highest_bid = bidders_dict[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def auction():
    bidders = {}
    end = False
    while not end:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        bidders[name] = bid
        next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if next == 'no':
            end = True
            find_highest_bidder(bidders)
        elif next == 'yes':
            clear()
    # print(bidders)

def main():
    auction()

main()