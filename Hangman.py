# https://tinyurl.com/h9q2cpc 

def hangman():
    wrong = 0
    stages = ["", "________ ", "|     |   ", "|     0   ", "|    /|\  ", "|    / \  ", "|         "]
    win = False

    print("Welcome to Hangman!")

    while True:
        word = input("Player One, enter a word for Player Two to guess: ").lower()
        if not word.isalpha():
            print("Please enter a valid word (letters only).")
            continue
        break

    rletters = list(word)
    board = ["__"] * len(word)

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg).lower()

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        print("\n".join(stages[0:wrong + 1]))

        if "__" not in board:
            print("You win! The word was: {}".format(word))
            win = True
            break

    if not win:
        print("\n".join(stages))
        print("You lose! The word was: {}".format(word))

hangman()