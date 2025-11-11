class MultipleFunctions():

    # Create a function, and list out the items in the list

    def SubfieldsInAI(Subfileds):
        for i in Subfileds:
            print(i)

    ai_fileds = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing',
                 'Natural Language Processing']
    print('Sub-fields in AI are : ')
    SubfieldsInAI(ai_fileds)

    # Create a function that checks whether the given number is Odd or Even

    def OddEven():
        number = int(input("Enter a number : "))
        if number % 2 == 0:
            print(number, "is Even number")
            Oddeven = number, "is Even number"
        else:
            print(number, "is Odd Number")
            Oddeven = number, "is Odd number"
        return Oddeven

    OddEven()

    # Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female

    def ElegiblityForMarriage():
        gender = input("Enter your gender:")
        age = int(input("Enter your age:"))
        if (gender == "male" and age >= 21):
            print("ELIGIBLE")
            ElegiblityForMarriage = "ELIGIBLE"
        elif (gender == "female" and age >= 18):
            print("ELIGIBLE")
            ElegiblityForMarriage = "ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            ElegiblityForMarriage = "NOT ELIGIBLE"
        return ElegiblityForMarriage

    ElegiblityForMarriage()

    # calculate the percentage of your 10th mark

    def FindPercent():
        subject1 = int(input("subject1 ="))
        subject2 = int(input("subject2 = "))
        subject3 = int(input("subject3 = "))
        subject4 = int(input("subject4 = "))
        subject5 = int(input("subject5 = "))

        total = subject1 + subject2 + subject3 + subject4 + subject5
        print("total:", total)
        percentage = total / 500 * 100
        print("percentage", percentage)

        return total, percentage

    FindPercent()

    # print area and perimeter of triangle using functions

    def triangle():
        h = int(input("Height:"))
        b = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Areaoftriangle = (h * b) / 2
        print("Area of Traingle:", Areaoftriangle)
        h1 = int(input("Height1:"))
        h2 = int(input("Height2:"))
        b1 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeteroftriangle = h1 + h2 + b1
        print("Perimeter of Traingle:", Perimeteroftriangle)
        return Areaoftriangle, Perimeteroftriangle

    triangle()


MultipleFunctions.OddEven()





