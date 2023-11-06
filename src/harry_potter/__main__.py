from create_wizard import CreateWizard

def main():
  wizard_instance = CreateWizard()
  print(wizard_instance.chooseHouse("Griffindor"))
  
if __name__ == '__main__':
  main()