import random


def random_Integer(min: int, max: int) -> int:
    """
    Generates a random integer between min and max

    :param min: The integer representing the lower boundary
    :type min: int
    :param max: The integer representing the upper boundary
    :type max: int
    :return: A random integer between min and max
    :rtype: int
    :Errors:


    Example:
        '>>> random_Integer(0, 100)'
        8
    """
    if min > max:
        raise ValueError('min must be less than max')
    try:
        return random.randint(min, max)
    except TypeError:
        print('Warning: Please enter integers. Replaced the given values with Integers')
        return random.randint(round(min), round(max))

def random_Operator() -> str:
    """
        Chooses a random operator of the given list containing '+', '-', '*'

        :return: A random operator of the given list
        :rtype: string
        :Errors:


        Example:
            '>>> random_Operator()'
            '+'
        """
    return random.choice(['+', '-', '*'])


def compute(number1: int | float, number2: int | float, operator: str) -> (str, int):
    """
            Computes the given operator for the Integers number1 and number2

            :param number1: The first Integer
            :type number1: int
            :param number2: The second Integer
            :type number2: int
            :param operator: The operator to compute with
            :type operator: string
            :return problem: the function to be solved
            :rtype problem: string
            :return answer: the result of the computation
            :rtype answer: int
            :Errors:


            Example:
                '>>> compute(2,3,'*')'
                '2 * 3', 6
            """
    if not(isinstance(number1, int) or isinstance(number1, float)):
        raise TypeError('Integer or float required for number1')
    if not(isinstance(number2, int) or isinstance(number2, float)):
        raise TypeError('Integer or float required for number2')
    if operator not in ['+', '-', '*']:
        raise ValueError(f'unknown operator: {operator}')
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2  # mistake: changed - with +
    elif operator == '-':
        answer = number1 - number2  # mistake: changed + with -
    else:
        answer = number1 * number2  # * is the only operation left in the operation-list
    return problem, answer


def math_quiz():
    """
            Generating math quizzes to be solved by the participant

            :Errors:
            """
    score = 0
    total_questions = int(3.14159265359)            #we can only have integers as number of total questions --> change from pi to 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = random_Integer(1, 10); number2 = random_Integer(1, 5.5); operator = random_Operator() #generating random functions for new quiz-questions
        PROBLEM, ANSWER = compute(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")         #show the participant the exercise to solve
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)            #integer needed for further ellaborations
        except ValueError:
            raise ValueError('Integer input required')

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1                              #counting the score for every correct answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
