import time
import random

while True:
    print("Waddup homies! Welcome to:")
    time.sleep(1)
    print("+---------+")
    print("| QUIESH! |")
    print("+---------+")
    time.sleep(2)
    print("| It's a python-based quiz game that let users to make aral da terms about ITE 366 (Introduction to computing) |")
    time.sleep(2)
    print("| Bruh, it is basically a reviewer for IT students who wants to more aral for their future pareehh! |")
    time.sleep(2)
    user = input("> Orayt homie, can you tell me your name? ")
    play = input("> R.U.G ba pare? (Y/N)").lower()


    EZ_QUESTIONS = [
        (">It serves as a link between hardware and computer users?\n | S,_,S,T,_,_  S,O,_,_,W,_,R,E |"),
        (">It is a framework for storing data and instructions?\n | _,E,M,_,R,Y   S,_,S,T,_,_ |"),
        (">It is utilized to interact with a computer?\n | _,_,P,_,T   D,_,_,I,C,E |"),
        (">It is also referred to as the time-sharing operating system?\n | M,U,_,_,I   T,A,_,_,I,N,_   O,_ |"),
        (">Used to extract and spread processed data from the computer?\n | O,U,_,_,U,T   D,_,V,I,_,E |"),
        (">It is a group of applications that make up a computer system’s configuration and make it easier to use?\n | _,P,E,_,A,_,I,N,G   S,_,S,T,_,M |"),
        (">They are developed using user-level libraries rather than system calls?\n | U,S,_,R  L,_V,E,L   T,_,R,_,A,D |"),
        (">It is the core function of any computer?\n | _,R,O,_,E,_,S,I,_,G |"),
        (">Devices that are capable of storing information temporarily or permanently?\n | M,_,_,O,_,Y   D,E,_,I,_,E,S |"),
        (">This presentation is clear, simple, and to the point?\n | I,N,_,O,R,_,A,T,I,V,E  P,_,E,_,E,N,T,_,T,I,_,N |"),
        (">For second-generation computers, it is the first operating system?\n | _,A,_,_,H  O,_ |"),
        (">It's the hardware that controls the actions carried out by a computer's processor?\n | _,O,_,T,R,_,L  U,_,_,T |"),
        (">Systems that control all networking operations and are server-based?\n | _,E,_,_,O,R,_  _,S |"),
        (">By assigning distinct duties, an operating system controls how the processor works?\n | P,R,_,_,E,_,S,_,R   _,A,N,_,G,E,_,E,N,T |"),
        (">It is the operating system decides which apps should run in what sequence and how much time should be given to each one?\n | _,O,_  S,C,_,E,D,_,L,I,_,G |"),
        (">A machine for the manipulation of data to present information?\n | _,O,_,P,U,_,E,_ |"),
        (">A built-in operation from the spreadsheet app, which can be used to calculate cell, row, column, or orange values, manipulate data, and more?\n | _,U,N,_,_,I,_,N |"),
        (">It is a free, web-based word processor offered by Google?\n | G,_,_,_,L,E  _,O,_S |"),
        (">You can pick who to share your file with and what permissions they have to utilize?\n | _,H,A,_,_  A  _,O_ |"),
        (">You can view and adjust your information, activity, security settings, and privacy preferences here?\n | M,_,_,A,G,_   A,_,C,O,_,N,_ |"),        
    ]

    EZ_ANSWERS = [("yemfta"), ("moyem"), ("inuev"), ("ltskgs"), ("tpec"), ("ortye"), ("eehe"), ("pcsn"), ("emrvc"), ("fmrsao"), ("btcs"), ("cnoni"), ("ntwko"), ("ocsomam"), ("jbhun"), ("cmtr"), ("fcto"), ("oogdc"), ("sredc"), ("anecut")]

    CORRECT_ANS = [("| Shesh, you got it bruh! |"), ("| Nice one pareh! |"), ("| SHESHH! |"), ("| Correct bruh! |"), ("| You got some brain cells pareh! |"), ("| Nice one homie! |"),
                   ("| Yea! |"), ("| Tama pareeeeeeehhhhhhh! |"), ("| Ayt bet! |"), ("| Bussin! |"), ("| Ngl you good bruh! |"), ("| Omsim!| "), ("| Aryt! |"), ("| Fr fr! |"), ("| Alrighty tall! |")
                   ]
    INCORRECT_ANS = [("| Nah bruh! |"), ("| Not the correct answer pareeeeeeh! |"),("| Naaw! |"),("| Make bawi pareh! |"),("| You got a wrong ans shawty! |"),("|NO bruh! |"),("| NO SHESH FOR TONIGHT! |"),
                     ("| Try again aight! |"),("| Bruhf, nah! |"),("| Aaa shawty, again! |")
                     ]

    EZ_done = []


    CHALLENGING_QUESTIONS =[("> A computer system that includes the central processor, memory system, and input/output devices?\n|H,_,_,_,_,_,_,E|"),
                       ("> The bridge between computer users and hardware?\n|S,_,_,_,_,_,_,E|"),
                       ("> A set of rules and methods that describe the functionality, organization, and implementation of computer systems?\n|C,_,_,_,_,_,_,R   A,_,_,_,_,_,_,_,_,_,_,E|"),
                       ("> This processor has a single processing unit, external memory, and a small register set?\n|C,_,_,C|"),
                       ("> This architecture was the result of a rethink, which led to the development of high-performance processors?\n|R,_,S,_|"),
                       ("> John von Neumann coined and developed this architecture?\n|V,_,_ - N,_,_,_,_,_,N  A,_,_,_,_,_,_,_,_,_,_,E|"),
                       ("> It consists of code and data laid in distinct memory sections?\n|H,_,_,_,_,_,D  A,_,_,_,_,_,_,_,_,_,E|"),
                       ("> This architecture holds a collection of instructions that the processor renders and surmises?\n|I,_,_,_,_,_,_,_,_,_,N  S,_,_  A,_,_,_,_,_,_,_,_,_,_,E|"),
                       ("> The structural design of a microprocessor?\n|M,_,_,_,O  A,_,_,_,_,_,_,_,_,_,E"),
                       ("> A design that can serve user requirements like system architecture, computer modules having various interfaces, and data management within a system?\n|S,_,_,_,_,M  D,_,_,_,_,N|"),
                       ("> This knows and manages the threads?\n|K,_,_,_,_,L   L,_,_,_,L   T,_,_,_,_,D|"),
                       ("> The first multitasking operating system that was developed by Bell labs?\n|U,_,_,X|"),
                       ("> It was the first disk operating system and it was developed  by Apple?\n|A,_,_,_,E  D,_,_"),
                       ("> Microsoft built their first DOS operating system by purchasing ‘86’ from a Seattle company?\n|M,_  _,_,S|"),
                       ("> This came to existence when MS-DOS was paired with a GUI, a graphics environment?\n|M,_,_,_,_,_,_,_,T  W,_,_,_,_,_,S|"),
                       ("> This component of an OS handles user interactions, and it is the outermost layer of an OS?\n|S,_,_,_,L"),
                       ("> It is the central component of an OS, and it manages the system's resources?\n|K,_,_,_,_,L|"),
                       ("> This type of an OS is useful when many events occur in a short time or within certain deadlines?\n|R,_,_,L - T,_,_,_  _,S|"),
                       ("> The operating system for mainly the applications in which the slightest delay is unacceptable?\n |H,_,_,D  R,_,_,L - T,_,_,E  O,_ |"),
                       ("> The operating system for applications where time constraint is not very strict?\n|S,_,_,T  R,_,_,L - T,_,_,E  _,S|")
    ]
                       

    CHALLENGING_ANS = [("ardwar"),("oftwar"),("omputerchitectur"),("is"),("ic"),("oneumanrchitectur"),("arvarrchitectur"),("nstructioetrchitectur"),("icrrchitectur"),("ysteesig"),("erneevehrea"),("ni"),("pplos"),("sdo"),("icrosofindow"),("hel"),("erne"),("eaimeo"),("areaims"),("ofeaimo")]

    CHALLENGING_done = []
    
    def EZ_level():
        score = 0
        lives = 3
        heart_symbol = u"\u2764"
              
        while lives > 0:
            print("+--------------------------------------------------------------------------------------------------------------+")
            print("| Ayo homie! You have 3 lives on this level, and you must answer all the questions while you still have lives. |")
            print("| You must also finish the level within 100 secconds to get extra points, or else you'll get a demerit!        |")
            print("+--------------------------------------------------------------------------------------------------------------+")
            time.sleep(3)
            start_time = time.time()

            for i in range (1,11):
                time.sleep(0.5)
                print("Lives left:", heart_symbol * lives)
                print(i,".)")
                print("+------------------------------------------------------------------------+")
                print("| Type in the missing letters without any spaces to answer the question. |")
                print("+------------------------------------------------------------------------+")
                choose_from_EZ = random.choice(EZ_QUESTIONS) 
                print(choose_from_EZ)
                EZ_done.append(choose_from_EZ)
                ans = input("ANSWER:").lower()
                
                while ans not in EZ_ANSWERS:
                    print(random.choice(INCORRECT_ANS))
                    lives -= 1
                    print("Lives left:", heart_symbol * lives)
                    if lives == 0:
                        time.sleep(2)
                        print("| Deins Pareh:",user,"\n| G luck next time! |")
                        time.sleep(2)
                        print("| Your score is:",score,"|")
                        break
                    
                    time.sleep(0.5)
                    print(i,".)")
                    print("+------------------------------------------------------------------------+")
                    print("| Type in the missing letters without any spaces to answer the question. |")
                    print("+------------------------------------------------------------------------+")
                    print(choose_from_EZ)
                    ans = input("ANSWER:").lower()

                if ans in EZ_ANSWERS:
                    print(random.choice(CORRECT_ANS))
                    score += 10
                    print("| Your score is: ",score, "|")
                    EZ_QUESTIONS.remove(choose_from_EZ)
                
            
                elif lives == 0:
                    break

            end_time = time.time()
            print("\nFinalizing the results...")
            elapsed_time = end_time - start_time
            time.sleep(3)
            

            print("+---------------------------------------------------------------------+")
            print("   Ey,",user,"! The time you took is:",float(elapsed_time),"seconds.  ")
            print("+---------------------------------------------------------------------+")
            if elapsed_time > 100:
                score -= 10
                print("| Yo! you just got a demerit for answering too long. |")
                print("| Your score now is:",score,"points! |")

            elif elapsed_time < 100 and lives > 0:
                score += 20
                time.sleep(2)
                print("| Mah dude you are bussin! You finished the EZ level within 100 seconds! |")
                time.sleep(2)
                print("| You dasurv a merit for this! Your score now is:", score,"points! |")
            elif elapsed_time <100 and lives == 0:
                time.sleep(2)
                print("|Parecakes! You've finished this level whitin 100 seconds, but you have no lives left. |")
                time.sleep(2)
                print("|Better luck next time brooo! |")
                time.sleep(2)
            print("\n============================================================================================")

            break



    def Challenging_level():
        score = 0
        
        print("+--------------------------------------------------------------------------------+")
        print("| Ayo homie! You'll have ten question that you must answer in this level.        |")
        print("| You'll gain 10 points if you answered correctly or minus 10 points if not.     |")
        print("| If you finished this level within 80 secs you'll gain an extra points, or else |")
        print("| you will receive a demerit for exceeding.                                      |")
        print("+--------------------------------------------------------------------------------+")
        time.sleep(6)

        start_time = time.time()
        for i in range(1,11):
            time.sleep(0.5)
            print(i,".)")
            print("+------------------------------------------------------------------------+")
            print("| Type in the missing letters without any spaces to answer the question. |")
            print("+------------------------------------------------------------------------+")
                
            choose_from_challenging = random.choice(CHALLENGING_QUESTIONS)
            print(choose_from_challenging)
            CHALLENGING_done.append(choose_from_challenging)
            ans = input("ANSWER:").lower()

            while ans not in CHALLENGING_ANS:
                print(random.choice(INCORRECT_ANS))
                score -= 10
                print("| Your score is: ",score, "|")
                print(i,".)")
                print("+------------------------------------------------------------------------+")
                print("| Type in the missing letters without any spaces to answer the question. |")
                print("+------------------------------------------------------------------------+")
                print(choose_from_challenging)
                ans = input("ANSWER:").lower() 

            if ans in CHALLENGING_ANS:
                print(random.choice(CORRECT_ANS))
                CHALLENGING_QUESTIONS.remove(choose_from_challenging)
                score += 10
                print("| Your score is: ",score, "|")
            
        end_time = time.time()               
        print("\nFinalizing the results...")
        elapsed_time = end_time - start_time
        time.sleep(3)
        print("+------------------------------------------------------------------+")
        print("   Ey,",user,"The time you took is:",float(elapsed_time),"seconds.  ")
        print("+------------------------------------------------------------------+")
        if elapsed_time <= 80:
            score += 20
            time.sleep(2)
            print("Mah dude you are bussin! You finished the Challenging level within 80 seconds!")
            time.sleep(2)
            print("You dasurv a merit for this! Your score now is:", score,"points!")
        elif elapsed_time >80:
            score -= 20
            time.sleep(2)
            print("Awts shawty! You've exceeded 80 seconds on this level!")
            time.sleep(2)
            print("You've been demerited for this, your score now is:", score, "points!")
        time.sleep(2)
        print("\n============================================================================================")
        
        
    while play != "y" and play != "n":
        play = input("Are you G ba pareh? (Y/N)?").lower()
        
    if play == "y":
        time.sleep(1)
        print("+--------------------------------------+")
        print("| What's your difficulty level ba bro? |")
        print("| A.) EZ!                              |")
        print("| B.) Challenging Pareh!               |")
        print("+--------------------------------------+")
        level = input("Level:").lower()
        while level != "a" and level != "b": 
            level = input("BRUH! Choose letter A or B lang. aight?").lower()
        if level == "a":
            EZ_level()
        elif level == "b":
            Challenging_level()
            
            
    elif play == "n":
        print("\n|Scoobs bro! See you na lang next time! |")
        break

    time.sleep(1)
    print("+----------------------------------------------+")
    print("| Do you like to play again ba broskies? (Y/N) |")
    print("+----------------------------------------------+")
    again = input().lower()

    while again != "y" and again != "n":
        again = input("| Do you like to play again ba broskies? (Y/N) |\n").lower()
        
    if again == "y":
        CHALLENGING_QUESTIONS.append(CHALLENGING_done)
        EZ_QUESTIONS.append(EZ_done)
        continue
    elif again == "n":
        print("Scoobs bro! \n see you na lang next time!")
        break
        
