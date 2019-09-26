# let the user know what's going on
print ("Welcome to the wired story!")
print ("Answer the questions to start your journey.")

# variables containing all of story info
location1 = raw_input("where is your favourite city?: ")
popstar = raw_input("Tell me an popstar that you hate: ")
clothes1 = raw_input("what do you normally wear?:")
activities = raw_input("what do you normally do in the morning?:")
emotion = raw_input("what do you feels now?:")



story = " You walking on the street of " + location1 + "with" + popstar + " who want to sell you " + clothes1 + " that you only wear when you are doing " + activities +", which make you feels so " + emotion + "."

#print the story after they finished the info
print (story)
