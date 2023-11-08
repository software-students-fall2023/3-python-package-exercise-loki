from src.harry_potter.create_wizard import CreateWizard

def test_candy_always_passed_num():
    assert(CreateWizard().chooseCandy("Hello World") == False)

def test_candy_list_length():
    assert(len(CreateWizard().chooseCandy(10)) == 10)

def test_candy_list_length_zero():
    assert(len(CreateWizard().chooseCandy(0)) == 0)

#testing the function operates as expected for very large values
def test_candy_list_length_10000():    
    assert(len(CreateWizard().chooseCandy(10000)) == 10000)

##*********************##

def test_fightingSpell_always_passed_num(): 
    assert(CreateWizard().generateFightingSpell("hello World") == False)

def test_fightingSpell_list_length(): 
    assert(len(CreateWizard().generateFightingSpell(10)) == 10)

def test_fightingSpell_list_length_zero():
    assert(len(CreateWizard().generateFightingSpell(0)) == 0)

#test the list generation works for very large values
def test_fightingSpell_list_length_10000(): 
    assert(len(CreateWizard().generateFightingSpell(10000)) == 10000)

#checks that the internal lists are all four elements long
def test_fighting_Spell_Internal_list(): 
    temp = CreateWizard().generateFightingSpell(10) 

    lenFour = True
    for i in range(len(temp)): 
        if (len(temp[i]) == 4): 
            lenFour = True
        else: 
            lenFour = False
            break
    
    assert(lenFour)
         
           


    




    

    

 

     


