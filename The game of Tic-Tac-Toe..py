def print_board(board):
    """Функция для отображения игрового поля в консоли"""
    print("\n   0   1   2")  # Заголовок столбцов
    for i, row in enumerate(board, start=0):
        print(f"{i}  {' | '.join(row)}")


def check_winner(board):
    """Функция проверки завершенности игры (победа или ничья)"""
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Проверка на ничью
    if all(cell != ' ' for row in board for cell in row):
        return 'Ничья'

    return None


def get_valid_move(board, player):
    """Функция для получения корректного хода от игрока"""
    while True:
        try:
            # Получаем координаты хода
            row = int(input(f"Игрок {player}, введите номер строки (0-2): ")) - 0
            col = int(input(f"Игрок {player}, введите номер столбца (0-2): ")) - 0

            # Проверка диапазона
            if not (0 <= row <= 2) or not (0 <= col <= 2):
                print("Ошибка: координаты должны быть от 0 до 2!")
                continue

            # Проверка занятости клетки
            if board[row][col] != ' ':
                print("Эта клетка уже занята! Выберите другую.")
                continue

            return row, col
        except ValueError:
            print("Ошибка: введите числа от 0 до 2!")


def main():
    """Основная функция игры"""
    # Инициализация игрового поля
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Добро пожаловать в игру Крестики-нолики!")
    print("Игроки по очереди ставят X или O на поле 3х3.")
    print("Для хода введите номер строки и столбца (от 0 до 2).\n")

    while True:
        print_board(board)
        row, col = get_valid_move(board, current_player)

        # Выполняем ход
        board[row][col] = current_player

        # Проверяем состояние игры
        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Ничья':
                print("\nИгра окончена! Ничья!")
            else:
                print(f"\nИгрок {result} победил!")
            break

        # Переключаем игрока
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()