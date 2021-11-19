#Player's initial hand
card1 = random.choices(cards,k=1)
player_hand.append(card1)
val_1= values[cards.index(card1[0],0)]
cards.remove(card1[0])
values.remove(val_1)

card2 = random.choices(cards,k=1)
player_hand.append(card2)
val_2 = values[cards.index(card2[0])]
cards.remove(card2[0])
values.remove(val_2)

player_hand_val = val_1 + val_2

#Dealer's initial hand

card1 = random.choices(cards,k=1)
dealer_hand.append(card1)
val_1 = values[cards.index(card1[0],0)]
cards.remove(card1[0])
values.remove(val_1)

card2 = random.choices(cards,k=1)
dealer_hand.append(card2)
val_2 = values[cards.index(card2[0],0)]
cards.remove(card2[0])
values.remove(val_2)

dealer_hand_val = val_2
hidden_dealer_hand_val = val_1 + val_2

while(True):
    if(player_hand_val > 21):
        print("\nBust!")
        print("Computer wins!")
        restart = input("\nPlay again? (yes or no)")
        if(restart.lower() == "yes"):
            break
        elif(restart.lower() == "no"):
            quit()
    else:
        continue
    hitORstand = input("(h)it or (s)tand? ")
    if(hitORstand.lower() == "h"):
            
        player_hand.append(deal())
        val = card_value(player_hand[len(player_hand)-1])
                             
        player_hand_val += val
            
        print("\nPlayer drew a " + card + " worth " + val_1)
        print("\nPlayer's new value is ", player_hand_val)
        continue
    elif(hitORstand.lower() == "s"):
        print("\nDealer flips their hidden card...\n")
        print("******* DEALER'S HAND *******")
        print("-----------------------------")
        print("Card 1: ",dealer_hand[0],"\nCard 2: ",dealer_hand[1],"\nValue: ",dealer_hand_val)

        print("\n******* PLAYERS'S HAND *******")
        print("------------------------------")
        #print(
        #print("Card 1: ",player_hand[0],"\nCard 2: ",player_hand[1],"\nValue: ",player_hand_val)
    else:
        print("Invalid entry, try again")
        continue



#Counts the amount of cards in the player's hand to print accurately after "standing"
#def cardcounter(array):
    
