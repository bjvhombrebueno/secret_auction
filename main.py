import art
import os
from time import sleep
print("Secret Auction")
#sleep(5)
os.system('cls')
bids = {}
more = 'y'
while more == 'y':
    name = input("Name ")
    bid = int(input("Bid "))
    bids[name] = bid
    more = input("Any more bidders? ").lower()
    if more == 'y':
        os.system('cls')
        continue
    else:
        break

winning_bid = max(bids.values())

for key in bids:
    find_winner = key
    find_winning_bid = bids[key]
    if find_winning_bid == winning_bid:
        os.system('cls')
        print(f"Winner is {find_winner}")
        break



