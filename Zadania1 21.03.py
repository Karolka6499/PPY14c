
print("--1--")
numb = input("Podaj liczby rozdzielone przecinkiem: ")
numb_list = numb.split(",")
min_num = int(numb_list[0])
max_num = int(numb_list[0])

for number in numb_list:
    number = int(number)
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number

print("Najmniejsza liczba to:", min_num)
print("Największa liczba to:", max_num)


print("--2--")
import random
v_cit = []
cit = ["Warszawa", "Kraków", "Łódź", "Wrocław",
          "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz",
          "Lublin", "Katowice"]
for i in range(10):
    city = random.choice(cit)
    v_cit.append(city)
    cit.remove(city)
print("Plan wycieczki:")

for i, city in enumerate(v_cit):
    print(i+1, ".", city)

print("--3--")
import random

def get_player_choice(player_name):
    choices = ['p', 'n', 'k']
    choice = ''
    while choice not in choices:
        choice = input(f"{player_name}, wybierz : papier (p), kamień (k) lub nożyce (n) : ")
    return choice

def play_round(player1_name, player2_name=None):
    if player2_name is None:
        player2_name = "Komputer"
        player2_choice = random.choice(['p', 'k', 'n'])
    else:
        player2_choice = get_player_choice(player2_name)

    player1_choice = get_player_choice(player1_name)

    #print(f"{player1_name} wybrał {player1_choice}")
    #print(f"{player2_name} wybrał {player2_choice}")

    if player1_choice == player2_choice:
        print("Remis!")
        return 0
    elif player1_choice == 'p' and player2_choice == 'n' \
            or player1_choice == 'k' and player2_choice == 'p'\
            or player1_choice == 'n' and player2_choice == 'k' :

        print(f"{player1_name} wygrywa runde !  :)")
        return 1
    else:
        print(f"{player2_name} wygrywa runde !  :)")
        return 2

def play_game(num_rounds, is_computer_game):
    player1_name = input("Gracz 1, podaj swoje imie : ")

    if not is_computer_game:
        player2_name = input("Gracz 2, podaj swoje imie : ")
    else:
        player2_name = None

    player1_score = 0
    player2_score = 0

    for i in range(num_rounds):
        print(f"Runda {i + 1}:")
        winner = play_round(player1_name, player2_name)

        if winner == 1:
            player1_score += 1
        elif winner == 2:
            player2_score += 1

    print("Koniec gry.")
    print(f"Wynik końcowy:")
    print(f"{player1_name}: {player1_score}")
    print(f"{player2_name}: {player2_score}")
    if player1_score > player2_score:
        print(f"{player1_name} wygrał grę!  :)")
    elif player2_score > player1_score:
        print(f"{player2_name} wygrał grę!  :)")
    else:
        print("Remis!   :)")

if __name__ == '__main__':
    num_rounds = int(input("Podaj liczbę rund: "))
    is_computer_game = input("Czy chcesz grać z komputerem? [t/n]: ").lower() == 't'

    if is_computer_game:
        play_game(num_rounds, True)
    else:
        play_game(num_rounds, False)
