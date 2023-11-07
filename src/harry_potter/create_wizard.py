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

    




