'''
BLACK JACK GAME CREATED BY BRAYAN AYALA
MILESTONE PROJECT 2
Python Bootcamp Zero to Hero

'''

import random
import sys
from colorama import init, Fore, Back, Style

init(convert=True)


class Deck():

	def __init__(self, deck):
		self.deck = list(deck)

	def __str__(self):
		return f"Deck: {self.deck}"

	def my_deck(self):

		shuffle = random.choice(self.deck)
		shuffle2 = random.choice(self.deck)

		## Transformation occurs here
		## If shuffle gives a Jack', 'Queen' or 'King'
		if shuffle == 'Jack':
			shuffle = 10

		if shuffle == 'Queen':
			shuffle = 10

		if shuffle == 'King':
			shuffle = 10

		if shuffle2 == 'Jack':
			shuffle2 = 10

		if shuffle2 == 'Queen':
			shuffle2 = 10

		if shuffle2 == 'King':
			shuffle2 = 10

		newdeck = [shuffle, shuffle2]

		return newdeck

	def dealer_deck(self):

		shuffle = random.choice(self.deck)
		shuffle2 = random.choice(self.deck)

		## Transformation occurs here
		## If shuffle gives a Jack', 'Queen' or 'King'
		if shuffle == 'Jack':
			shuffle = 10

		if shuffle == 'Queen':
			shuffle = 10

		if shuffle == 'King':
			shuffle = 10

		if shuffle2 == 'Jack':
			shuffle2 = 10

		if shuffle2 == 'Queen':
			shuffle2 = 10

		if shuffle2 == 'King':
			shuffle2 = 10

		newdeck = [shuffle, shuffle2]

		return newdeck


class Player(Deck):

	def __init__(self, balance,deck):

		self.balance = balance
		self.deck = deck


	## Check current player balance "print(p1.balance)"
	def __str__(self):
		return f"Player Balance is: {self.balance}$"


	def my_balance(self):
		return f"Player Balance is: {self.balance}$"

	def make_bet(self,num):
		print(f"Player has made a bet of {num}$")
		self.balance -= num
				

	def add_to_balance(self,num):

		self.balance += num
		print(f"Player has received an amount of {num}$")


	def stand(self):
		return False

	def hit(self):
		return True



def Add_Card(playerdeck, deck):
	randcard = random.choice(deck)

	if randcard == 'Jack':
		randcard = 10

	if randcard == 'Queen':
		randcard = 10

	if randcard == 'King':
		randcard = 10

	playerdeck.append(randcard)

def Check_Win(playerdeck, playerdeck2):

	total = 0
	total2 = 0

	for card in playerdeck:
		total += card

	for card in playerdeck2:
		total2 += card

	if total == 21:
		winner = "BPlayer"
		return winner
	elif total2 == 21:
		winner = "BDealer"
		return winner
		

	if total > total2 and total <= 21:
		winner = "Player"
		return winner
	elif total < total2 and total2 <= 21:
		winner = "Dealer"
		return winner
	elif total == total2:
		winner = "Tied"
		return winner

	if total > 21:
		winner = "PBusted"
		return winner
	elif total2 > 21:
		winner = "DBusted"
		return winner

def play_again(answer):

	if answer == 'Yes' or answer == 'yes':
		return True
	elif answer == 'No' or answer == 'no':
		return False


#####
##### RUNNING GAME STRUCTURE
#####

print("WELCOME TO BLACKJACK GAME!")
print("")

game_deck = ['Hearts','Diamonds','Spades','Club',2,3,4,5,6,7,8,9,'Jack','Queen','King']

p1 = Player(500, game_deck)

## Turns Boolean
Gaming = True


while Gaming:

	betmade = True
	PlayerTurn = True
	askadd = True
	dealeradd = True
	DealerTurn = False

	while PlayerTurn:

		## Bet
		while betmade:
			try:
				playerbet = int(input("Place your bet: "))
				if p1.balance >= playerbet:
					p1.make_bet(playerbet)
					print("")
					betmade = False
					break
				else:
					print("You do not have enough money.")
					continue
			except:
				print("ERROR: place a real number. (not letters)")
				print("")
				continue

		#Player Deck
		playerdeck = p1.my_deck()

		print("Player Deck: ")
		print(playerdeck)

		##########################

		option = 0
		if 'Hearts' in playerdeck:
			print("You got an Ace!")
			print("")
			option = int(input("Do you want it to be a 1 or 11?: "))

		if option == 1:
			playerdeck.remove('Hearts')
			playerdeck.append(1)
		elif option == 11:
			playerdeck.remove('Hearts')
			playerdeck.append(11)

		option = 0
		if 'Diamonds' in playerdeck:
			print("You got an Ace!")
			option = int(input("Do you want it to be a 1 or 11?: "))

		if option == 1:
			playerdeck.remove('Diamonds')
			playerdeck.append(1)
		elif option == 11:
			playerdeck.remove('Diamonds')
			playerdeck.append(11)

		option = 0
		if 'Spades' in playerdeck:
			print("You got an Ace!")
			option = int(input("Do you want it to be a 1 or 11?: "))

		if option == 1:
			playerdeck.remove('Spades')
			playerdeck.append(1)
		elif option == 11:
			playerdeck.remove('Spades')
			playerdeck.append(11)

		option = 0
		if 'Club' in playerdeck:
			print("You got an Ace!")
			option = int(input("Do you want it to be a 1 or 11?: "))

		if option == 1:
			playerdeck.remove('Club')
			playerdeck.append(1)
		elif option == 11:
			playerdeck.remove('Club')
			playerdeck.append(11)


		total = 0
		for card in playerdeck:
			total += card

		print(f"Total is: {total}")

		while askadd:

			while True:
				ask = input("Do you want to add a card? (Yes or No): ")

				if ask == 'Yes' or ask == 'yes':
					break
				elif ask == 'No' or ask == 'no':
					break
				else:
					print("")
					print("Please write 'Yes' or 'No'!")
					continue

			if 'No' in ask or 'no' in ask:
				askadd = False
				PlayerTurn = False
				DealerTurn = True

			if 'yes' in ask or 'Yes' in ask:
				Add_Card(playerdeck, game_deck)

				print("NEW CARD ADDED TO DECK: ")
				print(playerdeck)

			option = 0
			if 'Hearts' in playerdeck:
				print("You got an Ace!")
				option = int(input("Do you want it to be a 1 or 11?: "))

			if option == 1:
				playerdeck.remove('Hearts')
				playerdeck.append(1)
			elif option == 11:
				playerdeck.remove('Hearts')
				playerdeck.append(11)

			option = 0
			if 'Diamonds' in playerdeck:
				print("You got an Ace!")
				option = int(input("Do you want it to be a 1 or 11?: "))

			if option == 1:
				playerdeck.remove('Diamonds')
				playerdeck.append(1)
			elif option == 11:
				playerdeck.remove('Diamonds')
				playerdeck.append(11)

			option = 0
			if 'Spades' in playerdeck:
				print("You got an Ace!")
				option = int(input("Do you want it to be a 1 or 11?: "))

			if option == 1:
				playerdeck.remove('Spades')
				playerdeck.append(1)
			elif option == 11:
				playerdeck.remove('Spades')
				playerdeck.append(11)

			option = 0
			if 'Club' in playerdeck:
				print("You got an Ace!")
				option = int(input("Do you want it to be a 1 or 11?: "))


			if option == 1:
				playerdeck.remove('Club')
				playerdeck.append(1)
			elif option == 11:
				playerdeck.remove('Club')
				playerdeck.append(11)


		total = 0
		for card in playerdeck:
			total += card

		print("NEW TOTAL: ")
		print(total)

	while DealerTurn:

		#Dealer Deck
		#option = random.choice([1,11])
		dealerdeck = p1.dealer_deck()

		print("Dealer DECK: ")
		print(dealerdeck)

		option = 0
		if 'Hearts' in dealerdeck:
			print("Dealer got an Ace!")
			option = random.choice([1,11])

		if option == 1:
			dealerdeck.remove('Hearts')
			dealerdeck.append(1)
		elif option == 11:
			dealerdeck.remove('Hearts')
			dealerdeck.append(11)

		option = 0
		if 'Diamonds' in dealerdeck:
			print("Dealer got an Ace!")
			option = random.choice([1,11])

		if option == 1:
			dealerdeck.remove('Diamonds')
			dealerdeck.append(1)
		elif option == 11:
			dealerdeck.remove('Diamonds')
			dealerdeck.append(11)

		option = 0
		if 'Spades' in dealerdeck:
			print("Dealer got an Ace!")
			option = random.choice([1,11])

		if option == 1:
			dealerdeck.remove('Spades')
			dealerdeck.append(1)
		elif option == 11:
			dealerdeck.remove('Spades')
			dealerdeck.append(11)

		option = 0
		if 'Club' in dealerdeck:
			print("Dealer got an Ace!")
			option = random.choice([1,11])


		if option == 1:
			dealerdeck.remove('Club')
			dealerdeck.append(1)
		elif option == 11:
			dealerdeck.remove('Club')
			dealerdeck.append(11)

			#position = dealerdeck.index('Ace')
			#dealerdeck[position] = 11

		dtotal = 0


		while dealeradd:

			for card in dealerdeck:
				dtotal += card

			if dtotal >= 17:
				dealeradd = False
				DealerTurn = False
				break

			Add_Card(dealerdeck, game_deck)
			print("NEW CARD ADDED TO DEALER DECK: ")
			print(dealerdeck)

			option = 0
			if 'Hearts' in dealerdeck:
				print("Dealer got an Ace!")
				option = random.choice([1,11])

			if option == 1:
				dealerdeck.remove('Hearts')
				dealerdeck.append(1)
			elif option == 11:
				dealerdeck.remove('Hearts')
				dealerdeck.append(11)

			option = 0
			if 'Diamonds' in dealerdeck:
				print("Dealer got an Ace!")
				option = random.choice([1,11])

			if option == 1:
				dealerdeck.remove('Diamonds')
				dealerdeck.append(1)
			elif option == 11:
				dealerdeck.remove('Diamonds')
				dealerdeck.append(11)

			option = 0
			if 'Spades' in dealerdeck:
				print("Dealer got an Ace!")
				option = random.choice([1,11])

			if option == 1:
				dealerdeck.remove('Spades')
				dealerdeck.append(1)
			elif option == 11:
				dealerdeck.remove('Spades')
				dealerdeck.append(11)

			option = 0
			if 'Club' in dealerdeck:
				print("Dealer got an Ace!")
				option = random.choice([1,11])

			if option == 1:
				dealerdeck.remove('Club')
				dealerdeck.append(1)
			elif option == 11:
				dealerdeck.remove('Club')
				dealerdeck.append(11)

		for card in dealerdeck:
			dtotal += card

	if Check_Win(playerdeck, dealerdeck) == "Player":
		print(Fore.GREEN + "Winner is PLAYER!")
		p1.add_to_balance(playerbet * 2)
		print(p1.my_balance())
		print(Style.RESET_ALL)
	elif Check_Win(playerdeck, dealerdeck) == "Dealer":
		print(Fore.RED + "Winner is DEALER!")
		print(p1.my_balance())
		print(Style.RESET_ALL)
	elif Check_Win(playerdeck, dealerdeck) == "Tied":
		p1.add_to_balance(playerbet)
		print(Fore.YELLOW + "MATCH TIED!")
		print(p1.my_balance())
		print(Style.RESET_ALL)
	elif Check_Win(playerdeck, dealerdeck) == "DBusted":
		print(Fore.GREEN + "DEALER: BUSTED!")
		print(Fore.GREEN + "Winner is PLAYER!")
		p1.add_to_balance(playerbet * 2)
		print(p1.my_balance())
		print(Style.RESET_ALL)
	elif Check_Win(playerdeck, dealerdeck) == "Busted":
		print(Fore.RED + "PLAYER: BUSTED!")
		print(Fore.RED + "Winner is DEALER!")
		print(p1.my_balance())
		print(Style.RESET_ALL)
	elif Check_Win(playerdeck, dealerdeck) == "BPlayer":
		print(Fore.GREEN + "BLACKJACK FOR PLAYER!")
		print(Fore.GREEN + "Winner is PLAYER!")
		p1.add_to_balance(playerbet * 2)
		print(p1.my_balance())
		print(Style.RESET_ALL)
	elif Check_Win(playerdeck, dealerdeck) == "BDealer":
		print(Fore.RED + "BLACKJACK FOR DEALER")
		print(Fore.RED + "Winner is DEALER!")
		print(p1.my_balance())
		print(Style.RESET_ALL)


	### Loop again if wanted
	while True:
		repeat = input("Do you want to play again? ")

		if repeat == 'Yes' or repeat == 'yes':
			break
		elif repeat == 'No' or repeat == 'no':
			break
		else:
			print("")
			print("Please write 'Yes' or 'No'!")
			continue


	if play_again(repeat):
		print("")
		Gaming = True
	else:
		print("")
		print(Fore.GREEN + "THANKS FOR PLAYING BLACKJACK!")
		print("GAME DEVELOPED BY BRAYAN AYALA")
		Gaming = False
