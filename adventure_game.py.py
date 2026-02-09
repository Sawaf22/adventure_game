import time
import random


def play_game():
    names1=("Omar", "Mohammed", "Abdelrahman", "Amr")
    #This is a variable for the friend of the player.

    names2=("Ali", "Abdullah", "Islam", "Ahmed")
    #This is a variable for the name of the doctor.

    names3=("Khaled", "Mustafa", "Seif", "Marwan")
    #This is a variable for the first villager in scenario 2

    names4=("Amer", "Tarik", "Hazem", "Sherif")
    #This is a variable of the Second villager in scenario 3.

    Predators1=("Wolf", "Fox", "Hyana")
    #This is a variable of the first predator the player and his friend face.

    Predators2=("Scorpion", "Snake", "Egyptian Cobra")
    #This is a variable for the second predator
    #whom the player killed to rescue his friend in scenario 4

    Predators3=("Gilla Monster", "Puma", "Ostrich")
    #This is a variable for the last predator the player and his friend face.

    Friend_name=random.choice(names1)

    Doctor_name=random.choice(names2)

    Villigar1_name=random.choice(names3)

    Villigar2_name=random.choice(names4)
    #This is the (random.choice) function of the names in the game.



    prd1_animals=random.choice(Predators1)

    prd2_reptiles=random.choice(Predators2)

    prd3_sleeping=random.choice(Predators3)

    #This is the (random.choice) function of the predators in the game.



    total_score= 0
    #This is the variable of the score in the game.

    def print_pause(*strings):
        for slp in strings:
            print(slp)
            time.sleep(2)
    #This function is related to the short delay between 
    #one sentence and another by using a time module that includes the 
    #(time.sleep) function.






    print_pause("You were in front of a desert and behind you there is a small"
                " village.")
    print_pause("You have a friend who is named {}.".format(Friend_name))
    
    print_pause("He told you that there is a pandemic in the village ,and"
    " you have food that is enough for two days only.")
        
    print_pause("You have 3 masks and 2 pairs of gloves, hoping that this can" 
                " save you from the pandemic of the village.")
    #This is the first step of the project which is 
    #"Describe what is happening."
    print_pause("Enter 1 to go to the village.")
    print_pause("Enter 2 to go to the desert.")
    print_pause("Which number do you want to choose?")


    def get_valid_input(prompt, valid_choices):
        while True:
            user_input = input(prompt).lower()
            if user_input in valid_choices:
                return user_input
            else:
                print_pause("Invalid input. Please try again.")
    #This function represents the checking of the validity of the input.
    def go_to_village():
        
        print_pause("You decided to go to the village , you have earned 10" 
                    " points!")
        print_pause("Your score now is:", total_score)

        print_pause("You take your bicycle and approach to the village. ")
        print_pause("Before entering the village, you start wearing a mask and"
                    " a pair of gloves from what you have. ")
        print_pause("The sky is darkened and you start looking for a safe"
                    " place to sleep, you hope that this safe place is a" 
                    " house.")
        print_pause("Unfortunately you didn't find what you want, you decide"
                    " to go back to the desert. ")
        print_pause("Enter 1 to go back to the desert.")
        print_pause("Enter 2 to stay in the village.")
        print_pause("Would you like to go back to the desert or stay in the"
                    " village?")
        


    chosen_num1 = get_valid_input("Enter 1 or 2: ", ["1", "2"])
    print_pause(chosen_num1)

    while ( chosen_num1 ) == "1" :
        total_score+=10
        go_to_village()

        chosen_num2 = get_valid_input("Choose 1 or 2 please: ", ["1", "2"])
        print_pause(chosen_num2)

        while (chosen_num2) == "1":
            
            total_score+=10
            print_pause("You decided to go back to the desert, you have earned"
                        " another 10 points!")
            print_pause("Your score now is:", total_score)

            print_pause("Congratulation!")
            print_pause("You start doing what you have decided.")
            print_pause("You take your bike and start going back to the"
                        " desert.")
            print_pause("You have reached the desert and found a good place to"
                        " sleep in.")
            print_pause("You wake up and meet your friend then repeating what"
                        " you did yesterday.")
            print_pause("He told you that he has a friend in the village who"
                        " is"
                        " very smart in medicine,"
                        " his name is {}.".format(Doctor_name))
            print_pause("He thinks that you can learn from him so you can do"
                        " anything to at least reduce the number of infected"
                        " people or eliminate this disease. ")
            print_pause("You liked his idea and you ask about his friend's"
                        " place in the village and then start moving to it.")
            print_pause("While moving to {}'s house, there was a villager who"
                        " notices that you are"
                        " new to the village.".format(Doctor_name))
            print_pause("He invites you with love and generosity.")
            print_pause("He wants to know any information about you and tells"
                        " you that his name is {}.".format(Villigar1_name))
            print_pause("He invites you to sleep in his house.")
            print_pause("Enter 1 to go to {}.".format(Doctor_name)) 
            print_pause("Enter 2 to sleep in his house.")
            print_pause("What do you want to do?")


            
            chosen_num3 = get_valid_input("Please input 1 or 2: ", ["1", "2"])
            print_pause(chosen_num3)

            while (chosen_num3) == "1":
                
                total_score+=15
                print_pause("You choosed to go to {}'s house, 15 points is"
                            " added to your score!".format(Doctor_name))
                print_pause("Your total score now is: ", total_score)

                print_pause("You told him: I'm so sorry I can't sleep in your"
                            " house because I'm going to"
                            " a doctor called {}.".format(Doctor_name))
                print_pause("He replied: Oh! I know him, he is a very"
                            " intelligent doctor. Why are you going to him?")
                print_pause("You answered: I want to learn from him. I'm sorry"
                            " I want to leave. ")
                print_pause("He said: Ok. Nice to meet you")
                print_pause("You start moving to"
                            " {}'s house.".format(Doctor_name))
                print_pause("You have found his house, and you knock the door"
                            " of it.")
                print_pause("He opened the door for you and invites you to his"
                            " office.")
                print_pause("You start knowing about each other and start"
                            " talking about the village's pandemic.")
                print_pause("He told you that the number of deaths is"
                            " increasing day after day.")
                print_pause("He talked about his research to find any solution"
                            " for this this pandemic for the last 2 weeks.")
                print_pause("You told him that this the reason for your visit"
                            " and that you want learn Medicine.")
                print_pause("He said that this is a very difficult thing to"
                            " finish in at least 2 months.")
                print_pause("you told that this is not a big problem for you,"
                            " as you love learning.")
                print_pause("You were starving as your food has finished, so"
                            " you ask for anything to eat.")
                print_pause("You stayed 2 months learning about medicine and"
                            " what is this pandemic and its characteristics"
                            " and reasons, about how vaccines work and how you"
                            " can treat an illnes and other medical concepts.")
                
                total_score+=20
                print_pause("Good job! You learned some good and important"
                            " principles in medical sciences, Your score"
                            " increased by 20 points!")
                print_pause("Total score:", total_score)

                print_pause("You and {} spent another month learning and"
                            " researching to find a vaccine for"
                            " the disease.".format(Doctor_name))
                print_pause("In this 3 months and half, you didn't go out of"
                            " the house, as this is very dangerous, this is"
                            " one of the benefits you gained at the first day"
                            " in {}'s house.".format(Doctor_name))
                print_pause("Finally and fortuntely you and Ali finished a"
                            " model of the vaccine but you to experiment it.")
                
                total_score+=25
                print_pause("Victory!! You have found a model of a vaccine.")
                print_pause("Your score:", total_score)

                print_pause("Good work!!")
                print_pause("After year and half, the pandemic no longer"
                            " exists!!")
                
                total_score+=35
                print_pause("Mission completed!!!")
                print_pause("Your final score is: ", total_score)
                break

            if total_score>=100:
                print_pause("Congratulations!You have won the game!")
                


                play_again = get_valid_input("Do you want to play again?"
                                             " (yes/no): ", ["yes", "no"])

                if play_again.lower() == "yes":
                    play_game()
                    chosen_num1="0"
                    chosen_num2="0"
                    chosen_num3="0"
                elif play_again.lower() == "no":
                    print_pause("Thank you for playing!")
                    chosen_num1="0"
                    chosen_num2="0"
                    chosen_num3="0"
                
            #Senario 1        


            while (chosen_num3) == "2":
                
                total_score-=10
                print_pause("Oh no! You choosed to sleep in his house.")
                print_pause("Unfortunately, this is not a very good choice,"
                            " it resulted in losing 10 points!")
                print_pause("You total score now: ", total_score)

                print_pause("You decided to sleep in {}'s house, and tommorow"
                            " you can move to"
                            " {}'s house".format(Doctor_name,Villigar1_name))
                print_pause("The next day, you start moving, but Khaled"
                            " refused and start to threaten you!You are"
                            " locked in his home!")
                
                total_score-= 2
                print_pause("Unfortunately, you have lost 2 points.")
                print_pause("Your score now is :", total_score)

                print_pause("You were starving, and {} is mistreating you, so"
                            " he didn't give"
                            " you any food.".format(Villigar1_name))
                print_pause("You start planning to escape from his house, but"
                            " you have a high opportunity to be infected by"
                            " the disease.")
                print_pause("You start the first try of escaping."
                            " Fortunately, you escaped.")
                
                total_score+= 7
                print_pause("Good thinking! You have earned 7 points!")
                print_pause("Your total score now:", total_score)

                print_pause("You start going to {}'s house, and you start"
                            " feeling something strange, it is a very severe"
                            " pain in your eye.".format(Doctor_name))
                print_pause("After 2 days, your health condition is worsened"
                            " badly.")
                print_pause("You start feeling with a strong pain in your"
                            " brain, and now you are dead!")
                
                total_score-=20
                print_pause("Oh no! This is a bad ending! You have lost"
                            " 20 points!!")
                print_pause("Your final score: ", total_score)
            
                if total_score<=0:
                    print_pause("I'm so sorry to tell you that, you"
                                " have lost!")
                    
                    play_again = get_valid_input("Do you want to play again?"
                                                 " (yes/no): ", ["yes", "no"])

                    if play_again.lower() == "yes":
                        play_game()
                        chosen_num1="0"
                        chosen_num2="0"
                        chosen_num3="0"
                    elif play_again.lower() == "no":
                        print_pause("Thank you for playing!")
                        chosen_num1="0"
                        chosen_num2="0"
                        chosen_num3="0"
            #Senario 2
            
        while(chosen_num2)=="2":

            total_score+=5
            print_pause("You choosed to stay in the vilage , this may be a"
                        " good choice. You gained 5 points.")
            print_pause("Your total score now is:", total_score)

            print_pause("You decided to stay in the village.")
            print_pause("Somone called {} invited you in his house to sleep"
                        " in it.".format(Villigar2_name))
            print_pause("You wake up and start thinking and planning for"
                        " how to make this village safe.")
            print_pause("Your food start finishing , and you understanded"
                        " that going out of your house can threaten your"
                        " life!")
            print_pause("You asked {} for some food but he was very poor and"
                        " his food's quntity"
                        " is very small.".format(Villigar2_name))
            print_pause("You decided to do a suicide mission, to go out"
                        " to bring some food, but wait you don't even no"
                        " what is the currency of the  village or how they"
                        " buy and sell!")
            print_pause("{} told you that the system of buying and selling"
                        " in the village is the barter system, for example ,"
                        " I give you a tennis ball and you give"
                        " me cola!".format(Villigar2_name))
            print_pause("{} gives you some rocks to bring"
                        " some food.".format(Villigar2_name))
            print_pause("You start go out and go to a shop to buy anything"
                        " to eat, but the seller's condition is very strange"
                        " for you, he might be  ill!")
            print_pause("You become frightend as he may be infected with the"
                        " pandemic.")
            print_pause("Fortunately, you got the food you want from the"
                        " seller.")

            total_score+=10
            print_pause("Excellent! You have complete the suicide mission!")
            print_pause("Your score now is: ", total_score)

            print_pause("You arrived {}'s house and knocked the door but"
                        " nobody answers you, you thought that Amer may"
                        " be sleeping right now.".format(Villigar2_name))
            print_pause("Fortunately, the window of {}'s bedroom is opened ,"
                        " so you can cut doubt with certainty and see if he"
                        " is sleeping or not, you found him sleeping on the"
                        " floor in a very strange way!He is certainly"
                        " dead!".format(Villigar2_name))
            print_pause("You remembered that {}'s condition in the first time"
                        " you saw him, was the same as the seller's condition"
                        " , you start to be sure that Amer is dead due to the"
                        " pandemic!".format(Villigar2_name))
            print_pause("Most likely you are infected, and jumping through"
                        " the house is extremely difficult.")
            print_pause("The only solution is to stay out, so you decided to"
                        " do that.")

            total_score-=3
            print_pause("Oh! You have lost 3 points!"
                        " Your score now:" , total_score)
            print_pause("You think that you should look for any doctor who"
                        " you could learn from him as your task is to get rid"
                        " from the pandemic, and you decided to take the risk"
                        " and do that.")
            print_pause("You spent 3 days looking for any doctor and a"
                        " villager told you that there is a clever doctor"
                        " called {} is found in a"
                        " certain place.".format(Doctor_name))
            print_pause("So you follow his instructions so you can reach {}'s"
                        " house but unfortunately, you were very starving and"
                        " you start feeling the same strange condition and"
                        " you don't have anything so you can buy"
                        " any food.".format(Doctor_name))
            print_pause("Finally, after five days of searching you have found"
                        " {}'s house! You recognized that he is very near to"
                        " the desert.".format(Doctor_name))
            print_pause("You were very tired and before the first nock of the"
                        " door you are fainted!")
            
            total_score-=5
            print_pause("Very sad! Your score decreased by 5 points!")
            print_pause("Your score now is: ", total_score)

            print_pause("After 35 minutes, {} opens the door and is"
                        " dumbfounded, he finds"
                        " a fainted body!".format(Doctor_name))
            print_pause("He took this body quickley, enter his house and"
                        " tryed to do anything so he can wake up but all"
                        " attempts failed.")
            print_pause("In his own way, he realized that this body was dead!")

            total_score-=25
            print_pause("Your final score is :", total_score)
            

            if total_score<=5:
                print_pause("Oh no! You have lost the game!")
                
                play_again = get_valid_input("Do you want to play again?"
                                             " (yes/no): ", ["yes", "no"])

                if play_again.lower() == "yes":
                    play_game()
                    chosen_num1="0"
                    chosen_num2="0"
                    chosen_num3="0"
                elif play_again.lower() == "no":
                    print_pause("Thank you for playing!")
                    chosen_num1="0"
                    chosen_num2="0"                
                    chosen_num3="0"
        #Senario 3    


    while (chosen_num1)=="2":
        
        total_score+=10
        print_pause("You choosed number 2 which means that you want to go to"
                    " the desert, good choice!")
        print_pause("Your total score now: ", total_score)

        print_pause("You decided to go to the desert and {}"
                    " go with you.".format(Friend_name))
        print_pause("He told you: Our mission is to prevent the pandemic"
                    " from being in the desert.")
        print_pause("You asked: What is our plan?")
        print_pause("He answered: Our plan is to go a hospital in the desert"
                    " that has the secret solution for this for what we want"
                    " but this is very risky mission.")
        print_pause("You asked: Why it is very risky??")
        print_pause("{} answered: There is 2 reasons: the first one is that"
                    " the solution is very secret and the second one is that"
                    " our road to this hospital is very"
                    " dangerous.".format(Friend_name))
        print_pause("He completed: It is full of predators and we may get"
                    " lost easily.")
        print_pause("You said: No problem, you get relaxation by"
                    " getting tired.")
        print_pause("You and {} start moving to this"
                    " hospital.".format(Friend_name))
        print_pause("On the road to it, you faced the first predator but {}"
                    " killed it easily. It was a"
                    " {}!".format(Friend_name,prd1_animals))
        print_pause("The night comes and you have to find a safe place to"
                    " sleep, fortunately you find it.")
        print_pause("You wake up and realized that {} is in a battle with a"
                    " thief who is most likely from the"
                    " bandits.".format(Friend_name))
        print_pause("You tried doing anything to help him and fortunately,"
                    " the obnxious bandit has escaped and Omar was wounded"
                    " badly.")
        print_pause("You start stopping the bleeding till reaching this"
                    " difficult hospital.")
        print_pause("You continue walking and you noticed a {} tries to get"
                    " close to {} and harm him. You of course killed"
                    " it.".format(prd2_reptiles,Friend_name))

        total_score+=12
        print_pause("Nice! You rescue your friend from poisonous reptile!You"
                    " winned 12 point!")
        print_pause("Your score now is: ", total_score)

        print_pause("After that there was a downhill which you should go down"
                    " through it.")
        print_pause("While you are going down, you were injured in your leg,"
                    " but thank god, it was not a very bad danger.")
        print_pause("You faced another predatator which is a {}, but it was"
                    " sleeping so you passed it"
                    " peacefully.".format(prd3_sleeping))
        print_pause("{} told: We are very neer to the hospital, an hour"
                    " passed and we will be sleeping"
                    " in it.".format(Friend_name))
        print_pause("Finally, you arrived to this hospital.")
        
        total_score+=25
        print_pause("Hoooh! You reached to the hospital and there is only one"
                    " step remains! You have gained 25 points!")
        print_pause("Your total score now is: ", total_score)

        print_pause("{}'s wound and your small leg injury was treated. You"
                    " and the staff of the hospital start planning for how to"
                    " rescue the desert from the disease.".format(Friend_name))
        print_pause("This hospital is near to a city which is the source of"
                    " the pandemic, and it manufacture a vaccine that can"
                    " treat this disease by a very secret way.")
        print_pause("The hospital is forbidded to sell any version of the"
                    " vaccine -most likely- for no reason.")
        print_pause("Selling this vaccine means getting rid of the disease,"
                    " and that you and {} don't have to do the mission that"
                    " is the reason for all this journey.".format(Friend_name))
        print_pause("After three months of stay in this hospital, the"
                    " vaccine is selled finally.")
        print_pause("{} asked if he can get a model of the vaccine to a near"
                    " village, and the hospital refused till getting sure"
                     " that it works well.".format(Friend_name))
        print_pause("After 4 months, the effect of the vaccine is beginning"
                    " to be noticed, so you and {} took a model of the"
                    " vaccine and start moving to"
                    " the village.".format(Friend_name))
        print_pause("Finally, you arrived to the village after a very tiring"
                    " journey, and give this model to a clever doctor called"
                    " {}, {}'s friend.".format(Doctor_name,Friend_name))

        total_score+=20
        print_pause("Good job!! You have earned 20 points!")
        print_pause("Your score is: ", total_score)

        print_pause("He tested this vaccine, and experiment it. He was"
                    " astonished by its results, so he made an appointment"
                    " for taking the vaccine to the villagers immediately.")
        print_pause("After a year and half, the epidemic is over!")

        total_score+=35
        print_pause("Finally!You have reached to the end!")
        print_pause("Your final score is:", total_score)

        if total_score>=100:
            print_pause("Good job! You have won the game")
                                
            play_again = get_valid_input("Do you want to play again? (yes/no)"
                                         ": ", ["yes", "no"])

            if play_again.lower() == "yes":
                play_game()                    
                chosen_num1="0"
                chosen_num2="0"
                chosen_num3="0"
            elif play_again.lower() == "no":
                print_pause("Thank you for playing!")
                chosen_num1="0"
                chosen_num2="0"
                chosen_num3="0"
    #Senario 4  
play_game()