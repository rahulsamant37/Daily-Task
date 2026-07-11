## Create the question bank
## Create the answer of question bank
## Answer user for input
## Check if the answer matches
## Keep the track of the user score
## At the end of program show the user final score

import random

Question = {
    "Capital of France": "Paris",
    "Largest planet": "Jupiter",
    "Fastest land animal": "Cheetah",
    "Element with atomic number 1": "Hydrogen",
    "Color of the sky on a clear day": "Blue",
    "Author of '1984'": "Orwell",
    "Heaviest metal": "Osmium",
    "Smallest bone in the human body": "Stapes",
    "First man on the moon": "Armstrong",
    "Longest river": "Nile",
    "Largest ocean": "Pacific",
    "Continent with the most countries": "Africa",
    "Hottest planet": "Venus",
    "Currency of Japan": "Yen",
    "Tallest mountain": "Everest",
    "Largest desert": "Sahara",
    "Oldest living tree species": "Bristlecone",
    "National animal of Australia": "Kangaroo",
    "Creator of the theory of relativity": "Einstein",
    "Most spoken language": "English"
}

def Trivia_Game():
    question_list = list(Question.keys())
    total_question = 5
    score = 0
    selected_question = random.sample(question_list,total_question)
    for idx,ques in enumerate(selected_question):
        print(f"{idx+1}: {ques}")
        ans = input("Give your answer- ").strip().lower()
        if ans == Question[ques].lower():
            print('Correct!')
            score+=1
        else:
            print(f'Wrong! the right asnwer is {Question[ques]}')
    print(f'Your final score is {score}!')

Trivia_Game()