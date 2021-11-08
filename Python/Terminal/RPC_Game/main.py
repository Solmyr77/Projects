import random

choices = ['kő', 'papír', 'olló']

generated_pick = choices[random.randint(0,2)]
print(generated_pick)
user_pick = str(input('Kő, papír, olló?: ')).lower()

if user_pick == 'kő' and generated_pick not in ['papír']:
    print ('Nyertél')