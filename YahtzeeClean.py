import random

def rollDice(num_dice, num_rolls):
    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]
    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
        for die in range(0, len(double_list[roll])):
            double_list[roll][die] = (int)(random.random()*6 + 1)
    #print(double_list)
    return double_list


def sumOfRoll(double_list):
    SumRollList = []
    for rollgroup in range(len(double_list)):
        SumRoll = 0
        for die in double_list[rollgroup]:
            SumRoll = SumRoll + die
        SumRollList.append(SumRoll)
    #print (SumRollList)
    return SumRollList


def yahtzee(double_list):
    NumY = 0  
    count = 0
    for rollgroup in range(len(double_list)):
        NumRolls = len(double_list[rollgroup])
        first = double_list[rollgroup][0]
        count = double_list[rollgroup].count(first)
        if NumRolls == count:
            NumY = NumY + 1
    return NumY


def main():
    NumDice = int(input("How many dice are rolled?"+'\n'+">>> "))
    NumRolls = int(input("How many rolls?"+'\n'+">>> "))
    SimRollGame = rollDice(NumDice,NumRolls)
    print("Simulated game:", SimRollGame)
    if NumDice > 1:
        y = yahtzee(SimRollGame)
        if y == 1:
            print('\n', "You got a Yahtzee!")
        if y > 1:
            print('\n', "You got", y, "Yahtzees!")


if __name__ == '__main__':
    main()