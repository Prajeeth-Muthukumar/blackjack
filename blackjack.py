import random
import time

card_no = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
suite = ("Spade", "Diamond", "Cleaver", "Heart")

value = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : (1,11)}

class Card:
    def __init__(self, card_no, suite):
        self.card_no = card_no
        self.suite = suite
        self.value = value[card_no]

    def __str__(self):
        return f"{self.card_no} of {self.suite}"

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suite:
            for num in card_no:
                self.all_cards.append(Card(num, suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def remove(self):
        return self.all_cards.pop(-1)

class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []
        self.balance = 25
        self.score = 0
        self.card_count = 0
        self.ace_count = 0

    def __str__(self):
        return f"Player Name : {self.name}\nBalance : {self.balance}"
    
    def add_card(self, card, ai):
        self.player_cards.append(card)

        if not type(card.value) == type(tuple()):
            self.score += card.value
            self.card_count += 1

        else:
            self.card_count += 1
            self.ace_count += 1
            s1 = self.score+1; s2 = self.score+11
            if not ai:
                print("You Got an Ace Card!!!")
                print()
                if s2 > 21:
                    if not(self.ace_count > 1):
                        print("Ace Card is Here Considered as 1, If it is Considered as 11 It'll be More than 21")

                    else:
                        print("You Got Another Ace Card, It is Considered as 1 to not Cross 21")
                    self.score += 1

                elif s1 == 21 or s2 == 21:
                    if s1 == 21:
                        s = 1
                    else:
                        s = 11
                        
                    print(f"You Hit a BlackJack!!! Ace Card is Automatically Considered as {s} to Hit a BlackJack")
                    self.score = 21

                else:
                    ace_choice = int(input("What Do You Want to be the Score for an Ace Card(1 or 11): "))
                    self.score += ace_choice

            else:
                if not(self.card_count == 1):
                    if s1 == 21 or s2 == 21:
                        self.score = 21

                    elif s2 < 21 and s2 > 18:
                        self.score += 11

                    else:
                        self.score += 1

                else:
                    self.score += 11
                
                
    def clear(self):
        self.player_cards.clear()
        self.score = 0

    def add_coins(self, amount):
        self.balance += amount

    def remove_coins(self, amount):
        self.balance -= amount

    def display(self):
        print(f"{self.name} Cards :",end = " ")
        for i in self.player_cards:
            print(i, end = ", ")
        print()

    def total_score(self):
        return self.score

def end_Display():
    print()
    human.display()
    print(f"{human.name} Score :",human.total_score())
    computer.display()
    print(f"{computer.name} Score :", computer.total_score())
    print()
    
print("BlackJack : Player VS Computer")
print()

human = Player(input("Enter You Name : "))
print()
computer = Player("Computer")
rounds = 0

while human.balance > 0:
    deck = Deck()
    deck.shuffle()

    print(human)
    print()

    while True:
        bet_amount = int(input("Enter a Bet Amount Player : "))
        if human.balance < bet_amount:
            print("You Don't Have Enough Balance!!!")
            print()
            print(human)
            print()

        else:
            break
        
    for i in range(2):
        human.add_card(deck.remove(), False)
        computer.add_card(deck.remove(), True)
    
    print("\nComputer Cards :", computer.player_cards[0], ", ***********")
    human.display()
    print(f"{human.name} Score :", human.total_score(), "\n")
        
    if human.total_score() > 21:
        print(f"You Lost the Bet!!! You Lost {bet_amount} Coins")
        end_Display()
        human.remove_coins(bet_amount)

    elif computer.total_score() > 21:
        print(f"You Won the Bet!!! You Won {bet_amount} Coins")
        end_Display()
        human.add_coins(bet_amount)

    elif human.total_score() == 21 or computer.total_score() == 21:
        if human.total_score() == 21 and computer.total_score() == 21:
            print("Dealer and You, Both Got an BlackJack. No Coins are Lost")
            end_Display()
            print()
            print(human)
            print()

        elif human.total_score() == 21:
            print(f"BlackJack!!! You Won {bet_amount} Coins")
            human.add_coins(bet_amount)
            end_Display()
            print()
            print(human)
            print()

        else:
            print(f"Computer Got a Black Jack!! You Lost {bet_amount} Coins")
            human.remove_coins(bet_amount)
            end_Display()
            print()
            print(human)
            print()

    else:
        computer_play = True
        while True:
            choice = input("Do You Want to HIT (Y/N)???? : ")
            print()
            if choice.lower() == "y":
                new_Card = deck.remove()
                human.add_card(new_Card, False)
                print()
                print(f"You got {new_Card}")
                print()
                human.display()
                print(f"{human.name} Score :", human.total_score())
                print()

            else:
                break

            
            if human.total_score() > 21:
                print()
                print(f"You Lost the Bet!!! You Lost {bet_amount} Coins")
                computer.display()
                print("Computer Score :",computer.total_score())
                human.remove_coins(bet_amount)
                print()
                computer_play = False
                break

        counter = 0
        
        while computer_play:
                counter += 1
                if counter == 1:
                    computer.display()
                    print("Computer Score :",computer.total_score())
                    print()

                if computer.total_score() == 21:
                    print(f"You Lost {bet_amount} Coins!!!!")
                    print("Computer Score :", computer.total_score())
                    end_Display()
                    human.remove_coins(bet_amount)
                    break
                
                if computer.total_score() <= human.total_score():
                    print("Computer Hits\n")
                    time.sleep(1)
                    print()
                    new_Card = deck.remove()
                    computer.add_card(new_Card, True)
                    print("Computer Draws :", new_Card)
                    print()
                    computer.display()
                    print()
                    print("Computer Score :",computer.total_score())
                    print()

                if computer.total_score() > 21:
                    print(f"You Won {bet_amount} Coins!!!")
                    human.add_coins(bet_amount)
                    end_Display()
                    break

                if computer.total_score() > human.total_score():
                    print(f"Computer Wins!!! You Lost {bet_amount} Coins")
                    human.remove_coins(bet_amount)
                    end_Display()
                    break
                    
    human.clear()
    computer.clear()
    rounds += 1

    if human.balance != 0:
        nxt = input("Do You Want to Play Another Round(Y/N)??? : ")
        print()

        if nxt.upper() != "Y":
            break

if human.balance == 0:
    print("You Are Out of Coins!!! GGs")
    print("Rounds Lasted :", rounds)

else:
    print("GGs!!!")
    print(f"You Played {rounds} Rounds")
    net_coins = human.balance - 25
    
    if net_coins > 0:
        print(f"You Won {net_coins} Extra Coins")

    else:
        print("You Lost",abs(net_coins),"Coins")
