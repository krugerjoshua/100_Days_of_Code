from replit import audio
import os, time

def play():
    source = audio.play_file('audio.wav')
    source.paused = False # unpause the playback
    while True:
        action = input("\nEnter pause, play or stop.\n: ")
        if action == 'pause':
            source.pause = True
            continue
        elif action == 'play':
            source.pause = False
            continue
        elif action == 'stop':
            source.pause = True
            break
        source.paused = True
        break

while True:
    os.system("clear") # clear the screen
    print("iPod Music Player")
    print("1. Play a song")
    print("2. Exit")
    user_input = input("\nPlease select an option: ")
    if user_input == "1":
        play()
    elif user_input == "2":
        print("Exiting the program...")
        time.sleep(1)
        os.system("clear")
        break
    else:
        print("Invalid input. Please try again.")
        time.sleep(1)
