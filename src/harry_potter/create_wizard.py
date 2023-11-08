# from  .array_File import harry_potter_candies, prefix_key_list, prefix_value_list, suffix_key_list, suffix_value_list
import random

harry_potter_candies = ["Bertie Bott's Every Flavor Beans", 'Chocolate Frogs', 'Fizzing Whizzbees', 'Droobles Best Blowing Gum', 'Pumpkin Pasties', 'Cockroach Clusters', 'Licorice Wands', 'Sherbet Lemons', 'Pepper Imps', 'Chocoballs', 'Honeydukes Chocolate', 'Exploding Bonbons', 'Lemon Sherbets', 'Toothflossing Stringmints', 'Fudge Flies', 'Sugar Quills', 'Jelly Slugs', 'Acid Pops', 'Cauldron Cakes', 'Blood-Flavored Lollipops', 'Treacle Tart', 'Caramel Cobwebs', 'Fainting Fancies', 'Pink Coconut Ice', 'Cinnamon Gobstoppers', 'Licorice Snaps', 'Ice Mice', 'Nougat Nipples', 'Sherbet Balls', 'Chocolate Cauldrons', 'Frosted Fizzballs', 'Peppermint Toads', 'Pumpkin Juice', 'Butterbeer', 'Firewhisky', 'Gillywater', 'Pumpkin Juice', 'Polyjuice Potion', 'Amortentia Infused Chocolate', 'Dungbomb', 'Fizzing Pumpkin Juice', 'Ton-Tongue Toffee', 'Nosebleed Nougat', 'Blood-Flavored Lollipops', 'Charm Choc', 'Muggle Fudge', 'Cockroach Clusters', 'Nougat', 'Sugar Quills', 'Peppermint Toads', 'Treacle Tart', 'Chocolate Cauldrons', 'Blood Pops', 'Acid Pops', 'Puking Pastilles', 'Jelly Slugs', 'Exploding Bonbons', 'Pumpkin Pasties', 'Chocoballs', 'Honeydukes Chocolate', 'Fudge Flies', 'Liquorice Wands', 'Sherbet Lemons', 'Cauldron Cakes', 'Butterbeer', 'Pumpkin Juice', 'Fizzing Whizzbees', 'Toothflossing Stringmints', 'Caramel Cobwebs', 'Fainting Fancies', 'Pink Coconut Ice', 'Pepper Imps', 'Licorice Snaps', 'Ice Mice', 'Nougat Nipples', 'Sherbet Balls', 'Frosted Fizzballs', 'Fizzing Pumpkin Juice', 'Chocolate Frogs']

prefix_key_list = ['Ignis', 'Electrum', 'Ventus', 'Vortex', 'Umbra', 'Fulgor', 'Frigus', 'Terra', 'Lux', 'Noctis', 'Aqua', 'Mysti', 'Aether', 'Pyro', 'Geo', 'Zephyr', 'Solaris', 'Lumin', 'Nebula', 'Venenum', 'Aegis', 'Verus', 'Magica', 'Serpens', 'Draconis', 'Bellum', 'Luxor', 'Astrum', 'Mors', 'Venatus', 'Ethereum', 'Pulcher', 'Rutilus', 'Ferox', 'Bellator', 'Vorax', 'Ultor', 'Somnium', 'Bellatrix', 'Nimbus', 'Oculus', 'Vivida', 'Abyssus', 'Incendia', 'Corpus', 'Fulminis', 'Sanguis', 'Tenebris', 'Furtivus', 'Tumultus', 'Ardens', 'Cauda', 'Scutum', 'Corona', 'Ruptura', 'Fatum', 'Ens', 'Phasma', 'Pulvis', 'Stella', 'Insidiae', 'Machina', 'Silentium', 'Spiritus', 'Victoria', 'Venator', 'Requiem', 'Praetor', 'Primus', 'Puritas', 'Quantum', 'Cognitus', 'Vastitas', 'Aquila', 'Nobilis', 'Inanis', 'Viscus', 'Silva', 'Vindico', 'Veritas']
prefix_value_list = ['Fire', 'Electric', 'Wind', 'Whirlwind', 'Shadow', 'Lightning', 'Ice', 'Earth', 'Light', 'Night', 'Water', 'Mystic', 'Ether', 'Fire', 'Earth', 'Breeze', 'Solar', 'Luminous', 'Nebula', 'Venom', 'Aegis', 'True', 'Magic', 'Serpent', 'Dragon', 'War', 'Luxury', 'Star', 'Death', 'Hunt', 'Ethereal', 'Pulchritudinous', 'Red', 'Ferocious', 'Warrior', 'Voracious', 'Avenger', 'Dream', 'Female Warrior', 'Cloud', 'Eye', 'Vivid', 'Abyss', 'Incendiary', 'Corporeal', 'Fulminant', 'Sanguine', 'Tenebrous', 'Furtive', 'Tumultuous', 'Ardent', 'Caudal', 'Scutum', 'Coronal', 'Rupturing', 'Fateful', 'Ensouled', 'Phasmic', 'Pulverizing', 'Stellar', 'Insidious', 'Mechanical', 'Silent', 'Spectral', 'Victorious', 'Venator', 'Requiem', 'Praetorial', 'Primordial', 'Purifying', 'Quantum', 'Cognizant', 'Devastating', 'Aquilan', 'Noble', 'Inanis', 'Visceral', 'Silvan', 'Vindictive', 'Veritable']

suffix_key_list = ['Fulminis', 'Ictus', 'Impetus', 'Ruptura', 'Secare', 'Terrae', 'Incendium', 'Voltum', 'Mortis', 'Magus', 'Nobilis', 'Ardens', 'Corpus', 'Cuspis', 'Decus', 'Dolorem', 'Draco', 'Ens', 'Ethereus', 'Fatum', 'Fulgur', 'Ignis', 'Inferni', 'Lux', 'Machina', 'Nex', 'Nimbus', 'Nox', 'Obscurum', 'Oculus', 'Os', 'Phasma', 'Pulvis', 'Sanguis', 'Scutum', 'Serpens', 'Silentium', 'Spiritus', 'Stella', 'Tenebris', 'Terra', 'Timor', 'Umbralis', 'Vates', 'Venenum', 'Vestigium', 'Victoria', 'Vigor', 'Vis', 'Vita', 'Vorago', 'Vortex', 'Aetas', 'Astra', 'Celeritas', 'Cognitus', 'Ferox', 'Fiducia', 'Fortis', 'Gravis', 'Honos', 'Inferus', 'Infinitus', 'Insidiae', 'Luxor', 'Majestas', 'Nebula', 'Nihilum', 'Noster', 'Nova', 'Praetor', 'Primus', 'Pulcher', 'Puritas', 'Quantum', 'Requiem', 'Sapiens', 'Solus', 'Somnium', 'Spes']
suffix_value_list = ['Bolt', 'Strike', 'Impetus', 'Rupture', 'Sever', 'Terra', 'Inferno', 'Voltage', 'Mortality', 'Mage', 'Noble', 'Ardent', 'Corpse', 'Cusp', 'Decoration', 'Dolor', 'Dragon', 'Essence', 'Ethereal', 'Fate', 'Lightning', 'Fire', 'Inferno', 'Light', 'Machine', 'Death', 'Nimbus', 'Night', 'Obscure', 'Ocular', 'Bone', 'Phasma', 'Powder', 'Blood', 'Shield', 'Serpent', 'Silentium', 'Spirit', 'Star', 'Darkness', 'Earth', 'Fear', 'Umbral', 'Vates', 'Venom', 'Trace', 'Victory', 'Vigor', 'Power', 'Life', 'Abyss', 'Vortex', 'Age', 'Star', 'Celerity', 'Cognizance', 'Ferocity', 'Fidelity', 'Fortitude', 'Gravity', 'Honor', 'Infernal', 'Infinity', 'Insidious', 'Luxury', 'Majesty', 'Nebula', 'Nihilum', 'Our', 'Nova', 'Praetor', 'Primus', 'Pulchritudinous', 'Purity', 'Quantum', 'Requiem', 'Sapience', 'Solus', 'Somnium', 'Hope']



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

    




