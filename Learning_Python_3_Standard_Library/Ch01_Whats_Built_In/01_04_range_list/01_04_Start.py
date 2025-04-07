# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

numberedContestants = range(30)
print(list(numberedContestants)) #prints out list
print(numberedContestants, '\n') #prits range object

#range(start(inclusive), stop(exclusive), step)
luckyWinners = range(7, 30, 5)
print(list(luckyWinners))