#Variables
countries = {
    "China" : [4.5, 950],
    "USA" : [5, 1000],
    "Russia":[2, 750],
    "Brazil": [3.5, 800],
    "Japan": [4, 900],
    "India": [3, 850],
    "Japan": [3.5, 850],
}
playerdict = {}
query = ""

def separate():
    print('\n')
#Playerclass

class player:
    def __init__(self, country):
        self.country = country
        self.money = countries[country][1] + 2000 - countries[country][1]
        self.cash = 2000 - countries[country][1]
        self.assets = ["BMW"]
        self.stars = countries[country][0]
    def sayprop(self, property):
        separate()
        if property == "money":
            print(self.country + " has " + str(self.money) + "$")
        if property == "stars":
            print(self.country + " has " + str(self.stars))
        if property == "assets":
            print(self.country + " has " + str(self.assets))

def setup():
    print("Hello Welcome to the Pandemic Wars Dashboard")
    for i in range(0, int(input("How many players are there? "))):
        country = input("Which country did player " + str(i+1) + " get? " )
        playerdict[country] = player(country)

def give(sender, reciever, amount):
    separate()
    Sender = playerdict[sender]
    Reciever = playerdict[reciever]
    print(Sender.country + " has " + str(Sender.money))
    print(Reciever.country + " has " + str(Reciever.money))
    if Sender.money > amount:
        Sender.money = Sender.money - amount
        Reciever.money = Reciever.money + amount
    else:
        print(Sender.country + " does not have enough money!")
    print(str(amount) + " has been given to " + Reciever.country + " from " + Sender.country)
def trade(trader1, trader2):
    separate()
    tradee1 = playerdict[trader1]
    tradee2 = playerdict[trader2]
    tradeset = ""
    tradelst1 = []
    tradelst2 = []
    moneys = 0
    print("Welcome to the Trade program.")
    print(tradee1.country + " has " + str(tradee1.assets))
    print(tradee2.country + " has " + str(tradee2.assets))
    assets1 = tradee1.assets
    assets2 = tradee2.assets
    while tradeset != "done":
        tradeset = input("What would " + tradee1.country + " like to put in their tradelist? ")
        if tradeset == "done" and len(tradelst1) == 0:
            print("the deal has been cut.")
            break
        elif "money" in tradeset:
            tradeset = tradeset.removeprefix("money")
            moneys = moneys + int(tradeset)

        elif tradeset in assets1:
            tradelst1.append(tradeset)
            assets1.remove(tradeset)
        elif tradeset == "done":
            break
        elif tradeset not in assets1:
            print(tradee1.country + " doesnt have " + tradeset)
        print(tradee1.country + " now has " + str(assets1))
        print(tradee1.country + " has put up " + str(tradelst1) + " and " + str(moneys) + " money.")
    separate()
    tradeset = ""

    while tradeset != "done":
        tradeset = input("What would " + tradee2.country + " like to put in their tradelist? ")
        if tradeset == "end" and len(tradelst2) == 0:
            print("the deal has been cut.")
            break
        elif "money" in tradeset:
            tradeset = tradeset.removeprefix("money")
            moneys = moneys - int(tradeset)
        elif tradeset == "end":
            print(tradee2.country + " has put up " + str(tradelst2))
        elif tradeset in assets2:
            tradelst2.append(tradeset)
            assets2.remove(tradeset)
        elif tradeset == "done":
            break
        elif tradeset not in assets2:
            print(tradee2.country + " doesnt have " + tradeset)
        print(tradee2.country + " now has " + str(assets2))
        print(tradee2.country + " has put up " + str(tradelst2) + " and " + str(abs(moneys)) + " money.")
    final = input("Confirm? y/n")
    if final == "y":
        assets1 = assets1 + tradelst2
        assets2 = assets2 + tradelst1
        tradee1.assets = assets1
        tradee2.assets = assets2
        give(playerdict[trader1], playerdict[trader2], moneys)
    else:
        print("Trade has been cancelled")
    separate()
    print("A trade has occured. Between " + tradee1.country + " and " + tradee2.country)
    print(tradee1.country + " now has " + str(assets1))
    print(tradee2.country + " now has " + str(assets2))

def gain(reciever, amount):
    sender.money = sender.money + amount

def loss(sender, amount):
    reciever.money = reciever.money - amount
    if reciever.money < amount:
        print(reciever.country + "is bankrupt")

def describe(player):
    country = playerdict[player]
    print("Money: " + str(country.money) + "$")
    print("Assets: " + str(country.assets))
    print("Stars: " + str(country.stars))


setup()
funclst = ["describe", "loss", "gain", "trade", "give"]
query = ""
while query!= "Game Over":
    query = input("What should I do?: ")
    pref = query.split("(")[0]
    if pref in funclst:
        eval(query)
    else:
        print("No such function")
print("Thanks for playing!")
exit(0)




# Opening 3 assett cards to the tabe
# before that add a bear bull market flipped over




