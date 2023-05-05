import os,time
def voice(text):
    os.system("espeak ' " + text + " ' ")
 
voice("I am fine")
