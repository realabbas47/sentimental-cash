# TODO
txt = input("Change owed: ")
while txt.isalpha() or txt == "":
    txt = input("Change owed: ")
txt = float(txt)
while txt < 0:
    txt = float(input("Change owed: "))
txt = round(txt * 100)
coins = 0
while txt >= 25:
    txt -= 25
    coins += 1
while txt >= 10:
    txt -= 10
    coins += 1
while txt >= 5:
    txt -= 5
    coins += 1
while txt >= 1:
    txt -= 1
    coins += 1
print(coins)
