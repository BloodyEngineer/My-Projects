from art_silent_auction import logo
print(f"{logo} \n Welcome to our Silent auction.")
end_auction = True
auction_dict = {}
biggest = None
while end_auction:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    auction_dict[name] = bid
    if others == "no":
        end_auction = False
for key in auction_dict:
    if biggest is None:
        biggest = auction_dict[key]
        biggest_name = key
    elif biggest < auction_dict[key]:
        biggest = auction_dict[key]
        biggest_name = key
print(f"The winner of the silent auction is {biggest_name} who bid ${biggest}")
