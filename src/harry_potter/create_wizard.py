from  arrayFile import harry_potter_candies, prefix_key_list, prefix_value_list, suffix_key_list, suffix_value_list
import random

class CreateWizard:
    
    
    # type indicates good or bad
    def wizardNameGenerator(self,type):
        pass

    def pickName(slef):
        pass


    #Get the number of harry potter candies
    def chooseCandy(self, n):
    
        for i in range(n):
             rand = random.randint(0, 78)
             print(harry_potter_candies[rand])

    #Creates fighting spells -> take # of spells to be generatred
    def generateFightingSpell(self, n): 

        for i in range(n):

            randP = random.randint(0, 79)
            randS  = random.randint(0, 79)

            print(f"Spell {i+1}:")
            print(f"Action: {prefix_key_list[randP]} {suffix_key_list[randS]}")
            print(f"Translation: {prefix_value_list[randP]} {suffix_value_list[randS]}\n")

      
    def chooseAnimal(self):
        pass

    def chooseHouse(self):
        pass

    




