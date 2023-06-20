# unlock door with phrases
# say Khul Ja SIM SIM !

import speech_recognition as sr
from pyfirmata import Arduino,util,SERVO
from time import sleep

#Arduino Code

port="COM4"
board=Arduino(port)
iter8 = util.Iterator(board)
iter8.start()

pin=board.get_pin('d:9:s')
pin.write(0)


def openDoor():
    pin.write(100) 

 
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print(f"You said :{text}\n")
            if text=="khul ja sim sim":
                print("Opening Door!")
                openDoor()
                sleep(5)
                pin.write(0)
                break
            else:
                print("Wrong Commmand!")
                break
        except:
            print("Sorry couldnt get that")
              