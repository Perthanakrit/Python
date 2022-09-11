def choice ():
   country = """Brunei Darussalam = 1 
Cambodia = 2 
Laos = 3
Malaysia = 4
Philippines = 5
Singapore = 6
Vietnam = 7Indonesia = 8
Myanmar = 9"""
   print(country)
   print("----------------------------")

def BruneiDarussalam (money):
    moneyBND = money * 0.041
    print("BruneiDarussalam money => ",'%.3f' %moneyBND, "BND")
def Cambodia (money):
    moneyKHR = money * 122.52
    print("Cambodia money => "'%.3f' % moneyKHR, "KHR")

choice()

uSer = int(input("select exchanging money :"))
if uSer == 1:
    money = float(input("Thai money :"))
    BruneiDarussalam(money)
elif uSer == 2:
    money = float(input("Thai money :"))
    Cambodia(money)


