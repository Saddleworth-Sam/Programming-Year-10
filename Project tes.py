import time
import decimal

#Greater Than >
#Less Than <


#One Pence
onePenceW = 3.56
MaxOnePenceW = 3.56 * 100


#Two Pence
twoPenceW = 7.12
MaxTwoPenceW = 7.12 * 50

#Five Pence
fivePenceW = 3.25
MaxFivePenceW = 3.25 * 100

#10 Pence
tenPenceW = 6.50
MaxTenPenceW = 6.50 * 50

#Twenty Pence
twentyPenceW = 5.00
MaxTwentyPenceW = 5.00 * 50

#Fifty Pence
fiftyPenceW = 8.00
MaxFiftyPenceW = 8.00 * 20

#One Pound
onePoundW = 9.50
MaxOnePoundW = 9.50 * 20

#Two Pound
twoPoundW = 12.00
MaxTwoPoundW = 12.00 * 10


#Enter the coin type
coinType = input("Enter the type of Coin: ")
coinType = coinType.lower()

#One Pence
if coinType == ("one pence") or coinType == ("1p"):
    print("Type of coin set to: One Pence")
    time.sleep(1)
    weight = float(input("Enter the weight of your bag:"))
    new = weight - MaxOnePenceW
    other = new / 3.56
    if weight > MaxOnePenceW:
        print("Your bag exceeds the maximum amount.")
        print("Please remove this amount of coin(s):", + other)
    elif weight < MaxOnePenceW:
        new = abs(new)
        other = new / 3.56
        a = decimal.Decimal("43.8")
        print(round(a,0))
        print("Your bag is lower than the weight needed")
        print("Please add this amount of coin(s):", + other)
else:
    print("P")