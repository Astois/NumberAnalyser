def main():
    ListType = input("what data type will you be using for your list?(int or str or bool)  ")

    if ListType == "int": 
        def numberL():

            UserNList = input("enter a list of numbers seperated with spaces  ")
            NList = sorted(map(int,UserNList.split()), key=int)
            MinValue = NList[0]  # assuming the first number is the smallest one
            MaxValue = NList[-1] # assuming the last number is the largest one
            Average = sum(NList) / len(NList)
            Num10 = NList.count(10)
            Num15 = NList.count(15)

            print(f"The minimum value in the list is {MinValue}")
            print(f"The maximum value in the list is {MaxValue}")
            print(f"The average of all values in the list is {Average:.2f}")
            if Num10 > 0 :
                print (f"There are {Num10} occurrences of the number 10.")
            else:
                print("There are no occurrences of the number 10.")

            if Num15 > 0:
                print (f"There are {Num15} occurrences of the number 15.")
            else:
                print("There are no occurrences of the number 15.")
    if ListType == "str":
        def LetterL():
            UserLList = input("Enter a list of Letters separated by space:   ")
            LList =  [char for word in  UserLList.split() for char in word ]
            LetterLLength =  len(LList)
            vowels =  ['a', 'e','i','o','u']
            Lvowels = len([letter for letter in LList if letter in vowels])
            print(f"The length of the letter list is {LetterLLength}.")
            print(f"There are {Lvowels} vowels in the list.")

    if ListType == "bool":
        def  boolL():
            UserBList = input("Enter yes or no (or 1 and 0)answers separated by space:   ")
            BList = UserBList.split()
            TrueCount = 0
            FalseCount = 0
            for item in BList:
                if item.lower() in ["1","yes"]:
                    TrueCount += 1
                elif item.lower() in ["0",'no']:
                    FalseCount += 1
            print(f"The true count is {TrueCount}, and false count is {FalseCount}.")

    if ListType == "str":
        LetterL()
    elif  ListType == "int":
        numberL()
    else:
        boolL()
main()    