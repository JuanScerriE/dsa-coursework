import answers.q5 as q5

if 7.875 == q5.evaluate(q5.lex("65 32 -     7 32.125 - +")):
    print("\nTest Passed\n")
else:
    print("\nTest Failed\n")

if -82.7860696517413 == q5.evaluate(q5.lex("65 32 *     7 32.125 - /")):
    print("\nTest Passed\n")
else:
    print("\nTest Failed\n")

if -829.125 == q5.evaluate(q5.lex("65 32 - 7 32.125 - *")):
    print("\nTest Passed\n")
else:
    print("\nTest Failed\n")

expr = input("Input RPN Expression: ")

print("Result: " + str(q5.evaluate(q5.lex(expr))))
