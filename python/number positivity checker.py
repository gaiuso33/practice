
def check_grade(score):
    if 70 > score < 100:
        return "A"
    elif 60 > score < 69:
        return "B"
    elif 50 > score < 59:
        return "C"
    elif 45 > score < 49:
        return "D"
    elif 0 > score < 44:
        return "F"
    else:
        return "cant be calculated"
score=float(input("Enter the score: "))
result=check_grade(score)
print(f"The grade  is {result}.")
