# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.

GRADES = {"A": 4,
          "B": 3,
          "C": 2,
          "D": 1,
          "F": 0}
MODIFIER = 0.3

def main():
    # Output greeting
    greeting = "| GRADE CALCULATOR |"
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))

    print("Let's calculate your numerical grade value based on your letter grade!\n")

    grade = getString("Enter your letter grade. Valid grades include: A, B, C, D, F.\nOptional modifiers + / - are accepted and can be included right in the input.\n> ")
    gradeValue = convertLetterGrade(grade[0])

    try:
        gradeValue += getModifier(grade[1], grade[0])
    except:
        gradeValue = gradeValue

    if gradeValue != 99:
        if gradeValue > 4:
            gradeValue = 4
        
        print("The numeric value for your grade is {0}".format(gradeValue))
    else:
        print("You have entered an invalid input")
        main()
        return

    if (input("Enter another grade? (Y/N)\n> ").upper() == "Y"):
        main()

def getModifier(modIndex, grade):
    if grade.upper() != "F":
        match modIndex:
            case 1:
                return -0.3
            case 2:
                return 0.3
            case _:
                return 0
    else:
        return 0


def convertLetterGrade(grade):
    match grade.upper():
        case "A":
            return 4
        case "B":
            return 3
        case "C":
            return 2
        case "D":
            return 1
        case "F":
            return 0
        case _:
            return 99

def getString(outputString):
    inputString = input(outputString)
    grade = ""
    modifier = 0 # 0 = no modifier; 1 = minus modifier; 2 = plus modifier

    if len(inputString) == 0:
        return "Invalid input"

    match inputString[0].upper():
        case "A":
            grade = "A"
        case "B":
            grade = "B"
        case "C":
            grade = "C"
        case "D":
            grade = "D"
        case "F":
            grade = "F"
        case _:
            return "Invalid input"

    # Attempts to access inputString[1], where the modifier should be located. If no modifier exists, inputString[1] won't exist and function will return 0
    try:
        if inputString[1] == "+":
            return [grade, 2]
        elif inputString[1] == "-":
            return [grade, 1]
    except:
        return [grade, 0]
        
    return ["Invalid grade input.", 0]
    

if __name__ == "__main__":
    main()