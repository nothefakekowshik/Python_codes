import random
import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
numbers=[]
for i in range(1,91):
    r=random.randint(1,90)
    if r not in numbers:
        numbers.append(r)
numbers.sort()
print(numbers)
# for i in numbers:
#     print(i)
    # engine.say(i)
    # engine.runAndWait()
    # time.sleep(5)