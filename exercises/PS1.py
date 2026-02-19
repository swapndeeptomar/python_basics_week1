# Poem Print
print('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')

# REPL for MUltiplication

# install External module and use it
import pyttsx3
engine=pyttsx3.init()
engine.say("Hello Swapndeep")
engine.runAndWait()

import os
directory_path='/'
contents=os.listdir(directory_path)

for item in contents:
    print(item)