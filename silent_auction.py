from replit import clear
bids={}
end_of_auction=False
while end_of_auction==False:
  name=input("What's your name:- ")
  bid=int(input("What's your bid:- $"))
  bidders=input("Are there any more bidders? Type 'yes' or 'no'. :- ").lower()
  bids[name]=bid
  if bidders=="no":
    end_of_auction=True
  clear()

highest_bidder=""
highest_bid=0
for i in bids:
  bid_amount=bids[i]
  if highest_bid<bid_amount:
    highest_bid=bid_amount
    highest_bidder=i
print(f"Thw winner is {highest_bidder} with ${highest_bid}")
