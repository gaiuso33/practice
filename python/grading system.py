
def check_grade(num):
    if 70 > num < 100:
        return "A"
    elif 60 > num < 69:
        return "B"
    elif 50 > num < 59:
        return "C"
    elif 45 > num < 49:
        return "D"
    elif 0 > num < 44:
        return "F"
    else:
        return "cant be calculated"
score=float(input("Enter the score: "))
result=check_grade(score)
print(f"The grade  is {result}.")
