import openai
import json 
from dotenv import load_dotenv
import random
from house_quiz_questions import house_questions
import os

class CreateWizard:

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = api_key
    
    #Lettting user choose the name
    def wizardNameGenerator(self, type):
        if isinstance(type, str) and type != "":
            pass
        else:
            return False
        try:
            messages = [{"role": "user", "content": f"Give me a {type} wizard name"}]
            name_ret = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            name_returned = name_ret["choices"][0]["message"]["content"]
            return name_returned
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return "An error occurred"

    def chooseCandy(self):
        pass

    def chooseAnimal(self):
        pass

    #Lettting user match the house
    def chooseHouse(self, preference):
        if isinstance(preference, str):
            pass
        else:
            return False
        try:
            answers = []
            for question in house_questions:
                response = input(question + "\nYour choice: \n").strip().lower()
            if response in ['a', 'b', 'c', 'd']:
                answers.append(response)
            else:
                print("Invalid choice. Please select a valid option.\n")
            
            house_scores = {
                'Gryffindor': answers.count('a'),
                'Hufflepuff': answers.count('b'),
                'Ravenclaw': answers.count('c'),
                'Slytherin': answers.count('d')
            }

            if preference in house_scores:
                house_scores[preference] += 1
            max_score = max(house_scores.values())
            possible_houses = [house for house, score in house_scores.items() if score == max_score]
            
            if len(possible_houses) == 1:
                selected_house = possible_houses[0]
            else:
                sorted_houses = random.sample(possible_houses, len(possible_houses))
                selected_house = sorted_houses[0]
            
            explanation = f"Give me a 2 sentence fake explanation of why student wanted to be sorted into {preference} and the Sorting Hat chose {selected_house}. Sentence should be directed towards the second person."

            messages = [{"role": "system", "content": "You are a student at Hogwarts."},
                        {"role": "user", "content": explanation}]

            name_ret = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            explanation_returned = name_ret["choices"][0]["message"]["content"]
            return explanation_returned
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return "An error occurred"

    



    




