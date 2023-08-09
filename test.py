import time

def countdown_timer(duration_minutes):
    duration_seconds = duration_minutes * 60
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, duration_seconds - elapsed_time)
        minutes, seconds = divmod(remaining_time, 60)
        print(f"Remaining time: {int(minutes)} minutes {int(seconds)} seconds", end='\r')

        if remaining_time <= 0:
            break

    print("\nTime's up!")

# Usage example:
if __name__ == "__main__":
    countdown_minutes = 100
    countdown_timer(countdown_minutes)
