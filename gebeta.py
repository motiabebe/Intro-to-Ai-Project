def gebeta():
    board = [[4, 4, 4, 4, 4, 4] for _ in range(2)]
    stores = [0, 0]

    player = 0
    while all(board[player]):
        print(f"Player {player+1}'s turn. The board is {board} and the stores are {stores}")
        pit = int(input("Choose a pit to sow from (1-6): ")) - 1
        hand = board[player][pit]
        board[player][pit] = 0

        while hand > 0:
            pit = (pit + 1) % 6
            if board[player][pit] > 0:
                hand += board[player][pit]
                board[player][pit] = 0
            else:
                board[player][pit] += 1
                hand -= 1

        stores[player] += board[player][pit]
        board[player][pit] = 0

        player = 1 - player

    print(f"Game over. The final stores are {stores}. Player {stores.index(max(stores))+1} wins!")

gebeta()