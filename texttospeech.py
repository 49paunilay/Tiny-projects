# text to speech
import pyttsx3
engine = pyttsx3.init()
filename='Count.txt'
fhand=open(filename)
empty=''
for i in fhand:
    empty=empty+i
print(empty)

engine.say(empty)
engine.save_to_file(empty,filename+'.mp3')
engine.runAndWait()