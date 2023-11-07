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

    



    




from  .array_File import harry_potter_candies, prefix_key_list, prefix_value_list, suffix_key_list, suffix_value_list
import random

class CreateWizard:
        
    # type indicates good or bad
    def wizardNameGenerator(self,type):
        pass

    def pickName(slef):
        pass

    #Randomply pick harry potter candies -> takes # of candies to be returned
    def chooseCandy(self, n):
        my_list = []
        
        #Check Value passed is in int
        if isinstance(n, int):
            pass 
        else:
            return False
        
        #randomly pick n candies and append to a list
        for i in range(n):
             rand = random.randint(0, 78)
             my_list.append(harry_potter_candies[rand])
        
        return my_list

    #Creates fighting spells -> take # of spells to be generatred
    def generateFightingSpell(self, n): 

        #Check value passed is an int 
        if isinstance(n, int):
            pass 
        else:
            return False

        outer_array = []
        
        #randomly pick n spells and their english translations and append to list
        for i in range(n):

            randP = random.randint(0, 79)
            randS  = random.randint(0, 79)

            inner_array = [prefix_key_list[randP], suffix_key_list[randS], prefix_value_list[randP], suffix_value_list[randS]]
            outer_array.append(inner_array) 

        return outer_array

    def chooseAnimal(self):
        pass

    def chooseHouse(self):
        pass

    




