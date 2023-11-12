# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

# Доска
board = [" " for _ in range(9)]

def table_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Проверка победителя
def check_winner(player):
    for i in range(3):
        if all([board[i*3+j] == player for j in range(3)]) or all([board[i+3*j] == player for j in range(3)]):
            return True
    if all([board[i*4] == player for i in range(3)]) or all([board[2*i+2] == player for i in range(3)]):
        return True
    return False

# Игрок делает ход
def moves(player):
    while True:
        move = int(input(f"Player {player}, ваш ход, введите номер клетки от 1 до 9: ")) - 1
        if move >= 0 and move < 9 and board[move] == " ":
            board[move] = player
            break
        else:
            print("Выход за диапазон клеток")

# Игровой процесс
def game():
    table_board()
    for turn in range(9):
        player = "O" if turn % 2 == 0 else "X"
        moves(player)
        table_board()
        if check_winner(player):
            print(f"Победил игрок {player}")
            return
    print("Победила дружба")

game()