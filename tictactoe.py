#python code of the tictactoe game where 2 players take turns and mark X and O in a grid 

import itertools #provides helper functions to handle iterators

#we use a function to check if there are any winners 
def winner(current_grid):

    #we use a function to check if all the elements are same in the list provided to it
    def same(check):
        if check.count(check[0]) == len(check) and check[0] != 0:
            return True
        else:
            return False

    #there are 3 possibilities of winning the game: horizontally, vertically, diagonally
    #if the same element is found in a row or in a column or in a diagonal row, then the player with that element is declared the winner

    #1st possibility - same element in a row - horizontal

    #iterate over each row
    for row in current_grid:
        print(row)
        #check if the elements in the row are same using the same() function that we declared above
        if same(row):
            print(f"{row[0]} is the winner \n")
            print("same element found in a row - horizontal")
            return True

    #2nd possibility - same element in a column - vertical
    
    #For this case, we need to check in each column, and so for that we collect the 1st element in each row and put them in a list
    for column in range(len(current_grid[0])):
        check = []
        #iterate over each row
        for row in current_grid:
            check.append(row[column])
        #check if the elements in the columns are same using the same() function that we declared above
        if same(check):
            print(f"{check[0]} is the winner \n")
            print("same element found in a column - vertical")
            return True

    #3rd possibility - same element in a diagonal row 
    #now for this there are 2 cases of diagonal row (\) and (/)

    #for the 1st case - \ we collect elements from each 'diagonal position' - (00, 11, 22 etc)
    diagonal = []
    for posn in range(len(current_grid)):
        diagonal.append(current_grid[posn][posn])

    #check if the elements in the diagonal row are same using the same() function that we declared above
    if same(diagonal):
        print(f"{diagonal[0]} is the winner \n")
        print("same element found in a diagonal row - (\\)")
        return True

    #for the 2nd case - / we collect elements from 'diagonal positions' like 20, 11, 10 (starts from the last element in the 1st row to the 1st element in the last row)
    diagonal = []
    #we use the reversed() to get the 'opposite' order of the row_order 
    for posn, posn1 in enumerate(reversed(range(len(current_grid)))):
        diagonal.append(current_grid[posn][posn1])

    if same(diagonal):
        print(f"{diagonal[0]} is the winner \n")
        print("same element found in a diagonal row - (/)")
        return True

    return False

#we use a function to enter the X or O in the position entered by each player
def enter(grid, player=0, row=0, column=0, just_display=False):
    try:
        #first check if the space or position is already used by the other player
        if grid[row][column] != 0:
            print("This space is marked, try another!")
            return False
        #used to print the index of the row - to help the player decide the position 
        print("   "+"  ".join([str(i) for i in range(len(grid))]))
        #check if the player wanted to just see the grid and if not, enter X or O according to the player
        if not just_display:
            #if it is player1, mark the position as X
            if(player==1):
               grid[row][column] = 'X'
            #else if it is player2, mark the position as O
            elif(player==2):
                grid[row][column] = 'O'
        #print the grid
        for count, row in enumerate(grid):
            print(count, row)
        return grid
    #check if the player entered a position which is not in the scope of this grid
    except IndexError:
        print("Did you attempt to play a row or column outside the scope of this grid 0,1 or 2?")
        return False
    #else general exception handling
    except Exception as e:
        print(str(e))
        return False
    
play = True
players = [1, 2]

while play:
    #to make sure the size of the grid is not hardcoded and fixed as 3x3
    grid_size = int(input("What should be the size of the grid? "))
    grid = [[0 for i in range(grid_size)] for i in range(grid_size)]

    #initially setting that there are no winners
    game_won = False
    #we use the helper function of the itertools 
    #using the cycle() we get an infinite iterator over the 'players'
    player_cycle = itertools.cycle([1, 2])
    #print the grid before each player starts to mark X and O
    enter(grid, just_display=True)

    while not game_won:
        #we use the helper function next() to choose one among each of the players([1,2]) and this goes as a cycle like current_player is 1, then 2, then again 1 and so on
        current_player = next(player_cycle)
        played = False

        while not played:
            print(f"Player: {current_player}")
            #this is where we ask the user to enter the desired position to mark 
            #column
            column_choice = int(input("Which column? "))
            #row
            row_choice = int(input("Which row? "))
            played = enter(grid, player=current_player, row=row_choice, column=column_choice)
        
        #if the user exited by typing 'exit', ask if they want to start again 
        if(column_choice == 'exit' or row_choice == 'exit'):
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting!")
            elif again.lower() == "n":
                print("Byeeeee!!!")
                play = False
            else:
                print("Not a valid answer, but... c ya!")
                play = False

        #if the game has been won, just ask if the players want to play again
        if winner(grid):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting!")
            elif again.lower() == "n":
                print("Byeeeee!!!")
                play = False
            else:
                print("Not a valid answer, but... c ya!")
                play = False