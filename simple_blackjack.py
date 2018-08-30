# Main

# DEPENDENCIES
import random

# CLASSES

# Game class
class Game:
	def __init__(self):
		self.running = True # This used to keep game loop running
		self.bet = 0 # Amount player bet on the hand
		
	def first_deal(self):
		deck.deal_cards(player, 2)
		deck.deal_cards(dealer, 2)
		
		dealer.show_visible_hand() # Show visible_hand during actual play
		# dealer.show_hand_value() # Comment out for actual play
		dealer.show_bank()
		
		player.show_hand()
		player.show_hand_value()
		player.show_bank()
		
	def player_move(self): # Gets input from player
		end_turn = False
		
		while (end_turn == False):
			print("")
			cmd = input("(h)it or (s)tand? ")
			
			if (cmd == "h"):
				print("")
				print("<< Player hits >>")
				
				deck.deal_cards(player, 1)
				player.show_hand()
				player.show_hand_value()
				player.show_bank()
				
				if (player.hand_value > 21): # Check for bust
					player.bust = True
					print("")
					print("Player busts at {}!".format(player.hand_value))
					end_turn = True
				
			elif (cmd == "s"):
				print("")
				print("<< Player stands >>")
				player.show_hand()
				player.show_hand_value()
				player.show_bank()
				end_turn = True
		
	def dealer_move(self): # logic for dealer "choice"
		
		end_turn = False
		while (end_turn == False):
			if (dealer.hand_value < 17): # Check for mandatory hit
		
				deck.deal_cards(dealer, 1)
			
				print("")
				print("<< Dealer hits >>.")
			
				dealer.show_visible_hand()
				# dealer.show_hand_value()
				dealer.show_bank()
			
				if (dealer.hand_value > 21): # Check for bust
					dealer.bust = True
					print("")
					print("<< Dealer busts at {}! >>".format(dealer.hand_value))
					end_turn = True
					
			else:
				print("")
				print("<< Dealer stands >>")
				dealer.show_visible_hand()
				# dealer.show_hand_value()
				# dealer.show_bank()
				end_turn = True
			
	def check_hand_win(self): # Lose with bust
		victory_met = False
		
		while (victory_met == False): # while loop until victory condition is found
		
			if (player.bust == True) and (dealer.bust == False): # Player busted only
				player.won_hand = False 
				dealer.won_hand = True
				print("")
				print("The player loses the hand due to busting.")
				victory_met = True
		
			elif (dealer.bust == True) and (player.bust == False): # Dealer busted only
				dealer.won_hand = False
				player.won_hand = True
				print("")
				print("The dealer loses the hand due to busting.")
				victory_met = True
				
			elif (dealer.bust == True) and (player.bust == True): # Both bust. Unsure if this will work properly.
				dealer.won_hand = False
				player.won_hand = False
				print("")
				print("Dealer and player both busted.")
				print("The hand is a push.")
				victory_met = True
				
			elif (player.has_blackjack == True) and (dealer.has_blackjack == True): # Two blackjacks, dealer wins
				dealer.won_hand = True
				player.won_hand = False
				print("")
				print("Both player have Blackjack. Dealer wins on the tie.")
				victory_met = True
		
			else: # compare hand values (no bust or blackjack)
				if (player.hand_value > dealer.hand_value):
					player.won_hand = True
					dealer.won_hand = False
					victory_met = True
				elif (dealer.hand_value > player.hand_value):
					dealer.won_hand = True
					player.won_hand = False
					victory_met = True
				elif (player.hand_value == dealer.hand_value):
					dealer.won_hand = True
					player.won_hand = False
				else:
					player.won_hand = False
					dealer.won_hand = False # End of while loop
				
		# evaluate winner and do stuff
		
		if (player.won_hand == True) and (dealer.won_hand == False): # Player win
			print("")
			print("** Player wins! **")
			
			print("")
			dealer.show_hand()
			print("")
			player.show_hand()
			
			player.bank += (game.bet * 2)
			dealer.bank -= game.bet
			player.show_bank()
			
			
		elif (dealer.won_hand == True) and (player.won_hand == False): # Dealer win
			print("")
			print("** Dealer wins! **")
			
			print("")
			dealer.show_hand()
			print("")
			player.show_hand()
			
			player.bank -= game.bet
			dealer.bank += game.bet
			player.show_bank()
			
		else:
			print("")
			print("** The hand is a push. No one wins. **") # Push
			
			print("")
			dealer.show_hand()
			print("")
			player.show_hand()
			
			player.bank += game.bet
			player.show_bank()
			
		
	def wager(self): # Wagering function
	
		print("")
		
		valid_wager = False
		wager_amount = 0 
		
		while (valid_wager == False):
		
			print("How much will you bet on this hand?")
			print("You currently have {} in your bank.".format(player.bank))
			
			try:
				wager_amount = int(input("? $ "))
				
				if (wager_amount > player.bank):
					print("I'm afraid that you can't afford that wager.") # Too broke
					continue
				else:
					print("OK, your wager is {}".format(wager_amount)) # Wager is valid
					player.bank -= wager_amount
					game.bet = wager_amount
					valid_wager = True
			except: 
			
				print("")
				print("Please enter a valid amount to bet.")
				continue
			
		
		
			
class Deck:
	def __init__(self):
		
		# array of all cards in the deck
		self.all_cards = [
["2 SP", "3 SP", "4 SP", "5 SP", "6 SP", "7 SP", "8 SP", "9 SP", "10 SP", "J SP", "Q SP", "K SP", "A SP"],
["2 CL", "3 CL", "4 CL", "5 CL", "6 CL", "7 CL", "8 CL", "9 CL", "10 CL", "J CL", "Q CL", "K CL", "A CL"],
["2 HT", "3 HT", "4 HT", "5 HT", "6 HT", "7 HT", "8 HT", "9 HT", "10 HT", "J HT", "Q HT", "K HT", "A HT"],
["2 DI", "3 DI", "4 DI", "5 DI", "6 DI", "7 DI", "8 DI", "9 DI", "10 DI", "J DI", "Q DI", "K DI", "A DI"]		
]
		self.cards_dealt = [] # list track cards dealt from single deck
		
	def deal_cards(self, target, amount): 
		for i in range(amount):
		
			valid_card = False # Toggle boolean when non-dealt card selected
			while (valid_card == False): # loop until valid card
			
				s = random.randint(0,3) # random suit
				c = random.randint(0, 12) # random card
				
				if (self.all_cards[s][c] not in self.cards_dealt): # flow control to append lists/ toggle loop
					target.hand.append(self.all_cards[s][c])
					self.cards_dealt.append(self.all_cards[s][c])
					valid_card = True
				
					# Evaluate card
					
					if (c == 12): # if card is an ace
						if (target.hand_value <= 10):
							target.hand_value += 11
						else:
							target.hand_value += 1	
					elif (c == 0): # Numeric face values
						target.hand_value += 2
					elif (c == 1):
						target.hand_value += 3
					elif (c == 2):
						target.hand_value += 4
					elif (c == 3):
						target.hand_value += 5
					elif (c == 4):
						target.hand_value += 6
					elif (c == 5):
						target.hand_value += 7
					elif (c == 6):
						target.hand_value += 8
					elif (c == 7):
						target.hand_value += 9
				
					else: # Ten and face cards
						target.hand_value += 10		
				
			
				else:
					continue # keep looping if card chosen has already been dealt
		
class Player:
	def __init__(self):
		self.name = "Player"
		self.hand = []
		self.hand_value = 0
		self.bank = 100
		self.has_blackjack = False
		self.bust = False
		self.won_hand = False
		
	def show_name(self): # Testing method of parent and child class
		print("")
		print(self.name)

	def show_hand(self):
		print("")
		print("{} hand:".format(self.name))
		for card in self.hand:
			print(card)
	
	def show_hand_value(self):
		print("")
		print("{} hand value: {}".format(self.name, self.hand_value))
		
	def show_bank(self):
		print("{} bank: ${}".format(self.name, self.bank))
		
	def check_for_blackjack(self):
		ace_in_hand = False
		
		if ("A SP" in self.hand):
			ace_in_hand = True
		elif ("A CL" in self.hand):
			ace_in_hand = True
		elif ("A HT" in self.hand):
			ace_in_hand = True
		elif ("A DI" in self.hand):
			ace_in_hand = True
		else:
			ace_in_hand = False
		
		if (ace_in_hand == True and self.hand_value == 21):
			self.has_blackjack = True
		
class Dealer(Player): # Dealer is child class of Player
	def __init__(self):	
		self.name = "Dealer"
		self.hand = []
		self.visible_hand = []
		self.hand_value = 0 
		self.bank = 10000
		self.blackjack = False
		self.bust = False
		self.won_hand = False
		
	
	def show_visible_hand(self): # Called alternately to parent method. Hides 'hole' card.
		self.visible_hand = self.hand # populates visible_hand list
		self.visible_hand[0] = "??" # 'hides' fist card
		print("")
		print("{} hand:".format(self.name))
		for card in self.visible_hand: # prints iteration of visible_hand list
			print(card)	
		
			
		
# OBJECTS
game = Game()
deck = Deck()
player = Player()
dealer = Dealer()

def main():
	
	while(game.running): # Game loop
		
		game.wager()
		game.first_deal()
		player.check_for_blackjack()
		dealer.check_for_blackjack()
		game.player_move()

		if (player.bust == False): game.dealer_move()
		
		game.check_hand_win()
		
		if (player.bank < 1):
			print("You're broke!")
			print("Thanks for playing.")
			game.running = False
			break
		
		print("")
		print("Would you like to play another hand?")
		
		ask_play = str(input("(y)es or anything else to quit. "))
		ask_play.lower()
		
		if (ask_play == "y"):
			# reset game factors
			deck.cards_dealt = []
			
			player.hand = []
			player.hand_value = 0
			player.has_blackjack = False
			player.bust = False
			player.won_hand = False
			
			dealer.hand = []
			dealer.visible_hand = []
			dealer.hand_value = 0 
			dealer.blackjack = False
			dealer.bust = False
			dealer.won_hand = False
			wager_amount = 0
			game.bet = 0
			
			
			continue
			
		else:
			print("")
			print("Thanks for playing!")
			game.running = False
				
main()
	



