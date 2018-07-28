import time
import turtle
import math
print("When asked questions MAKE IT LOWERCASE, if it the entire answer is not lowercase the app will stop working.")
SaveOverWrite = 0
SaveData = 0
FoodName = 0
FridgeFoodAmount = 0
FridgeEmpty = input("Is your Firdge Empty?")
FridgeEmpty_Check = 0
if  FridgeEmpty == "yes":
    print("Saving... Don't exit")
    SaveData = open('FridgeTracker.txt','w')
    SaveData.write("Empty!")
    print("Saved")

else:
    FridgeEmpty_Check = 1
    FridgeFoodAmount = input("How much food do you have")
    print("You have")
    print(FridgeFoodAmount)
    print("Food")
    FoodName = input("Name all the food you want to add to the fridge tracker")
    print ("Saving... Don't exit")
    SaveOverWrite = input("Want to remove everything from last save? (If your last save was empty then say yes)")
if SaveOverWrite == "yes":
    SaveData = open('FridgeTracker.txt','w')
    SaveData.write(FoodName)
    print("Done Saving.")
if SaveOverWrite == "no":
    SaveData = open('FridgeTracker.txt','a')
    SaveData.write(FoodName)
    print("Done Saving.")
print("Bye!!!!!!!")
Exit = input('Press Enter to exit')
