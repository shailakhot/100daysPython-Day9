import art

def compare_bid(auction_bid):
    highest_bid = 0
    winner = ""
    for bidder in auction_bid:
       bidamt = auction_bid[bidder]
       if bidamt > highest_bid:
            highest_bid = bidamt
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")



print(art.logo)
print("Welcome to secret auction program")
do_continue = True
auction_bid = {}

while do_continue:
  #TODO ask the user for inputs and save inputs in dictionary
   name =input("What is your name? ")
   bid_value = int(input("What is your bid? $"))
   auction_bid[name] = bid_value
   print(auction_bid)

  #TODO add new bids if there are more ppl demands
   repeat = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
   if repeat == 'yes':
       print("\n"* 20)
   elif repeat == 'no':
       do_continue = False
       # TODO getting a key with maximum value in dictionary
       compare_bid(auction_bid)


