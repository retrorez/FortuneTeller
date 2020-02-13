import random

def getAnswer(r):
    if r == 1:
        return 'That is very likely'
    elif r == 2:
        return 'There\'s a good chance'
    elif r == 3:
        return 'I dont think that looks so good'
    elif r == 4:
        return 'Yes, for sure'
    elif r == 5:
        return 'Sorry, but no chance'
    elif r == 6:
        return 'I shouldnt answer that right now'
    elif r == 7:
        return 'Ask again later'
    elif r == 8:
        return 'Pretty doubtful'
    elif r == 9:
        return 'You didn\'t focus enough'

while True:
    r = random.randint(1,9)
    print('Concentrate, think of a question, and pick a number 1-9, the great CPU will guide you...')
    primer = int(input())      
    fortune = getAnswer(r * primer % 10)
    print(fortune)
    print('Again? Type yes to ask another question.')
    response = input()
    if response == 'yes':
        continue
    else:
        break

