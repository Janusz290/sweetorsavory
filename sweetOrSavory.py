import datetime
import math

# sweetOrSavory(mydate)
# mydate is a datetime.date sometime after 2017-09-15
# returns whether mydate is in the "Sweet" or "Savory" cycle
def sweetOrSavory(mydate):
    day1 = datetime.date(2017,9,15) # 2017-09-15 was the 1st day of a Sweet cycle
    duration = mydate - day1 
    durationInDays = duration.days + 1
    # Since a complete cycle consists of 5 Sweet & 5 Savory days,
    # we "mod" the duration by 10, which lets us know where in the cycle
    # the day falls into (1-5: Sweet, 6-10(0): Savory)
    dayInCycle = durationInDays % 10
    # print("duration is", durationInDays, "dayInCycle:", dayInCycle)
    if (0 < dayInCycle <= 5):
        return "Sweet"
    else:
        return "Savory"

# def getDateWhenTargetIsReached(myTacos, targetTacos, flavor)
# myTacos and targetTacos are both dicts of the form:
# {'Sweet':254, 'Savory':234}
# myTacos contains your current taco count
# targetTacos contains the number of tacos you're counting towards
# flavor is either "Sweet" or "Savory"
# returns when 
def getDateWhenTargetIsReached(myTacos, targetTacos, flavor):
    tacosNeeded = targetTacos[flavor] - myTacos[flavor]
    dailyTacoIncome = 3
    duration = math.ceil(tacosNeeded / dailyTacoIncome)
    # print("Duration:", duration)
    singleDay = datetime.timedelta(days=1)
    myDate = datetime.date.today()
    flavorCount = 0
    while (flavorCount <= duration):
        if (sweetOrSavory(myDate)) == flavor:
            flavorCount += 1
            # print(myDate, flavor, flavorCount)
        if (flavorCount <= duration):
            myDate += singleDay
    return myDate

def main():
    myTacos = {'Sweet':254, 'Savory':234}
    targetTacos = {'Sweet':300, 'Savory':300}
    sweetDuration = targetTacos['Sweet'] - myTacos['Sweet']
    savoryDuration = targetTacos['Savory'] - myTacos['Savory']
    for flavor in myTacos.keys():
        dateTargetIsReached = getDateWhenTargetIsReached(myTacos, targetTacos, flavor)
        print(targetTacos[flavor], flavor, "tacos will be reached on", dateTargetIsReached)

    
if __name__ == '__main__':
  main()    
