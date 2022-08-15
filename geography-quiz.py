# want_to_play=input('Welcome dude. Do you want to play? ')

# if want_to_play.lower() != 'yes':
#     quit()

# score=0

# answer=input('What is the capital of Australia? ')
# if answer.lower() == 'canberra':
#     print('Well done!')
#     score += 1
# else:
#     print('Incorrect :(')    

# answer=input('What is the capital of Canada? ')
# if answer.lower() == 'ottawa':
#     print('Well done!')
#     score += 1
# else:
#     print('Incorrect :(')    

# answer=input('What is the largest country of South America? ')
# if answer.lower() == 'brazil':
#     print('Well done!')
#     score += 1
# else:
#     print('Incorrect :(')    

# answer=input('What is the smallest country in the world? ')
# if answer.lower() == 'vatican':
#     print('Well done!')
#     score += 1
# else:
#     print('Incorrect :(')    

# answer=input('Which is more populated between Usa and pakistan? ')
# if answer.lower() == 'usa':
#     print('Well done!')
#     score += 1
# else:
#     print('Incorrect :(')    

# print(f'You got {score} points out of 5')    



want_to_play=input('Welcome dude. Do you want to play? ').lower()

if want_to_play != 'yes':
    print('Ok! Sorry to bother you')
    quit()

# QUESTIONS
CAPITAL_AUSTRALIA='What is the capital of Australia? '
CAPITAL_CANADA='What is the capital of Canada? '
LARGEST_CITY_SOUT_AMERICA='What is the largest country of South America? '
SMALLEST_COUNTRY='What is the smallest country in the world? '
USA_PAKISTAN='Which is more populated between Usa and pakistan? '
# QUESTIONS LIST
questions=[CAPITAL_AUSTRALIA,CAPITAL_CANADA,LARGEST_CITY_SOUT_AMERICA,SMALLEST_COUNTRY,USA_PAKISTAN]

# ANSWERS
CANBERRA='canberra'
OTTAWA='ottawa'
BRAZIL='brazil'
VATICAN='vatican'
USA='usa'
# ANSWERS LIST
correct_answers=[CANBERRA,OTTAWA,BRAZIL,VATICAN,USA]
max_point=len(correct_answers)


score=0
for question in questions:

    i=questions.index(question)
    answer=input(question).lower()

    if answer == correct_answers[i]:
        print('Well done!')
        score += 1
    else:
        print('Incorrect :(')

print(f'You got {score} points out of {max_point}')

        
