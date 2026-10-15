import time
import schedule
from plyer import notification



# 1. NOTIFICATION HELPER FUNCTION

def send_break_alert(title, message, timeout=5):
    notification.notify(
        title=title,
        message=message,
        app_name="Health & Ergonomics Daemon",
        timeout=timeout 
    )


# 2. SCHEDULED TASK FUNCTIONS
def hydration_job():
    print("Triggered: Hydration Alert")
    send_break_alert(
        title="Hydration Alert",
        message="Time to drink a glass of water! Stay hydrated."
    )

def posture_job():
    print("Triggered: Posture Check")
    send_break_alert(
        title="Posture Check",
        message="Sit up straight! Stretch your back and roll your shoulders."
    )


# 3. MAIN SCHEDULER & BACKGROUND LOOP
def main():
    print("==================================================")
    print("   Desktop Health & Break Reminder Daemon Active   ")
    print("==================================================")
    print("• Hydration Alert: Scheduled every 10 seconds (Testing mode)")
    print("• Posture Check:   Scheduled every 20 seconds (Testing mode)")
    print("Press Ctrl+C at any time to stop the daemon safely.\n")

    # Step A: Register job schedules
    schedule.every(10).seconds.do(hydration_job)
    schedule.every(20).seconds.do(posture_job)

    # Step B: Continuous Background Listener Loop with Ctrl+C Interruption
    try:
        while True:
            schedule.run_pending()  # Checks if any job is due to run
            time.sleep(1)           # Pauses for 1 second to prevent high CPU usage
            
    except KeyboardInterrupt:
        # Step C: Catch Ctrl+C safely and show clean shutdown message
        print("\n\nKeyboardInterrupt detected!")
        print("Health & Break Reminder Daemon has been safely terminated. Bye!\n")


if __name__ == "__main__":
    main()