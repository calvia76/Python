import random
import time
#Function that picks a card at random, evaluates its value, then deletes card 
#and value instances from its respective list
#Returns card name and value
def deal():
    
    card = random.choices(cards,k=1)
    val = values[cards.index(card[0],0)]
    del values[cards.index(card[0])]
    cards.remove(card[0])
    return card, val

def restart():
    while(True):
        restart = input("\nWould you like to play again? (yes or no) ")
        if(restart.lower() == "yes"):
            return True
        elif(restart.lower()=="no"):
            quit()
        else:
            print("Invalid entry: try again.")
        
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts','6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts','2 of Hearts','Ace of Hearts',
          'King of Hearts','Queen of Hearts', 'Jack of Hearts', '10 of Diamonds','9 of Diamonds', '8 of Diamonds', '7 of Diamonds','6 of Diamonds', '5 of Diamonds',
          '4 of Diamonds','3 of Diamonds', '2 of Diamonds','Ace of Diamonds',
          'King of Diamonds','Queen of Diamonds', 'Jack of Diamonds','10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs',
          '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs','2 of Clubs', 'Ace of Clubs',
          'King of Clubs','Queen of Clubs','Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades','7 of Spades',
          '6 of Spades','5 of Spades', '4 of Spades','3 of Spades', '2 of Spades', 'Ace of Spades',
          'King of Spades','Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
          10, 10, 10]

player_hand = []
dealer_hand = []

player_hand_val = 0
dealer_hand_val = 0

#card(name,value)
flag1 = True
while(flag1):
    print("\nPlease wait, the dealer is shuffling the cards...\n")

    time.sleep(2)

    #First card dealt to PLAYER
    card1 = deal()
    player_hand.append(card1[0])
    pval = card1[1]

    #Second card dealt to DEALER, card and value are hidden
    card2 = deal()
    dealer_hand.append(card2[0])
    hidden_val = card2[1]


    #Third card dealt to PLAYER
    card3 = deal()
    player_hand.append(card3[0])
    player_hand_val = card3[1] + pval

    #Fourth card dealt to DEALER
    card4 = deal()
    dealer_hand.append(card4[0])
    dealer_hand_val = card4[1]
    hidden_dealer_hand_val = hidden_val + dealer_hand_val

    print("\nPlease wait, the dealer is dealing the cards...\n")
    time.sleep(1)
    print("******* DEALER'S HAND *******")
    print("-----------------------------")
    print("Card 1:  Hidden\nCard 2: ",dealer_hand[1],"\nValue: ",dealer_hand_val)
                             
    print("\n******* PLAYERS'S HAND *******")
    print("------------------------------")
    print("Card 1: ",player_hand[0],"\nCard 2: ",player_hand[1],"\nValue: ",player_hand_val)
    flag1 = False
    flag2 = True
    while(flag2):
        if(player_hand_val > 21):
            print("\nBust!")
            print("Computer wins!")
            if(restart()):
                player_hand_val = 0
                flag2 = False
                flag1 = True
                continue
        else:
            hitORstand = input("\n(h)it or (s)tand? ")
            if(hitORstand.lower() == "h"):
                card = deal()
                player_hand.append(card[0])
                val = card[1]
                                 
                player_hand_val = player_hand_val + val
                    
                print("\nPlayer is dealt a " , card[0] , " worth ", val)
                print("\nPlayer's new value is ", player_hand_val)
                continue
            elif(hitORstand.lower() == "s"):
                print("\nDealer flips their hidden card...\n")
                time.sleep(.5)
                print("\n...and reveals a(n) ",dealer_hand[0], " for a total of ", hidden_dealer_hand_val)
                if(player_hand_val > hidden_dealer_hand_val):
                    print("\nPlayer wins!")
                    
                elif(player_hand_val < hidden_dealer_hand_val):
                    print("\nComputer wins!")
                    
                elif(player_hand_val == hidden_dealer_hand_val):
                    print("\nIts a draw!")
                    
                if(restart()):
                    player_hand_val = 0
                    flag2 = False
                    flag1 = True
                    continue








                      
