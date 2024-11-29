import time
#time makes it where it can pause the program for "x" seconds which is useful if you want the user to wait
import random
#random makes it where the program chooses something at random. I used random so the program picks a random item off the goodies_list and for other uses
import threading
#threading makes it where the program can run different things at the same time

Splash = """
                                                      _____ _ _ _      _____                 _ 
                                                     / ____(_) | |    |  __ \               | |
                                                    | (___  _| | | __ | |__) |___   __ _  __| |
                                                     \___ \| | | |/ / |  _  // _ \ / _` |/ _` |
                                                     ____) | | |   <  | | \ \ (_) | (_| | (_| |
                                                    |_____/|_|_|_|\_\ |_|  \_\___/ \__,_|\__,_|
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXNWMMMMMMMMMMMMMMMMMMMMMMMWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXK00KKXNWWXxco0WMMMMMMMMMMMMMMMMMMMMMMNOd0XKK0KKXXXXNXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKO0NMWWX0kdlcc:;:::codkOo:kWMMMMMMMMMMMMMMMMMMMMMMMNxldkxdlodxolxOkkxkOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:dXXOdc:::;;::;::;;::;;,cKMMMMMMMMMMMMMMMMMMMMMMMWKxoodoolodxlcxkkxdxxkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOccdl::;;::;;::;;;;;;;;,,;xWMMMMMMMMMMMMMMMMMMMMMMNOxxdddooooo:cxkkxoolo0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0c,,;::;;:;;,;,,,'''''''',dNMMMMMMMMMMMMMMMMMMMMMMKkxxdxxxxdddl:oxxkOOOkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:,,;;;,,'''',,,'',,,,,'',oNMMMMMMMMMMMMMMMMMMMMMW0xkxdddoooddooOKXNWMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc,,''',,,,,,,,,,,,,,,,,,'oKWMMMMMMMMMMMMMMMMMMMWXkxkkkxdoxOKK0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOc,'',,,,,,,,'''''''.'',,,ckKXNWWWMMMMMMMMMMMMMMWKkkkkkxdxKWMN0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK0x;',,,,''''...........'',,cxkO0KKXNWMMMMMMMMMMMMW0kkkkkxd0WMMN0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0000Od;',''......'''''''..'',,;okkkOO000KXNWMMMMMMMMWKdlxkkxdxXMMMN0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXK0OkkkOOOko;,,''..'''',,,,,,,'',,,;lxkkkkkkkOO00KXNWWWWWXkolccloddOWMMMNOKMMMMMMMMMMMMMMMMMMMWX0OO0KNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkkkkkOOO00Ox:,,,,'',,,,'''''''',,,:oxkkkkkkkkkkkkOOO00K00Oxc;lolc:lKMMMMW0KMMMMMMMMMMMMMMMMMMNkoccc:cxXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkxkkkkkkkkkO0Oo;,,,,,''''........'';dkkOO000Okkkkkkkkkkkkkkkko:::cloOWMMMMW00MMMMMMMMMMMMMMMMMMKollc;''cKMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWX0kddxkkkkkkkkkk0Okdl:,''.............':xkkkkkOOOOkkkkkkkkkkkkkkkxlclc:xNMMMMMM00WMMMMMMMMMMMMMMMMMXdlol;'':0WMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWK0XKxodxkkkkkkkkOOOkkkxc'..',,,,,,:l::cldkkkkkkkOOOkkkkkkxxxxxxxxxxo:cddkNMMMMMMKONMMMMMMMMMMMMMMMMMNklloc;,c0MMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXOKWW0dodxkkkkkkkkOkxddxoc:codooo::oxocldxkkkkkkkkOOOkxxxdddkOkxxxddxxodx0WMMMMMMNOKMMMMMMMMMMMMMMMWKxc::lolokXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMW0ONMMW0dodddddxkkkkkxdooddocdkoclc,;ol;:oxkkkkkkkkkOOkxdodkKNWWNNNNNNWNKKNMMMMMMMW00WMMMMMMMMMMMMMNklc:,':olokXWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXOKWMMMNOooooodxkkkkxdoooool;:do:cl;,ldlcodxxkkkkkkkkkkdox0NMMMMMMMMMMMMMMMMMMMMMMMXOXMMMMMMMMMMMMNkooooc,;ool;lKMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNOONMMMMWOdoodxxkkkkxdooooooolloooooc;lddoooodxkkkkkkkkxdoxXMMMMMMMMMMMMMMMMMMMMMMMMW00WMMMMMMMMMMWKdool:,,:ooo::OMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNKkdkNMMMMNkodxxkkkkkxdoooooooooooooooo:;looooooxkkkkkkkxdooxXMMMMMMMMMMMMMMMMMMMMMMMMMNOKMMMMMMMMMWKxool;'',coooc;OMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWKkdookNMMMW0ddxkkkkkOkdoooooooddooooooool:;loooodxkkkkkkxxoood0WMMMMMMMMMMMMMMMMMMMMMMMMMKOXMMMMMMMMNkooo:''',loooc;kMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMW0doooxKWMMN0ddxkkkkO00xoooooodkKK0Okxxxxxkkxk0OxoxkkkkkO0KOdoooxXMMMMMMMMMMMMMMMMMMMMMMMMMWKONMMMMMMWKdooc,''',coooc;dNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNkoodkXWMWXkddxkkkOKKOxoooooxOXWMMMWWWNNNWWWMMMXxdxkkkkkKWWXkooodONMMMMMMMMMMMMMMMMMMMMMMMMMWKONMMMMMW0doo:'''',coooc,c0WMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXkdOKNMWN0xddxkO0XXKkdooodx0XWMMMMMMMMMMMMMMMMMXkdkkkkk0WMMWKxoood0WMMMMMMMMMMMMMMMMMMMMMMMMMWKOXMMMMW0dooc,''',cooo:,:dKWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMX0XWMWN0kddxkOKNNKkdooodkKNMMMMMMMMMMMMMMMMMMMMNOxkkkk0NMMMMW0doooxXMMMMMMMMMMMMMMMMMMMMMMMMMMWXOKWMMMXxool,''',coooc,;oxXMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWNWMNKkxxkk0XNWXOdoodxOXWMMMMMMMMMMMMMMMMMMMMMMWOxkkkkXWMMMMMNOdoodONMMMMMMMMMMMMMMMMMMMMMMMMMMMN00XWMNOooo:''',coooc,;ldkNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWXkxxkk0XWWNOdoodx0NWMMMMMMMMMMMMMMMMMMMMMMMMW0xkkk0NMMMMMMWKxooodONMMMMMMMMMMMMMMMMMMMMMMMMMMMWX00XKocool;''':oooc,,odldXWMMMMMMMM
MMMMMMMMMMMMMMMMMMMNOxkkOXWMMW0dood0NWMMMMMMMMMMMMMMMMMMMMMMMMMMNOxkkk0WMMMMMMMXkoooodONMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOo,,;;;,''';lool,'oOo:oXMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKkk0NWMMMMNOddOWMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxxkkkKWMMMMMMMXxoooookNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd:,,''''';loooookXXO0NMMMMMMMM
MMMMMMMMMMMMMMMMMMMMW0OXMMMMMMMWKxONMMMMMMMMMMMMMMMMMMMMMMMMMMMNOddxkk0WMMMMMMMNOdodxkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxc:;;:ccloood0WMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWK0NMMMMMMMMW0kXMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkdxk0XWMMMMMMMWKxd0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxllloooooooodOWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMW0ONMMMMMMMMMXkONMMMMMMMMMMMMMMMMMMMMMMMMMMMMKkkXWMMMMMMMMMNkd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxooooooooooooONMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNOONMMMMMMMMMW0dONMMMMMMMMMMMMMMMMMMMMMMMMMMW0x0WMMMMMMMMMWKdkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxooooooooooooxXMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXkkNMMMMMMMMMMXxdONMMMMMMMMMMMMMMMMMMMMMMMMMWOxKWMMMMMMMMMXkdKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKdoooooooooooooONMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXkkXMMMMMMMMMMWOddONMMMMMMMMMMMMMMMMMMMMMMMMNkxXMMMMMMMMMW0dxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOooooooooooooooxXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKxkKWMMMMMMMMMMKxodONMMMMMMMMMMMMMMMMMMMMMMMKxkXMMMMMMMMWKxokNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXxloooooooooloookXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMW0xx0NMMMMMMMMMMNkoodONMMMMMMMMMMMMMMMMMMMMMW0xkKWMMMMMMMW0doONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdooooooooooooooxXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMW0dxOXMMMMMMMMMMWKkxdxKWMMMMMMMMMMMMMMMMMMMMWOxkKWMMMMMMMWKdd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkoooooooloooooooxXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNKkk0NWMMMMMMMMMMWXkodkKNWMMMMMMMMMMMMMMMMMWKkk0WMMMMMMMWKxdkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNK0dco0KKK0KK0xloONMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNkdxk0KNWMMMMMMMMXxddodxONMMMMMMMMMMMMMMMMMWOxk0KNWMMMMWXOkkkOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl;xWMMMMMMM0c:OWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXOxxxxxOXWMMMMMMMWXXXKKKKNMMMMMMMMMMMMMMMMMW0kkOOKNMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,,l0WMMMMMMXl':ok0XWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWWWNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xooONMMMMMNkddxxOKWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
print (Splash)

health = 500 #this is the starting health for the player

goodies_list = [' jade', ' porcelain', ' tea', ' ginger spices', ' cinnamon spices'] #this is all the goodies the player has in the beginning

def ending(): #if the player beats the game, this screen pops up
    print("\033[1;32;m")
    print("After lots of hard work and determination...")
    input("")
    print("And after a long time...")
    input("")
    print("\033[1;32;40m You made it to Europe!")
    input("\033[1;32;m")
    print("You can now give all the reaminging cargo you have:" + str(goodies_list) + " to other people in Europe!")
    input("")
    print('Good job ' + username + "!")
    input("")
    print("Thank you for your determination and grit you endured while crossing the Silk Road.")
    input("")
    input("Press Enter to quit the program.") #smooth way to end the program

def youlost_health(): #this is if the player looses the game by loosing all health, this part shows

    print(" You've lost all your health")
    input("")
    print("You ended with:")
    input("")
    print("Health: " + str(health) + ".")
    print("Cargo: " + str(goodies_list) + ".")

def youlost_cargo(): #this is if the player looses the game by loosing all cargo, this part shows

    print(" You've lost all your cargo")
    input("")
    print("You ended with:")
    input("")
    print("health: " + str(health) + ".")
    print("Cargo: None left.")

def multi_question1(): 
#multiple choice question number 1
    global health
    #global makes the health variable to work correctly for the questions
  
    print("\u001b[33mQuestion #1: Which is a popular Cantonese dim sum dish made from shrimp?\u001b[0m\n") #prints the question and below it prints the options. The stuff before and after the question is to change the colour of the text.

    print("1. Har Gow")
    print("2. Xianglongbao")
    print("3. Juk Gow")
    print("")
    #this prints the options to the question above
    input("")
    response1 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) #\n makes the user response go under this question

    if response1 == 1: #if the user selects the first option
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question2() #brings the player to the next question

    elif response1 == 2: #if the user selects the second option
        input("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
        input("")
        print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\u001b[37m \u001b")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question2() #brings the player to the next question
  
    elif response1 == 3: #if the user selects the third option
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
        input("") 
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        input("")
        print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
        print("\u001b[37m \u001b") #this changes the text to grey
        print("")
        input("")
        multi_question2() #brings the player to the next question

    
    else: #if the user did not click any of the options
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        time.sleep(1)
        multi_question1()

def multi_question2():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #2: Which of the following is a sweet Cantonese dessert soup?\u001b[0m")
    input("")
    print("")
    print("1. Wonton Soup")
    print("2. Sweet Almond Soup")
    print("3. Congee Soup")
    print("")
    input("")
    response2 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response2 == 1:
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour
        input("")
        print(" Sweet Almond Soup is a creamy dessert soup made from ground almonds. It is a soothing treat often served warm or chilled.")
        input("")    
        health = health - 100 #the player looses 100 health
        print(" Oh no! A robber cut you with a sword! Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\u001b[37m \u001b")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question3() #brings the player to the next question

    
    elif response2 == 2:
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Sweet Almond Soup is a creamy dessert soup made from ground almonds. It is a soothing treat often served warm or chilled.")
        input("")
        print(" You successfully fended off a thief. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\u001b[37m \u001b")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question3() #brings the player to the next question

    elif response2 == 3:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print(" Sweet Almond Soup is a creamy dessert soup made from ground almonds. It is a soothing treat often served warm or chilled.")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
        print("\u001b[37m \u001b")
        input("")
        multi_question3() #brings the player to the next question

    
    else:
        time.sleep(0.5) #this makes the program sleep for 2 seconds before printing something
        print(" This is not a valid choice, please try again")
        time.sleep(1)
        print("")
        multi_question2()

def multi_question3():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    time.sleep(1)
    print("")
    print("\u001b[33mQuestion #3: What is Char Siu?\u001b[0m")
    input("")
    print("")
    print("1. BBQ Pork")
    print("2. Peking Duck")
    print("3. Pork Ribs")
    print("")
    input("")
    response3 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response3 == 1:
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Char Siu is Cantonese-style barbecued pork, characterized by its sweet and savory marinade and its reddish hue.")
        input("")
        print("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question4() #brings the player to the next question

    
    elif response3 == 2:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print(" Char Siu is Cantonese-style barbecued pork, characterized by its sweet and savory marinade and its reddish hue.")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
        print("\033[1;32;m")
        input("")
        multi_question4() #brings the player to the next question

    elif response3 == 3:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour   
        input("")
        print(" Char Siu is Cantonese-style barbecued pork, characterized by its sweet and savory marinade and its reddish hue.")
        input("") 
        health = health - 100 #the player looses 100 health
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question4() #brings the player to the next question
            
    else:
        time.sleep(0.5) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        time.sleep(2)
        multi_question3()

def multi_question4():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #4: Which is NOT a dim sum dish?\u001b[0m")
    input("")
    print("1. Xianlongbao")
    print("2. Bak Kut Teh")
    print("3. Shumai")
    input("")

    response4 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response4 == 1:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print(" Bak Kut Teh, which means meat bone tea, is a flavorful broth with pork ribs and herbs, and it's primarily from Fujian and Singaporean cuisine, not Cantonese.")


        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
        print("\033[1;32;m")
        input("")   
        multi_question5() #brings the player to the next question
    
    elif response4 == 2:
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        print("")
        input("")
        print(" Bak Kut Teh, which means meat bone tea, is a flavorful broth with pork ribs and herbs, and it's primarily from Fujian and Singaporean cuisine, not Cantonese.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question5() #brings the player to the next question

    elif response4 == 3:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour   
        input("") 
        print(" Bak Kut Teh, which means meat bone tea, is a flavorful broth with pork ribs and herbs, and it's primarily from Fujian and Singaporean cuisine, not Cantonese.")
        input("")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a sword! Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question5() #brings the player to the next question
            
    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question4()

def multi_question5():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #5: Which dish is a steamed sponge cake, known for its light and fluffy texture?\u001b[0m")
    input("")
    print("1. Sponge Cake")
    print("2. Baozi")
    print("3. Ma Lai Go")
    input("")
    response5 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response5 == 1:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print("Ma Lai Go is a traditional Cantonese steamed sponge cake, often found in dim sum restaurants. Its soft, airy texture and caramel-like flavor make it a favorite among many.")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        
        if len(goodies_list) == 0: #if the goodies_list is empty
            youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

        else: #if the player still has some health and cargo left
            print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
            print("\u001b[37m \u001b")
            multi_question6()

    
    elif response5 == 2:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink and the part where it says [31m parts of this line is to change the text colour    
        input("")
        print("Ma Lai Go is a traditional Cantonese steamed sponge cake, often found in dim sum restaurants. Its soft, airy texture and caramel-like flavor make it a favorite among many.")        
        input("")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
                
        if health == 0: #if the player looses all their health, the game ends
            youlost_health() #brings player to youlost_health (they lost the game because they lost all health)

        else: #if the player has not lost all their health, the game continues
            print("\033[1;32;m")
            print("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            multi_question6() #brings the player to the next question

    elif response5 == 3:
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Ma Lai Go is a traditional Cantonese steamed sponge cake, often found in dim sum restaurants. Its soft, airy texture and caramel-like flavor make it a favorite among many.")
        input("")
        print("")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question6() #brings the player to the next question            
    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question5()

def multi_question6():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #6: When is Cantonese Soup Generally Consumed?\u001b[0m")
    input("")
    print("1. At the beginning of the meal")
    print("2. During the meal")
    print("3. After the meal")
    input("")
    response6 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response6 == 1:
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" In Cantonese cuisine, soup is often consumed at the beginning of a meal to warm up the stomach and prepare it for dishes to come.")
        print("")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question7() #brings the player to the next question            
    

    elif response6 == 2:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print(" In Cantonese cuisine, soup is often consumed at the beginning of a meal to warm up the stomach and prepare it for dishes to come.")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        
        if len(goodies_list) == 0: #if the goodies_list is empty
            youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

        else: #if the player still has some health and cargo left
            input("")
            print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
            print("\u001b[37m \u001b")
            multi_question7()

    elif response6 == 3:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour 
        input("")
        print(" In Cantonese cuisine, soup is often consumed at the beginning of a meal to warm up the stomach and prepare it for dishes to come.")  
        input("") 
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
                
        if health == 0: #if the player looses all their health, the game ends
            youlost_health() #brings player to youlost_health (they lost the game because they lost all health)

        else: #if the player has not lost all their health, the game continues
            print("\033[1;32;m")
            print("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            multi_question7() #brings the player to the next question
    
    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question6()

def multi_question7():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #7: Which dish involves thinly sliced ingredients served with a boiling pot of broth?\u001b[0m")
    input("")
    print("1. Xianlongbao")
    print("2. Hot Pot")
    print("3. Steaming Pot")
    input("")
    response7 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response7 == 1:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print("Hot Pot is a communal dish where ingredients are cooked in a boiling pot of broth at the table. Participants can choose from a variety of meats, vegetables, and other add-ins.")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        
        if len(goodies_list) == 0: #if the goodies_list is empty
            youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

        else: #if the player still has some health and cargo left
            input("")
            print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
            print("\u001b[37m \u001b")
            multi_question8()

    elif response7 == 2:

        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Hot Pot is a communal dish where ingredients are cooked in a boiling pot of broth at the table. Participants can choose from a variety of meats, vegetables, and other add-ins.")
        print("")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question8() #brings the player to the next question            

    elif response7 == 3:

        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
        input("")
        print("Hot Pot is a communal dish where ingredients are cooked in a boiling pot of broth at the table. Participants can choose from a variety of meats, vegetables, and other add-ins.")
        input("")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
                
        if health == 0: #if the player looses all their health, the game ends
            youlost_health() #brings player to youlost_health (they lost the game because they lost all health)

        else: #if the player has not lost all their health, the game continues
            print("\033[1;32;m")
            print("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            multi_question8() #brings the player to the next question

    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question7()

def multi_question8():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #8: Yum Cha in Cantonese culture primarily refers to:\u001b[0m")
    input("")
    print("1. Eating food with your family")
    print("2. Meeting up with family members after a long time")
    print("3. Drinking tea and enjoying dim sum")
    input("")
    response7 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response7 == 1:
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print("Yum Cha translates to drink tea, and it often involves enjoying tea with dim sum dishes, especially during mornings or early afternoons.")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        
        if len(goodies_list) == 0: #if the goodies_list is empty
            youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

        else: #if the player still has some health and cargo left
            input("")
            print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
            print("\u001b[37m \u001b")
            multi_question9()

    elif response7 == 2:
      
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
        input("")
        print("Yum Cha translates to drink tea, and it often involves enjoying tea with dim sum dishes, especially during mornings or early afternoons.")
        input("")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
                
        if health == 0: #if the player looses all their health, the game ends
            youlost_health() #brings player to youlost_health (they lost the game because they lost all health)

        else: #if the player has not lost all their health, the game continues
            print("\033[1;32;m")
            print("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            multi_question9() #brings the player to the next question

    elif response7 == 3:


        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Yum Cha translates to drink tea, and it often involves enjoying tea with dim sum dishes, especially during mornings or early afternoons.")
        print("")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        multi_question9() #brings the player to the next question              time.sleep(0.5)


    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question8()

def multi_question9():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #9: Which ingredient is NOT traditionally found in a 'Har Gow' (shrimp dumpling)?\u001b[0m")
    input("")
    print("1. Chocolate")
    print("2. Bamboo shoots")
    print("3. Ginger")
    input("")
    response7 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response7 == 1:

        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Har Gow is a classic Cantonese dim sum dish made with translucent wrappers and contains shrimp, bamboo shoots, and sometimes ginger. Chocolate is not a traditional ingredient in Har Gow..")
        print("")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        time.sleep(0.5)
        multi_question10() #brings the player to the next question   

    elif response7 == 2:
      
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
        input("")
        print("Har Gow is a classic Cantonese dim sum dish made with translucent wrappers and contains shrimp, bamboo shoots, and sometimes ginger. Chocolate is not a traditional ingredient in Har Gow..")
        input("")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
                
        if health == 0: #if the player looses all their health, the game ends
            youlost_health() #brings player to youlost_health (they lost the game because they lost all health)

        else: #if the player has not lost all their health, the game continues
            print("\033[1;32;m")
            print("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            multi_question7() #brings the player to the next question

    elif response7 == 3:

        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print("Har Gow is a classic Cantonese dim sum dish made with translucent wrappers and contains shrimp, bamboo shoots, and sometimes ginger. Chocolate is not a traditional ingredient in Har Gow..")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        
        if len(goodies_list) == 0: #if the goodies_list is empty
            youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

        else: #if the player still has some health and cargo left
            input("")
            print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
            print("\u001b[37m \u001b")
            multi_question10()



    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question9()
        
def multi_question10():
#essentially this is a copy pasted from question 1 besides the questions and answers are changed

    global health
    #global makes the health variable to work correctly for the questions
    
    print("\u001b[33mQuestion #10: Which of the following is a popular Cantonese dessert made from sweetened almond milk, often set to a jelly-like consistency?\u001b[0m")
    input("")
    print("1. Almond Tofu")
    print("2. Mooncake")
    print("3. Almond Jelly")
    input("")
    response7 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) 

    if response7 == 1:

        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Almond Tofu, sometimes referred to as almond pudding, is a sweet dessert made from sweetened almond milk. While called 'tofu', it doesn't contain any soy and gets its name from its soft, tofu-like consistency.")
        print("")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        time.sleep(0.5)
        ending() #brings the player to the ending   

    elif response7 == 2:
      
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
        input("")
        print("Almond Tofu, sometimes referred to as almond pudding, is a sweet dessert made from sweetened almond milk. While called 'tofu', it doesn't contain any soy and gets its name from its soft, tofu-like consistency.")
        input("")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
                
        if health == 0: #if the player looses all their health, the game ends
            youlost_health() #brings player to youlost_health (they lost the game because they lost all health)

        else: #if the player has not lost all their health, the game continues
            print("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            ending() #brings the player to the ending

    elif response7 == 3:

        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") 
        input("")
        print("Almond Tofu, sometimes referred to as almond pudding, is a sweet dessert made from sweetened almond milk. While called 'tofu', it doesn't contain any soy and gets its name from its soft, tofu-like consistency.")
        input("")
        removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
        
        if len(goodies_list) == 0: #if the goodies_list is empty
            youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

        else: #if the player still has some health and cargo left
            input("")
            print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
            print("\u001b[37m \u001b")
            ending()


    else:
        time.sleep(2) #this makes the program sleep for 2 seconds before printing something
        print("This is not a valid choice, please try again")
        print("")
        multi_question9()

def time_question1():
    global health
    global response1
    print("\u001b[33mQuestion #1: Which is a popular Cantonese dim sum dish made from shrimp?\u001b[0m\n") #prints the question and below it prints the options. The stuff before and after the question is to change the colour of the text.
    print("1. Har Gow")
    print("2. Xianglongbao")
    print("3. Juk Gow")
    print("")
    input("")
    response1 = int(input("\x1B[4mPlease Type 1, 2, or 3 to select one of the options\u001b\033[0m\n")) #\n makes the user response go under this question
    
response1 = None
thread = threading.Thread(target=time_question1)
thread.start()
thread.join(8)  # Timeout after 8 seconds

if thread.is_alive(): #if 8 seconds have passed and the user did not summit an answer

    random_punishment = random.randint(0,1) #50/50 chance of the player recieving a random punishment for getting the question wrong
        
    if random_punishment == 0: #if the random number lands on 0, this code will play out
        time.sleep(0.5)
        print("")
        print("\u001b[31mYou ran out of time\u001b") #the pink parts of this line is to change the text colour            
        input("")
        print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
        health = health - 100 #the player looses 100 health
        input("")
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\u001b[37m \u001b")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        time_question2() #brings the player to the next question

    elif random_punishment == 1: #if the random number lands on 1, this code will play out
        
        time.sleep(0.5)
        print("")
        print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour   
        input("")
        print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
        input("") 
        health = health - 100 #the player looses 100 health
        print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
        print("\033[1;32;m")
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        time_question2() #brings the player to the next question

elif response1 == 1: #if the user selects the first option
    time.sleep(0.5)
    print("")
    print("\u001b[32mCorrect!\u001b")
    input("")
    print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
    input("")
    print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
    input("")
    print(" This is what cargo you have left: " + str(goodies_list) + ".")
    input("")
    time_question2() #brings the player to the next question

elif response1 == 2: #if the user selects the second option
    input("")
    print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
    input("")
    print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
    health = health - 100 #the player looses 100 health
    input("")
    print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
    print("\u001b[37m \u001b")
    input("")
    print(" This is what cargo you have left: " + str(goodies_list) + ".")
    input("")
    time_question2() #brings the player to the next question

elif response1 == 3: #if the user selects the third option
    time.sleep(0.5)
    print("")
    print("\u001b[31mIncorrect\u001b") 
    input("")
    print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
    input("") 
    removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
    input("")
    print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
    input("")
    print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
    print("\u001b[37m \u001b") #this changes the text to grey
    print("")
    input("")
    time_question2() #brings the player to the next question


else: #if the user did not click any of the options
    time.sleep(2) #this makes the program sleep for 2 seconds before printing something
    print("This is not a valid choice, please try again")
    print("")
    time.sleep(1)
    time_question1()



def time_question2():
    print("Nothing here yet")

def type_question1():
    global health
    #global makes the health variable to work correctly for the questions
    print("\u001b[33mQuestion #1: Which is a popular Cantonese dim sum dish made from shrimp?\u001b[0m") #prints the question and below it prints the options. The stuff before and after the question is to change the colour of the text.
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) #\n makes the user response go under this question

    if response1 == 'Har Gow'.casefold() or response1 == 'How Gow'.casefold() or repsonse1 == 'Haw Gow'.casefold(): #possible answers for the question listed to the left, any of these answers are considered correct, casefold means that the answer is not case sensitive
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) #prints the player's health on screen
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question2() #brings the player to the next question
    
    else: #if the player does not get the answer right
        random_punishment = random.randint(0,1) #50/50 chance of the player recieving a random punishment for getting the question wrong
        
        if random_punishment == 0: #if the random number lands on 0, this code will play out
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour    
            input("")
            print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
            health = health - 100 #the player looses 100 health
            input("")
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
            print("\u001b[37m \u001b")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question2() #brings the player to the next question

        elif random_punishment == 1: #if the random number lands on 1, this code will play out
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") #the pink parts of this line is to change the text colour   
            input("")
            print(" Har Gow is a traditional Cantonese dim sum specialty, comprising translucent steamed dumplings filled with shrimp.")
            input("") 
            health = health - 100 #the player looses 100 health
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) #prints the player's health on screen
            print("\033[1;32;m")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question2() #brings the player to the next question

def type_question2():
    global health
    print("\u001b[33mQuestion #2: What is a dessert soup made from ground almonds?\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'sweet almond soup'.casefold() or response1 == 'sweet almod soup'.casefold or response1 == 'almond soup'.casefold() or response1 == 'almod soup'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Sweet Almond Soup is a creamy dessert soup made from ground almonds. It is a soothing treat often served warm or chilled.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question3() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print(" Sweet Almond Soup is a creamy dessert soup made from ground almonds. It is a soothing treat often served warm or chilled.")
            health = health - 100 
            input("")
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
            print("\u001b[37m \u001b")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question3() 

        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print(" Sweet Almond Soup is a creamy dessert soup made from ground almonds. It is a soothing treat often served warm or chilled.")
            input("") 
            health = health - 100
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
            print("\033[1;32;m")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question3() 

def type_question3():
    global health
    print("\u001b[33mQuestion #3: What is Char Siu?\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'bbq pork'.casefold() or response1 == 'barbecued pork'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Char Siu is Cantonese-style barbecued pork, characterized by its sweet and savory marinade and its reddish hue.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question4() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print(" Char Siu is Cantonese-style barbecued pork, characterized by its sweet and savory marinade and its reddish hue.")
            health = health - 100 
            input("")
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
            print("\u001b[37m \u001b")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question4() 

        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print(" Char Siu is Cantonese-style barbecued pork, characterized by its sweet and savory marinade and its reddish hue.")
            input("") 
            health = health - 100
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
            print("\033[1;32;m")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question4() 

def type_question4():
    global health
    print("\u001b[33mQuestion #4: Bolo Bao, commonly seen in Cantonese bakeries, has a topping made of:\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'Pineapple shaped sugar crust'.casefold() or response1 == 'Pinapple-shaped sugar crust'.casefold() or response1 == 'Pinapple sugar crust'.casefold() or response1 == 'crispy topping'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" Bolo Bao, also known as Pineapple Bun, doesn't contain any pineapple. The name comes from the appearance of its sugar crust topping, which resembles the texture of a pineapple's skin.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question5() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print(" Bolo Bao, also known as Pineapple Bun, doesn't contain any pineapple. The name comes from the appearance of its sugar crust topping, which resembles the texture of a pineapple's skin.")
            health = health - 100 
            input("")
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
            print("\u001b[37m \u001b")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question5() 

        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print(" Bolo Bao, also known as Pineapple Bun, doesn't contain any pineapple. The name comes from the appearance of its sugar crust topping, which resembles the texture of a pineapple's skin.")
            input("") 
            health = health - 100
            print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
            print("\033[1;32;m")
            input("")
            print(" This is what cargo you have left: " + str(goodies_list) + ".")
            input("")
            type_question5() 

def type_question5(): 
    global health
    print("\u001b[33mQuestion #5: Which dish is a steamed sponge cake, known for its light and fluffy texture?\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'mai lai go'.casefold() or response1 == 'ma lai go'.casefold() or response1 == 'mai la go'.casefold() or response1 == 'ma la go'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Ma Lai Go is a traditional Cantonese steamed sponge cake, often found in dim sum restaurants. Its soft, airy texture and caramel-like flavor make it a favorite among many.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question6() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print("Ma Lai Go is a traditional Cantonese steamed sponge cake, often found in dim sum restaurants. Its soft, airy texture and caramel-like flavor make it a favorite among many.")
            input("")
            removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, 
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print("\033[1;32;m")
                print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question6()


        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print("Ma Lai Go is a traditional Cantonese steamed sponge cake, often found in dim sum restaurants. Its soft, airy texture and caramel-like flavor make it a favorite among many.")
            input("\033[1;32;m") 
            health = health - 100
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question6()
          
def type_question6(): 
    global health
    print("\u001b[33mQuestion #6: When is Cantonese Soup Generally Consumed? (Your answer should be about if its: before, during or after a meal)\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'in the beginning of the meal'.casefold() or response1 == 'at the beginning of the meal'.casefold() or response1 == 'before the meal'.casefold() or response1 == 'the beginning of the meal'.casefold() or response1 == 'the start of the meal'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print(" In Cantonese cuisine, soup is often consumed at the beginning of a meal to warm up the stomach and prepare it for dishes to come.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question7() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print(" In Cantonese cuisine, soup is often consumed at the beginning of a meal to warm up the stomach and prepare it for dishes to come.")
            input("")
            removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print("\033[1;32;m")
                print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question7()


        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print(" In Cantonese cuisine, soup is often consumed at the beginning of a meal to warm up the stomach and prepare it for dishes to come.")
            input("\033[1;32;m") 
            health = health - 100
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question7()     

def type_question7(): 
    global health
    print("\u001b[33mQuestion #7: Which dish involves thinly sliced ingredients served with a boiling pot of broth?\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'hot pot'.casefold() or response1 == 'boiling pot'.casefold() or response1 == 'warm pot'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Hot Pot is a communal dish where ingredients are cooked in a boiling pot of broth at the table. Participants can choose from a variety of meats, vegetables, and other add-ins.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question8() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print("Hot Pot is a communal dish where ingredients are cooked in a boiling pot of broth at the table. Participants can choose from a variety of meats, vegetables, and other add-ins.")
            input("")
            removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print("\033[1;32;m")
                print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question8()


        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print("Hot Pot is a communal dish where ingredients are cooked in a boiling pot of broth at the table. Participants can choose from a variety of meats, vegetables, and other add-ins.")
            input("\033[1;32;m") 
            health = health - 100
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question8()
  
def type_question8():
    global health
    print("\u001b[33mQuestion #8: Yum Cha in Cantonese culture primarily refers to:\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'Drinking tea and enjoying dim sum'.casefold() or response1 == 'drinking tea and eating dim sum'.casefold() or response1 == 'enjoying dim sum and drinking tea'.casefold() or response1 == 'eating dim sum and drinking tea'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Yum Cha translates to drink tea, and it often involves enjoying tea with dim sum dishes, especially during mornings or early afternoons.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question9() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print("Yum Cha translates to drink tea, and it often involves enjoying tea with dim sum dishes, especially during mornings or early afternoons.")
            input("")
            removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print("\033[1;32;m")
                print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question9()


        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print("Yum Cha translates to drink tea, and it often involves enjoying tea with dim sum dishes, especially during mornings or early afternoons.")
            input("\033[1;32;m") 
            health = health - 100
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question9()

def type_question9():
    
    global health
    print("\u001b[33mQuestion #9: Which dish involves wrapping ingredients in lotus leaves and then steaming them?\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'lo mai gai'.casefold() or response1 == 'lo ma ga'.casefold() or response1 == 'lo mai ga'.casefold() or response1 == 'lo mai ga'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Lo Mai Gai, or sticky rice chicken, involves glutinous rice filled with chicken, mushrooms, and sometimes sausages, all wrapped in lotus leaves before steaming?")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        type_question10() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print("Lo Mai Gai, or sticky rice chicken, involves glutinous rice filled with chicken, mushrooms, and sometimes sausages, all wrapped in lotus leaves before steaming?")
            input("")
            removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print("\033[1;32;m")
                print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question10()


        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print("Lo Mai Gai, or sticky rice chicken, involves glutinous rice filled with chicken, mushrooms, and sometimes sausages, all wrapped in lotus leaves before steaming?")
            input("\033[1;32;m") 
            health = health - 100
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                type_question10()

def type_question10():

    global health
    print("\u001b[33mQuestion #10: What is a popular Cantonese dessert made from sweetened almond milk, often set to a jelly-like consistency?\u001b[0m")
    input("")
    response1 = str(input("\x1B[4mType the Answer Below\u001b\033[0m\n")) 

    if response1 == 'Almond tofu'.casefold() or response1 == 'almod tofu'.casefold() or response1 == 'almond towfu'.casefold() or response1 == 'almod towfu'.casefold() or response1 == 'almond pudding'.casefold() or response1 == 'almond puding'.casefold():
        time.sleep(0.5)
        print("")
        print("\u001b[32mCorrect!\u001b")
        input("")
        print("Almond Tofu, sometimes referred to as almond pudding, is a sweet dessert made from sweetened almond milk. While called 'tofu', it doesn't contain any soy and gets its name from its soft, tofu-like consistency.")
        input("")
        print(" You successfully fended off a robber. Your health is currently: "+ str(health)) 
        input("")
        print(" This is what cargo you have left: " + str(goodies_list) + ".")
        input("")
        endung() 
    
    else: 
        random_punishment = random.randint(0,1) 
        
        if random_punishment == 0: 
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b")    
            input("")
            print("Almond Tofu, sometimes referred to as almond pudding, is a sweet dessert made from sweetened almond milk. While called 'tofu', it doesn't contain any soy and gets its name from its soft, tofu-like consistency.")
            input("")
            removed_item = goodies_list.pop() #this removes a random item from the goodies_list because the player got the question wrong
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print("\033[1;32;m")
                print(" A robber has stolen some of your" + removed_item + "!") #this prints what cargo the player lost
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                ending()


        elif random_punishment == 1: 
            
            time.sleep(0.5)
            print("")
            print("\u001b[31mIncorrect\u001b") 
            input("")
            print("Almond Tofu, sometimes referred to as almond pudding, is a sweet dessert made from sweetened almond milk. While called 'tofu', it doesn't contain any soy and gets its name from its soft, tofu-like consistency.")
            input("\033[1;32;m") 
            health = health - 100
            
            if len(goodies_list) == 0: #if the goodies_list is empty
                youlost_cargo() #brings player to the youlost_cargo (they lost the game because they lost all their cargo)

            elif health == 0: #if the player looses all their health, the game ends
                youlost_health() #brings player to youlost_health (they lost the game because they lost all health)


            else: #if the player still has some health and cargo left
                print(" Oh no! A robber cut you with a knife! Your health is currently: "+ str(health)) 
                input("")
                print(" This is what cargo you have left: " + str(goodies_list) + ".") #this prints what cargo the player has left
                print("\u001b[37m \u001b")
                ending()


validChoice = False
global start

while (validChoice == False): #beginning of the program starts here
    # global validChoice
    # global start
       
    print("Welcome to the Silk Road Adventure!!!")
    start = int(input("If you wanat the basics and preliminaries about the program or if you haven't played this program before, type the digit 1, if you want to skip this part, type the digit 2\n"))
        
    if start == 1:
        
        #this is essentially the "tutorial" for a new player where it teaches them the ropes of the program
        print("Hi Player, here you will be learning about how the program works, some background infromation, the points system and also the rules")
        input("Press Enter to Continue. Note that you will always have to press enter to continue throughout the game.")
        print("")
        print("Firstly, you will be learning about how the prgoram works.")
        input("")
        print("This program is a story game combined with a gamified learning system. You will playing as a Chinese merchant 600 C.E. trying to travel across the Silk Road with lots of valuables such as jade, porcelain, tea, and various spices.")
        input("")
        print("There will be various bandits and robbers trying to steal your precious cargo throughout the game. You have to protect your cargo and YOU from these vicious bandits by answering various questions about Cantonese cuisine correctly.")
        input("")
        print("If you fail to answer the question correctly, you loose some of your health and/or cargo.")
        input("")
        print("If you loose all your health or cargo, the game will end")
        input("")
        print("If you survive for longer than 10 questions, you manage to get to Europe to sell your goodies and beat the game!!!")
        input("")
        print("It is important to know that all questions will be " + "\x1B[4munderlined\u001b\033[0m")
        input("")
        print("Now you get choose your name!")
        input("")
        username = input("\x1B[4mWhat do you want your name to be? Please enter your name below.\u001b\033[0m\n") #this part of the program is asking for what name the player wants to have for the game
        print("")
        print("Good choice " + username + "!")
        print("")
        print("You will start with having porcelain, tea, ginger spices and cinnamon spices as all of your cargo in the beginning of the game.")
        input("")
        print("You will also start with 500 health in beginning, you loose 100 health for every question wrong.")
        input("")
        print("What type of Cantonese food questions during the game would you like? (WARNING: YOU WILL NOT be able to see how much time you have left for the timed multiple choice questions)")
        print("\u001b[31m!!!WARNING!!!: YOU WILL NOT be able to see how much time you have left for the timed multiple choice questions\u001b") 
        input("\033[1;32;m")        

        print("There are 3 different types of questions:")
        input("")
        print("1. Multiple Choice (beginner level)")
        print("2. Timed Multiple Choice (intermediate level)")
        print("3. Short Answer (advanced level)")
        print("")
        input("")

        answer_question = int(input("\x1B[4mChoose one of the options above by typing 1 for the first option, 2 for the second option, or 3 for the third option.\u001b\033[0m\n"))
        #answer_question is for when the user is choosing a type of question for the game

        if answer_question == 1:

            print("You chose the multiple choice questions for the game.")
            input("")
            print("We will now start the game!")
            print("")
            time.sleep(1)

            validChoice = True
            multi_question1() # here we call the first multiple choice questions directly

        if answer_question == 2:

            print("You chose the timed multiple choice questions for the game.")
            input("")
            print("You will have 8 seconds to answer each question")
            input("")
            print("We will now start the game!")
            print("")
            time.sleep(1)

            validChoice = True
            time_question1()

        if answer_question == 3:

            print("You chose the short answers questions for the game.")
            input("")
            print("We will now start the game!")
            print("")
            time.sleep(1)

            validChoice = True
            type_question1() #directs the user to a typed question

    elif start == 2: #if the player selects the second option for if they want to skip the tutorial
        print("As a reminder start with having porcelain, tea, ginger spices and cinnamon spices as all of your cargo in the beginning of the game. \n")
        input("Press Enter to Continue. Note that you will always have to press enter to continue throughout the game after text is displayed. \n")
        print("Also, you will start with 500 health in the beginning but loose 100 health for every question wrong")
        input("")
        print("It is important to know that all questions in the game will be " + "\x1B[4munderlined\u001b\033[0m")
        input("")
        print("Now you get choose your name!")
        input("\n")
        username = input("\x1B[4mWhat do you want your name to be? Please enter your name below.\u001b\033[0m\n") #this part of the program is asking for what name the player wants to have for the game
        print("")
        print("Good choice " + username + "!\n")

        print("What type of Cantonese food questions during the game would you like?")
        print("\u001b[31m!!!WARNING!!!: YOU WILL NOT be able to see how much time you have left for the timed multiple choice questions\u001b") 
        input("\033[1;32;m")



        print("There are 3 different types of questions:")
        input("")
        print("1. Multiple Choice (beginner level)")
        print("2. Timed Multiple Choice ((intermediate level)")
        print("3. Short Answer (advanced level)")
        input("")


        answer_question = int(input("\x1B[4mChoose one of the options above by typing 1 for the first option, 2 for the second option, or 3 for the third option.\u001b\033[0m\n"))
        #answer_question is for when the user is choosing a type of question for the game

        if answer_question == 1:

            print("You chose the multiple choice questions for the game.")
            input("")
            print("We will now start the game!")
            print("")
            time.sleep(1)


            validChoice = True
            multi_question1() # here we call the first question directly

        if answer_question == 2:

            print("You chose the timed multiple choice questions for the game.")
            input("")
            print("You will have 8 seconds to answer each question")
            input("")
            print("We will now start the game!")
            print("")
            time.sleep(1)

            validChoice = True
            time_question1()

        if answer_question == 3:

            print("You chose the short answers questions for the game.")
            input("")
            print("We will now start the game!")
            print("")
            time.sleep(1)

            validChoice = True
            type_question1()
            #add short answer questions here

    elif start == 3:
        multi_question1()
    #get rid of this for the final product "3'"

    elif start == 4:
        type_question1()
    #get rid of this for the final product

    elif start == 5:
        time_question1()

    else:
        # this will take us back to the beginning of the loop to see this menu again
        print("This is not a valid choice, please try again")
        print("")