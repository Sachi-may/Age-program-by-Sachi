age_year=int(input("Enter your Age or birth year(you have to enter year more than 1900 and age less than 150)\n"))
if age_year>1900 and age_year<2021:
    print("Your birth year is ",age_year)
    age_year1=age_year+100
    print("You will be 100 years old at the year ",age_year1)
    print("If you are interested to know your age in any particular year enter I")
    var = input()
    if var == "I":
        intersted_year = int(input("Enter the year in which you want to know your age"))
        age_2 = intersted_year - age_year
        print(f"You will be {age_2} years old in the year of {intersted_year}")

elif age_year<150 and age_year>0:
    print("Your age is ", age_year )
    current_year=int(input("Enter the current year "))
    birth_year=current_year-age_year
    age=100-age_year
    age1=current_year+age
    print("You will be 100 years old in the year of",age1)
    print("If you are interested to know your age in any particular year enter I")
    var = input()
    if var == "I":
        intersted_year = int(input("Enter the year in which you want to know your age"))
        age_2 = intersted_year - birth_year
        print(f"You will be {age_2} years old in the year of {intersted_year}")
    else:
        exit("wrong input")

elif age_year>150 and age_year<1900:
    print("Invalid age or year")
    exit()
