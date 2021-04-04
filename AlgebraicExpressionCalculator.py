# print(solve_eq("x + 4 = 9"))... x = 5
# print(solve_eq("x - 4 = 9"))... x = 13
# print(solve_eq("x / 5 = 2"))... x = 10
# print(solve_eq("x * 4 = 8"))... x = 2

def solve_eq(equation):
    variable, operator, num, equals, answer = equation.split()
    num, answer = int(num), int(answer)

    if operator == "+":
        return "{} ({} = {})".format(equation, variable, str(answer-num))
    elif operator == "-":
        return "{} ({} = {})".format(equation, variable, str(answer+num))
    elif operator == "/":
        return "{} ({} = {})".format(equation, variable, str(answer*num))
    elif operator == "*":
        return "{} ({} = {})".format(equation, variable, str(answer/num))
    else:
        return "Please enter a valid algebraic expression."


print(solve_eq("x + 4 = 9"))
print(solve_eq("x - 4 = 9"))
print(solve_eq("x / 4 = 9"))
print(solve_eq("x * 4 = 9"))
