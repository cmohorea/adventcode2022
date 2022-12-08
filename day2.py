TXTFILE = "day2.txt"

def item_name (item):
    v = {"A":"Rock", "B":"Paper", "C":"Scissors", "X":"Rock", "Y":"Paper", "Z":"Scissors", }
    return v[item]

def item_cost (item):
# 1 for Rock, 2 for Paper, and 3 for Scissors
    v = {"X":1, "Y":2, "Z":3, }
    return v[item]

def intent (his, mine):
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    res = {
        "Z": {"A":"Y", "B":"Z", "C":"X"}, 
        "Y": {"A":"X", "B":"Y", "C":"Z"}, 
        "X": {"A":"Z", "B":"X", "C":"Y"},
    }

    return res[mine][his]

def game_cost (item):
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    res = {
        "XC":6, "YA":6, "ZB":6,     # win
        "XA":3, "YB":3, "ZC":3,     # tie
        "XB":0, "YC":0, "ZA":0      # lose
    }

    return res[item]

gamecost = 0
with open(TXTFILE, "r") as f:
    for line in f:
        line = line.strip()
        p1=line.split()[0]
        op2=line.split()[1]
        p2=intent(p1,op2)
        cost = item_cost (p2)
        game = game_cost (p2+p1)
        gamecost += cost
        gamecost += game
        print (f"{item_name(p1)} vs {item_name(p2)}:\t{cost}\t{game}\t{gamecost}")
