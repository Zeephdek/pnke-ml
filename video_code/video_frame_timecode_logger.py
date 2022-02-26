import pyautogui as gui
import time
import keyboard
import os

"""
Press enter to start in 5 seconds, 
code presses space to start for your (using pyautogui)

Then monitors for certain keypresses from the keyboard
code copied from 2048
Press [u] to log the timestamp
Press [x] to end the logging and print the result (lazy to output in lul)

I swear this needs to export to a text file.

"""

## Main vars



##
prestimings = []

def currentTime():
    return time.time() - start_time

def main():
    
    ## input message
    print("""
Please switch to the video-playing window before the 5s timer elapses.

Frame key is [u]
End key is [x]
""")
    input("Code starts when the enter key is pressed.")

    os.system('cls')
    ## timer thingy
    for i in range(5):
        print(5-i) # lazy
        time.sleep(1)
        os.system('cls')

    print(0)
    time.sleep(0.1)
    os.system('cls')

    gui.press("space")
    print("Started logging...\n")

    global start_time
    start_time = time.time()
    
    n = 0
    while True:
        if keyboard.is_pressed('u'):
            n += 1
            cTime = currentTime()
            prestimings.append(cTime)
            print("Logged timestamp no. {} : {}".format(n, cTime))
            time.sleep(0.15) # 150ms between each press. GOOD.

        elif keyboard.is_pressed('x'):
            print("Ending logging. \nPlease copy the times out as I am too lazy to write exporting code.\n")
            break

        ## just a delay to prevent excessive key logs, or rather some n-key rollover nonsense
        
    os.system('cls')
    for i in prestimings:
        print(i)

    input("\nPress enter to close.")


main()