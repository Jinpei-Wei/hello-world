import sys # system stuff for exiting
player = { 
    "name": "p1"
}
pcmd = raw_input(">")

def printGraphic(name):
    if (name == "apple"):
        print '                               /$$          '
        print '                              | $$          '
        print '  /$$$$$$   /$$$$$$   /$$$$$$ | $$  /$$$$$$ '
        print ' |____  $$ /$$__  $$ /$$__  $$| $$ /$$__  $$'
        print '  /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$$$$$$$'
        print ' /$$__  $$| $$  | $$| $$  | $$| $$| $$_____/'
        print '|  $$$$$$$| $$$$$$$/| $$$$$$$/| $$|  $$$$$$$'
        print ' \_______/| $$____/ | $$____/ |__/ \_______/'
        print '          | $$      | $$                    '
        print '          | $$      | $$                    '
        print '          |__/      |__/                    '



    if (name == "ipad"):
        print '                     &(                                          '
        print '               @&&&&&&&&&&&@    .@@  @@@@@@@@,                 @@ '
        print '              @&&&&&&&&&&&&          @@(   *@@(                @@ '
        print '             *&&&&&&&&&&&&.     .@@  @@(   .@@# @@@@@@@  &@@@@@@@ '
        print '              &&&&&&&&&&&&@     .@@  @@@@@@@@,    ./&@@.#@@    @@ '
        print '              (&&&&&&&&&&&&&%   .@@  @@(       #@@,  @@ #@@    @@ '
        print '               &&&&&&&&&&&&%    .@@  @@(       &@@/(@@@. @@@%&@@@ '
        print '                .@@&/./&@&                       ..        ..     '


def ipad():

    printGraphic("ipad")

    print "There are so many differnt ways to purchase the ipad you desired actually."
    print "Where would you try to get from?"
    print "Your options : [apple store, best buy]"
    pcmd = raw_input(">")

    if (pcmd == "applestore"):
        print "You got your stunning ipad, show off to your friends!"

    elif (pcmd == "bestbuy"):
        print "You got a discont at bust buy when buying your iphone,so lucky!"

    else:
        print "I don't understand."
        ipad()

def iPhone():

    print "There are so many differnt ways to purchase the iphone you desired actually."
    print "Where would you try to get from?"
    print "Your options : [apple store, best buy]"
    pcmd = raw_input(">")
    #option 1 
    if (pcmd == "apple store"):
       print "You got your stunning iphone, show off to your friends!"

    #option 2 
    elif (pcmd == "best buy"):
       print "You got a discont at bust buy when buying your iphone,so lucky!"
    else:
       print "I don't understand."
       iPhone()



def productSelect():
    print "You begin to think very depply about what to buy......."
    print "After a while, You make your mind!"
    print "Your options: [ ipad, iphone11, macbook]"

    pcmd = raw_input(">")

    if (pcmd == "macbook"):
       print "Seems like you already got the most high-end one.It seems not very necessary to you."
       productSelect()


    elif (pcmd == "iphone11"):
       print "You decide to buy the newset iphone"
       iPhone()

    elif (pcmd == "ipad"):
        print "You decide to buy the newset ipad"
        ipad()  

    else:
        print "I don't understand."


def introStory():
       
            # let's introduce them to our world
    print "Welcome to the group of apple's fans!"
    print "We know that you are also a huge fan of apple who always want to buy something from apple..."
    print "So do you want to buy some products today? "

    pcmd = raw_input("please choose yes or no >")

    if (pcmd == "yes"):

        print "You suddenly get excited but not sure what to buy"
        raw_input("press entrer >")
        productSelect()
    else:
        print "No?...Come on! You are a huge apple fans, think about it again please!"  
        pcmd = raw_input("press enter >")
        introStory()
            #repeat when they don't follow


def main():

    printGraphic("apple") #print the graphic of apple
    introStory()

main()





