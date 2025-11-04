import time
import datetime
import winsound

def alarmClock():
    alarm_set = input("Enter alarm time (HH:MM:SS format): ")
    print(f"⏰ Alarm set for {alarm_set}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_set:
            print("🔔 It's time to wake up!")
            # Beep sound (frequency, duration)
            winsound.Beep(1000, 1000)
            break
        time.sleep(1)

# Run the alarm clock
alarmClock()

