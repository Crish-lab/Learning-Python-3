import random
name = 'Cris'
question = 'Am I going to meet Rihanna?'
answer = ''
random_number = random.randint(1, 9)

if random_number == 1:
    answer = 'Yes, defenetly, is how it meant to be'
if random_number == 2:
    answer = 'Sure, wait for it'
if random_number == 3:
    answer = 'is possible, dont loose the hope'
if random_number == 4:
    answer = 'you already know the answer, please ask me something else'
if random_number == 5:
    answer = 'is not likely, but maybe, who knows?'
if random_number == 6:
    answer = 'ask again later'
if random_number == 7:
    answer = 'the answer isnt clear'
if random_number == 8:
    answer = 'No, that would NEVER happen'
if random_number == 9:
    answer = 'That was stupid, please enter another question'

if name == '' and question == '':
    print('ERROR, please enter your name and a question')
elif question == '':
    print('ERROR, please enter a question')
elif name == '':
    print('ERROR, please enter your name')
else:
    print('Hello ' + name + ' Im the magic ball, your query is: ' + question +
          ' After consulting with my sources my answer to you is ' + answer)