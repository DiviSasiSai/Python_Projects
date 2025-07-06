import time
import datetime
import pygame

# Initialize and play sound for 30 seconds
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/divis/Downloads/wake_up.wav")
    pygame.mixer.music.play()

    time.sleep(30)

    pygame.mixer.music.stop()

# Terminal clear sequences
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Alarm logic
def alarm(alarm_time):
    while True:
        print(CLEAR + CLEAR_AND_RETURN)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{current_time}")

        if current_time == alarm_time:
            print("Wake Up!")
            play_sound()
            break  # Exit loop after alarm triggers

        time.sleep(1)

# Clock with 2 snoozes (5 minutes each)
def clock(alarm_time):
    alarm(alarm_time)
    for _ in range(2):
        h, m, s = map(int, alarm_time.split(':'))
        m += 1
        if m >= 60:
            h += m // 60
            m %= 60
        if h >= 24:
            h %= 24
        alarm_time = f"{h:02d}:{m:02d}:{s:02d}"
        alarm(alarm_time)

# Main program
if __name__ == "__main__":
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f"Current Time - {now}")
    alarm_input = input("Enter Alarm Time (HH:MM:SS): ")
    clock(alarm_input)
