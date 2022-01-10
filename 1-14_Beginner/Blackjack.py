import random

cards = [
    'A', 'A', 'A', 'A',
    '2', '2', '2', '2',
    '3', '3', '3', '3',
    '4', '4', '4', '4',
    '5', '5', '5', '5',
    '6', '6', '6', '6',
    '7', '7', '7', '7',
    '8', '8', '8', '8',
    '9', '9', '9', '9',
    '10', '10', '10', '10',
    'J', 'J', 'J', 'J',
    'Q', 'Q', 'Q', 'Q',
    'K', 'K', 'K', 'K'
    ]
value = {
    'A': 11, 
    '2': 2, 
    '3': 3, 
    '4': 4,
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8,
    '9': 9, 
    '10': 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10
}

def bj():
    random.shuffle(cards)
    banker = []
    player = []
    banker.append(cards.pop(0))
    player.append(cards.pop(0))
    banker.append(cards.pop(0))
    player.append(cards.pop(0))
    print(f"banker: '{banker[0]}'\nplayer: {player}")
    player_sum = 0
    banker_sum = 0
    end = False
    while not end:
        decision = input("hit or stand? ")
        if decision == "hit":
            player.append(cards.pop(0))
            print(f"banker: '{banker[0]}'\nplayer: {player}")
            for card in player:
                player_sum += value[card]
            if player_sum > 21:
                print("busted")
                end = True
        if decision == "stand":
            # print(f"banker: {banker}\nplayer: {player}")
            for card in banker:
                    banker_sum += value[card]
            while banker_sum <= 17:
                banker.append(cards.pop(0))
                banker_sum += value[banker[-1]]
            if banker_sum > 21:
                print(f"banker: {banker}\nplayer: {player}")
                print("player win!")
            if player_sum < banker_sum <= 21:
                print(f"banker: {banker}\nplayer: {player}")
                print("banker win!")
            end = True

def main():
    # test()
    end = False
    while not end:
        next = input("Do you want to play blackjack? y or n\n")
        if next == 'y':
            bj()
        elif next == 'n':
            end = True

main()