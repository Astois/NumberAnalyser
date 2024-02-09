def main():
    UserList = input ("enter a list of numbers seperated with spaces  ")
    List = sorted(map(int,UserList.split()), key=int)
    MinValue = List[0]  # assuming the first number is the smallest one
    MaxValue = List[-1] # assuming the last number is the largest one
    Average = sum(List) / len(List)
    Num10 = List.count(10)
    Num15 = List.count(15)

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

main()     