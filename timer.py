import time
import sys
import tkinter as tk

def countdown(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        remaining_time = seconds - elapsed_time
        
        # Calculate the percentage of time elapsed
        progress = (elapsed_time / seconds) * 100
        
        # Clear the terminal screen
        sys.stdout.write("\033[H\033[J")
        
        # Print the progress bar
        sys.stdout.write(f"Progress: [{'=' * int(progress / 5)}{' ' * int(20 - progress / 5)}] {int(progress)}%\n")
        sys.stdout.flush()
        
        # Wait for 0.1 seconds before updating the progress bar
        time.sleep(0.1)
    
    # Clear the terminal screen
    sys.stdout.write("\033[H\033[J")
    
    # Print the completed progress bar
    sys.stdout.write("Progress: [====================] 100%\n")
    sys.stdout.flush()
    
    print("Timer completed!")
    
    # Flash the screen
    flash_screen()

def flash_screen():
    # Create a blank Tkinter window
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.configure(background='white')

    # Flash the screen by changing the background color
    for _ in range(5):
        window.configure(background='black')
        window.update()
        time.sleep(0.2)
        window.configure(background='white')
        window.update()
        time.sleep(0.2)

    # Close the window
    window.destroy()

def get_time_input():
    time_input = input("Enter the time (e.g., 1 min, 2 hours): ")
    
    try:
        time_value, time_unit = time_input.split()
        time_value = int(time_value)
        
        if time_unit == "sec" or time_unit == "secs":
            return time_value
        elif time_unit == "min" or time_unit == "mins":
            return time_value * 60
        elif time_unit == "hour" or time_unit == "hours":
            return time_value * 60 * 60
        else:
            raise ValueError()
    
    except ValueError:
        print("Invalid time format. Please try again.")
        return get_time_input()

def main():
    time_seconds = get_time_input()
    countdown(time_seconds)

if __name__ == "__main__":
    main()
