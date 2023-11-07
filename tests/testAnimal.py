import pytest
from src.harry_potter.create_wizard import CreateWizard



class Test:

    def test_gryffindor_1(self,monkeypatch):

        # simulate user inputs
        responses = iter(['A','B','A'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("gryffindor")
        assert result == "Acromantula"
    
    def test_gryffindor_2(self,monkeypatch):
        responses = iter(['A','A','A'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("gryffindor")
        assert result == "Phoenix"
    
    def test_ravenclaw_1(self,monkeypatch):
        responses = iter(['B','B','B'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("ravenclaw")
        assert result == "Eagles"

    def test_ravenclaw_2(self,monkeypatch):
        responses = iter(['B','A','A'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("ravenclaw")
        assert result == "Owls"

    def test_hufflepuff_1(self,monkeypatch):
        responses = iter(['A','B','B'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("Hufflepuff")
        assert result == "Nifflers"

    def test_hufflepuff_2(self,monkeypatch):
        responses = iter(['A','A','A'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("Hufflepuff")
        assert result == "Stags"

    def test_slytherin_1(self,monkeypatch):
        responses = iter(['B','B','B'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("Slytherin")
        assert result == "Snakes"

    def test_slytherin_2(self,monkeypatch):
        responses = iter(['A','B','A'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("Slytherin")
        assert result == "Thestrals"




    
    

