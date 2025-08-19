'''Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win= 4 points, 1 tie =2 points)'''

total_games_played = int(input("Enter total num. of games played in tournament :"))
games_won = int(input("Enter Num. of games won :"))
games_loss = int(input("Enter num. of games loss :"))

games_tie=total_games_played-games_won-games_loss
print("Total games Tie:",games_tie)

total_points = (games_won*4)+(games_tie*2)
print("Total Points :", total_points)