def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def assert_prompt(expected_answer):
    answer = int(input())

    if not answer == expected_answer:
        print('Please, try again')
        assert_prompt(expected_answer)


def ask_until_correct(question_stack, expected_answer):
    for line in question_stack:
        print(line)

    assert_prompt(expected_answer)


def test():
    print("Let's test your programming knowledge.")

    question_stack = [
        "How does JS works on server-side?",
        "1. All operation systems have been upgraded for that.",
        "2. It works in its own virtual machine.",
        "3. It uses V8 engine with bridging C++ layers",
        "4. By getting transpiled to platform native code."
    ]

    ask_until_correct(question_stack, 3)

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
