import pyjokes
# print("Printing Jokes...")
joke=pyjokes.get_joke()
print(joke)

import pyttsx3
engine=pyttsx3.init()
engine.say("Hello Swapndeep")
engine.runAndWait()