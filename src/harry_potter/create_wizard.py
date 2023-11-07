



class CreateWizard:
   
    # type indicates good or bad
    def wizardNameGenerator(self,type):
        pass

    def pickName(self):
        pass

    def chooseCandy(self):
        pass

    def chooseAnimal(self,house):
       # A : 1 B: 0 , max total : 3. 
        dict = [["Lion","Hippogriffs", "Acromantula","Phoenix"],
               ["Badgers" , "Nifflers", "Honeybees","Stags"],
               [ "Eagles", "Ravens", "Owls","Phoenixes"],
               ["Snakes", "Basilisks", "Thestrals","Nagini"]]
          # check data type 
        if(not isinstance(house,str)):
            print("please enter a string")
            return "please enter a string"

        lowercase = house.lower()
        # check if string is empty
        if(len(lowercase)== 0):
            print("empty, try again")
            return "empty"
        
        # check if entered input belongs to one of the houses
        if(lowercase != "gryffindor" and lowercase != "hufflepuff" and lowercase != "ravenclaw" and lowercase != "slytherin"):
            print("enter a correct house")
            return "enter a correct house"

        points = 0
        if lowercase == "gryffindor":
           
            q1 = input("When faced with a dangerous or challenging situation, A) do you tend to act  quickly and impulsively to protect others or B) do you carefully plan your actions to minimize risk?(A/B)")
            
            while(not (q1 == "A" or q1 == "B")):
                q1 = input("Please only enter either A or B : ")
                
            
            q2 = input("Which qualities do you admire most in a person: A) courage, bravery, and a willingness to stand up for what's right, or B) intelligence, knowledge, and a love of learning?(A/B)")
            
            while(not (q2 == "A" or q2 == "B")):
                q2 = input("Please only enter either A or B : ")
                

            q3 = input("Imagine you're in a situation where you have to choose between a path that is A) safe but morally questionable and a B) riskier path that is ethically sound. Which option would you be more inclined to choose?(A/B)")
            while(not (q3 == "A" or q3 == "B")):
                q3 = input("Please only enter either A or B : ")
                

            if q1 == "A" :
                points += 1
            if q2 == "A" :
                points += 1
            if q3 == "A" :
                points += 1
            if q1 == "B" :
                points += 0
            if q2 == "B" :
                points += 0
            if q3 == "B" :
                points += 0
            
            #print(points)
            print("Your animal is : " ,dict[0][points])
            return dict[0][points]
       
        elif lowercase == "hufflepuff":
           q1 = input("When working on a group project, do you A) find yourself prioritizing cooperation and ensuring everyone's contributions are valued, or B) are you more focused on achieving the best possible outcome, even if it means taking charge and making tough decisions?(A/B)")
           
           while(not (q1 == "A" or q1 == "B")):
                q1 = input("Please only enter either A or B : ")
           
           q2 = input("Which qualities do you value most in a friend: A) loyalty, kindness, and a strong sense of fairness, or B) intelligence, creativity, and a thirst for knowledge?(A/B)")
           while(not (q2 == "A" or q2 == "B")):
                q2 = input("Please only enter either A or B : ")
           
           q3 = input("Imagine you have a choice between A) joining a club or organization that focuses on charitable work and helping those in need, and another that offers opportunities for personal achievement and recognition. Which option would you be more drawn to?(A/B)")
           while(not (q3 == "A" or q3 == "B")):
                q3 = input("Please only enter either A or B : ")
           
           if q1 == "A" :
               points += 1
           if q2 == "A" :
               points += 1
           if q3 == "A" :
               points += 1
           if q1 == "B" :
               points += 0
           if q2 == "B" :
               points += 0
           if q3 == "B" :
               points += 0
           
           
           print("Your animal is : " ,dict[1][points])
           return dict[1][points]
       
        elif lowercase == "ravenclaw":
           q1 = input("When faced with a difficult problem, do you A) find yourself relying on logic, research, and analytical thinking to solve it, or B) are you more inclined to trust your instincts and intuition?(A/B)")
           while(not (q1 == "A" or q1 == "B")):
                q1 = input("Please only enter either A or B : ")
           
           q2 = input("What type of books or subjects do you enjoy reading about the most: A) topics that expand your knowledge, explore the mysteries of the universe, or B) delve into imaginative worlds and creative pursuits?(A/B)")
           while(not (q2 == "A" or q2 == "B")):
                q2 = input("Please only enter either A or B : ")

           q3 = input("If you had to choose between a social gathering with friends or spending a quiet evening exploring a new area of knowledge or a creative project, which option would you be more likely to pick? (A/B)")
           while(not (q3 == "A" or q3 == "B")):
                q3 = input("Please only enter either A or B : ")
           
           if q1 == "A" :
               points += 1
           if q2 == "A" :
               points += 1
           if q3 == "A" :
               points += 1
           if q1 == "B" :
               points += 0
           if q2 == "B" :
               points += 0
           if q3 == "B" :
               points += 0
           
        
           print("Your animal is : " ,dict[2][points])
           return dict[2][points]

        elif lowercase == "slytherin":
           q1 = input("When striving to achieve your goals, are you A) more likely to use your ambition, resourcefulness, and determination to succeed, or B) do you prioritize fairness, collaboration, and the greater good? (A/B)")
           while(not (q1 == "A" or q1 == "B")):
                q1 = input("Please only enter either A or B : ")
           
           q2 = input("Which qualities do you find most admirable in a leader: A)  a strategic mind, the ability to make tough decisions, and a strong desire for success, or B) empathy, compassion, and a dedication to equality and justice? (A/B)")
           while(not (q2 == "A" or q2 == "B")):
                q2 = input("Please only enter either A or B : ")

           q3 = input("If you had the choice between A) joining a group that values competition, individual success, and the pursuit of power, or B) one that focuses on cooperation, community, and social justice, which option would you be more inclined to choose? (A/B)")
           while(not (q3 == "A" or q3 == "B")):
                q3 = input("Please only enter either A or B : ")

           if q1 == "A" :
               points += 1
           if q2 == "A" :
               points += 1
           if q3 == "A" :
               points += 1
           if q1 == "B" :
               points += 0
           if q2 == "B" :
               points += 0
           if q3 == "B" :
               points += 0
           
           print("Your animal is : " ,dict[3][points])
           return dict[3][points]


    def chooseHouse(self):
        pass



    




