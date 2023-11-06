from src.harry_potter.create_wizard import CreateWizard
import pytest

class Tests:

    @pytest.fixture
    def create_wizard_instance(self):
        wizard = CreateWizard()
        return wizard
    
    def test_wizardNameGenerator(self, create_wizard_instance):
        wizard = create_wizard_instance
        result = wizard.wizardNameGenerator("some_preference")
        assert isinstance(result, str)

    def test_wizardNameGenerator_empty_preference(self, create_wizard_instance):
        wizard = create_wizard_instance
        preference = "" 
        result = wizard.wizardNameGenerator(preference)
        assert result == False

    def test_choose_house_invalid_preference(self, create_wizard_instance):
        wizard = create_wizard_instance
        preference = None
        result = wizard.chooseHouse(preference)
        assert result == False

    def test_choose_house_invalid_preference(self, create_wizard_instance):
        wizard = create_wizard_instance
        preference = None
        result = wizard.chooseHouse(preference)
        assert result == False
    
    def test_choose_house_valid_preference(self, create_wizard_instance):
        wizard = create_wizard_instance
        preference = "some_preference"
        result = wizard.chooseHouse(preference)
        assert isinstance(result, str)


    
    

    

    




    


    
    
    



    


    



        



        






