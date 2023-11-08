import openai
import json 
from dotenv import load_dotenv
import random
import os

house_questions = [
    "\nWhat trait do you value most in yourself?\n"
    "a. Courage\n"
    "b. Loyalty\n"
    "c. Intelligence\n"
    "d. Ambition",

    "\nIn a difficult situation, what is your instinctive reaction?\n"
    "a. Face it head-on\n"
    "b. Seek help from friends\n"
    "c. Analyze and strategize\n"
    "d. Find the most advantageous solution",

    "\nWhat kind of people do you admire?\n"
    "a. Brave and daring\n"
    "b. Loyal and true\n"
    "c. Intelligent and wise\n"
    "d. Ambitious and determined",

    "\nHow do you approach learning?\n"
    "a. Through experience\n"
    "b. Collaboratively with others\n"
    "c. By analyzing and studying\n"
    "d. Through strategic planning",

    "\nWhich animal represents you best?\n"
    "a. Lion\n"
    "b. Badger\n"
    "c. Eagle\n"
    "d. Serpent",

    "\nHow do you handle pressure?\n"
    "a. Confront it directly\n"
    "b. Rely on your support system\n"
    "c. Think strategically to find solutions\n"
    "d. Use it as motivation to succeed",

    "\nWhat type of magical creature fascinates you the most?\n"
    "a. Dragon\n"
    "b. Hippogriff\n"
    "c. Phoenix\n"
    "d. Basilisk",

    "\nWhat is your favorite school subject?\n"
    "a. Defense Against the Dark Arts\n"
    "b. Herbology\n"
    "c. Potions\n"
    "d. Transfiguration",

    "\nWhat kind of magical spell would you prefer to learn?\n"
    "a. A spell for protection and defense\n"
    "b. A spell for healing and nurturing\n"
    "c. A spell for knowledge and discovery\n"
    "d. A spell for manipulation and control",

    "\nWhich Hogwarts teacher do you find most interesting?\n"
    "a. Professor McGonagall\n"
    "b. Professor Sprout\n"
    "c. Professor Flitwick\n"
    "d. Professor Snape",
] 

harry_potter_candies = ["Bertie Bott's Every Flavor Beans", 'Chocolate Frogs', 'Fizzing Whizzbees', 'Droobles Best Blowing Gum', 'Pumpkin Pasties', 'Cockroach Clusters', 'Licorice Wands', 'Sherbet Lemons', 'Pepper Imps', 'Chocoballs', 'Honeydukes Chocolate', 'Exploding Bonbons', 'Lemon Sherbets', 'Toothflossing Stringmints', 'Fudge Flies', 'Sugar Quills', 'Jelly Slugs', 'Acid Pops', 'Cauldron Cakes', 'Blood-Flavored Lollipops', 'Treacle Tart', 'Caramel Cobwebs', 'Fainting Fancies', 'Pink Coconut Ice', 'Cinnamon Gobstoppers', 'Licorice Snaps', 'Ice Mice', 'Nougat Nipples', 'Sherbet Balls', 'Chocolate Cauldrons', 'Frosted Fizzballs', 'Peppermint Toads', 'Pumpkin Juice', 'Butterbeer', 'Firewhisky', 'Gillywater', 'Pumpkin Juice', 'Polyjuice Potion', 'Amortentia Infused Chocolate', 'Dungbomb', 'Fizzing Pumpkin Juice', 'Ton-Tongue Toffee', 'Nosebleed Nougat', 'Blood-Flavored Lollipops', 'Charm Choc', 'Muggle Fudge', 'Cockroach Clusters', 'Nougat', 'Sugar Quills', 'Peppermint Toads', 'Treacle Tart', 'Chocolate Cauldrons', 'Blood Pops', 'Acid Pops', 'Puking Pastilles', 'Jelly Slugs', 'Exploding Bonbons', 'Pumpkin Pasties', 'Chocoballs', 'Honeydukes Chocolate', 'Fudge Flies', 'Liquorice Wands', 'Sherbet Lemons', 'Cauldron Cakes', 'Butterbeer', 'Pumpkin Juice', 'Fizzing Whizzbees', 'Toothflossing Stringmints', 'Caramel Cobwebs', 'Fainting Fancies', 'Pink Coconut Ice', 'Pepper Imps', 'Licorice Snaps', 'Ice Mice', 'Nougat Nipples', 'Sherbet Balls', 'Frosted Fizzballs', 'Fizzing Pumpkin Juice', 'Chocolate Frogs']

prefix_key_list = ['Ignis', 'Electrum', 'Ventus', 'Vortex', 'Umbra', 'Fulgor', 'Frigus', 'Terra', 'Lux', 'Noctis', 'Aqua', 'Mysti', 'Aether', 'Pyro', 'Geo', 'Zephyr', 'Solaris', 'Lumin', 'Nebula', 'Venenum', 'Aegis', 'Verus', 'Magica', 'Serpens', 'Draconis', 'Bellum', 'Luxor', 'Astrum', 'Mors', 'Venatus', 'Ethereum', 'Pulcher', 'Rutilus', 'Ferox', 'Bellator', 'Vorax', 'Ultor', 'Somnium', 'Bellatrix', 'Nimbus', 'Oculus', 'Vivida', 'Abyssus', 'Incendia', 'Corpus', 'Fulminis', 'Sanguis', 'Tenebris', 'Furtivus', 'Tumultus', 'Ardens', 'Cauda', 'Scutum', 'Corona', 'Ruptura', 'Fatum', 'Ens', 'Phasma', 'Pulvis', 'Stella', 'Insidiae', 'Machina', 'Silentium', 'Spiritus', 'Victoria', 'Venator', 'Requiem', 'Praetor', 'Primus', 'Puritas', 'Quantum', 'Cognitus', 'Vastitas', 'Aquila', 'Nobilis', 'Inanis', 'Viscus', 'Silva', 'Vindico', 'Veritas']
prefix_value_list = ['Fire', 'Electric', 'Wind', 'Whirlwind', 'Shadow', 'Lightning', 'Ice', 'Earth', 'Light', 'Night', 'Water', 'Mystic', 'Ether', 'Fire', 'Earth', 'Breeze', 'Solar', 'Luminous', 'Nebula', 'Venom', 'Aegis', 'True', 'Magic', 'Serpent', 'Dragon', 'War', 'Luxury', 'Star', 'Death', 'Hunt', 'Ethereal', 'Pulchritudinous', 'Red', 'Ferocious', 'Warrior', 'Voracious', 'Avenger', 'Dream', 'Female Warrior', 'Cloud', 'Eye', 'Vivid', 'Abyss', 'Incendiary', 'Corporeal', 'Fulminant', 'Sanguine', 'Tenebrous', 'Furtive', 'Tumultuous', 'Ardent', 'Caudal', 'Scutum', 'Coronal', 'Rupturing', 'Fateful', 'Ensouled', 'Phasmic', 'Pulverizing', 'Stellar', 'Insidious', 'Mechanical', 'Silent', 'Spectral', 'Victorious', 'Venator', 'Requiem', 'Praetorial', 'Primordial', 'Purifying', 'Quantum', 'Cognizant', 'Devastating', 'Aquilan', 'Noble', 'Inanis', 'Visceral', 'Silvan', 'Vindictive', 'Veritable']

suffix_key_list = ['Fulminis', 'Ictus', 'Impetus', 'Ruptura', 'Secare', 'Terrae', 'Incendium', 'Voltum', 'Mortis', 'Magus', 'Nobilis', 'Ardens', 'Corpus', 'Cuspis', 'Decus', 'Dolorem', 'Draco', 'Ens', 'Ethereus', 'Fatum', 'Fulgur', 'Ignis', 'Inferni', 'Lux', 'Machina', 'Nex', 'Nimbus', 'Nox', 'Obscurum', 'Oculus', 'Os', 'Phasma', 'Pulvis', 'Sanguis', 'Scutum', 'Serpens', 'Silentium', 'Spiritus', 'Stella', 'Tenebris', 'Terra', 'Timor', 'Umbralis', 'Vates', 'Venenum', 'Vestigium', 'Victoria', 'Vigor', 'Vis', 'Vita', 'Vorago', 'Vortex', 'Aetas', 'Astra', 'Celeritas', 'Cognitus', 'Ferox', 'Fiducia', 'Fortis', 'Gravis', 'Honos', 'Inferus', 'Infinitus', 'Insidiae', 'Luxor', 'Majestas', 'Nebula', 'Nihilum', 'Noster', 'Nova', 'Praetor', 'Primus', 'Pulcher', 'Puritas', 'Quantum', 'Requiem', 'Sapiens', 'Solus', 'Somnium', 'Spes']
suffix_value_list = ['Bolt', 'Strike', 'Impetus', 'Rupture', 'Sever', 'Terra', 'Inferno', 'Voltage', 'Mortality', 'Mage', 'Noble', 'Ardent', 'Corpse', 'Cusp', 'Decoration', 'Dolor', 'Dragon', 'Essence', 'Ethereal', 'Fate', 'Lightning', 'Fire', 'Inferno', 'Light', 'Machine', 'Death', 'Nimbus', 'Night', 'Obscure', 'Ocular', 'Bone', 'Phasma', 'Powder', 'Blood', 'Shield', 'Serpent', 'Silentium', 'Spirit', 'Star', 'Darkness', 'Earth', 'Fear', 'Umbral', 'Vates', 'Venom', 'Trace', 'Victory', 'Vigor', 'Power', 'Life', 'Abyss', 'Vortex', 'Age', 'Star', 'Celerity', 'Cognizance', 'Ferocity', 'Fidelity', 'Fortitude', 'Gravity', 'Honor', 'Infernal', 'Infinity', 'Insidious', 'Luxury', 'Majesty', 'Nebula', 'Nihilum', 'Our', 'Nova', 'Praetor', 'Primus', 'Pulchritudinous', 'Purity', 'Quantum', 'Requiem', 'Sapience', 'Solus', 'Somnium', 'Hope']

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
            name_ret = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            name_returned = name_ret.choices[0].message.content
            return name_returned
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return "An error occurred"


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

            exp_ret = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            explanation_returned = exp_ret.choices[0].message.content
            return explanation_returned
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return "An error occurred"
    
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

