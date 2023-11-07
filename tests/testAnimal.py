import pytest
from src.harry_potter.create_wizard import CreateWizard



class Test:

    def test_gryffindor(self,monkeypatch):

        # simulate user inputs
        responses = iter(['A','B','A'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses) )
        wizard = CreateWizard()
        result = wizard.chooseAnimal("gryffindor")
        assert result == "Acromantula"

