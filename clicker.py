import pyautogui
from pynput import keyboard
import termios
import threading
import time
import sys
import os

# Global variables to control the script
click_delay = 0.4
input_mode = False
delay_input = ""
is_enabled = False
shift_pressed = False
click_thread = None
program_running = True
confirm_exit = False
exit_confirmed = False

def flush_input():
    if os.name == 'posix':
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def click_loop():
    """Function to handle continuous clicking while Shift is pressed"""
    while shift_pressed and is_enabled:
        pyautogui.click()
        time.sleep(click_delay)

def on_press(key):
    """Handle key press events"""
    global is_enabled, shift_pressed, click_thread, program_running, confirm_exit, exit_confirmed
    global input_mode, delay_input, click_delay
    
    try:
        # Enable script with Home key
        if key == keyboard.Key.home:
            is_enabled = True
            sys.stdout.write("\rScript enabled\n")
            sys.stdout.flush()
            
        # Disable script with End key
        elif key == keyboard.Key.end:
            is_enabled = False
            shift_pressed = False
            sys.stdout.write("\rScript disabled\n")
            sys.stdout.flush()
            
        # Handle Delete key with confirmation
        elif key == keyboard.Key.delete and not confirm_exit and not input_mode:
            confirm_exit = True
            sys.stdout.write("\r                    ")
            sys.stdout.write("\rExit program? (y/n): ")
            sys.stdout.flush()
            
        # Handle confirmation keys when confirm_exit is True
        elif confirm_exit:
            if hasattr(key, 'char'):
                if key.char == 'y':
                    exit_confirmed = True
                    program_running = False
                    sys.stdout.write("\r                    ")
                    sys.stdout.write("\rProgram terminated\n")
                    sys.stdout.flush()
                    time.sleep(0.5)
                    return False
                elif key.char == 'n':
                    confirm_exit = False
                    sys.stdout.write("\r                    ")
                    sys.stdout.write("\rCancelled\n")
                    sys.stdout.flush()
        
        # Start clicking when Shift is pressed (if enabled)
        elif key == keyboard.Key.shift and is_enabled:
            if not shift_pressed:
                shift_pressed = True
                if click_thread is None or not click_thread.is_alive():
                    click_thread = threading.Thread(target=click_loop)
                    click_thread.start()
                    
        # Enter delay input mode with Tilde key
        elif hasattr(key, 'char') and key.char == '`' and not confirm_exit:
            input_mode = True
            delay_input = ""
            sys.stdout.write("\r                    ")
            sys.stdout.write("\rEnter delay (x.x) then press Insert: ")
            sys.stdout.flush()
        
        # Handle delay input when in input_mode
        elif input_mode:
            if hasattr(key, 'char'):
                if key.char.isdigit() or key.char == '.':
                    delay_input += key.char
                    sys.stdout.write(f"\rEnter delay (x.x) then press Insert: {delay_input}")
                    sys.stdout.flush()

            # Handle Backspace to delete last character
            elif key == keyboard.Key.backspace and delay_input:
                delay_input = delay_input[:-1]
                sys.stdout.write(f"\rEnter delay (x.x) then press Insert: {delay_input} ")
                sys.stdout.flush()
            
            # Update delay with Insert key when in input mode
            elif key == keyboard.Key.insert:
                try:
                    new_delay = float(delay_input)
                    if new_delay >= 0:
                        click_delay = new_delay
                        sys.stdout.write("\r                                                   ")
                        sys.stdout.write(f"\rDelay updated to {click_delay} seconds\n")
                        sys.stdout.flush()
                    else:
                        sys.stdout.write("\r                                                   ")
                        sys.stdout.write("\rError: Delay must be non-negative\n")
                        sys.stdout.flush()
                except ValueError:
                    sys.stdout.write("\r                                                       ")
                    sys.stdout.write("\rError: Invalid delay format (use x.x)\n")
                    sys.stdout.flush()
                input_mode = False
                delay_input = ""
        
        # Show current delay with Insert key when not in input mode or confirm_exit
        elif key == keyboard.Key.insert and not input_mode and not confirm_exit:
            sys.stdout.write("\r                                                               ")
            sys.stdout.write(f"\rCurrent delay: {click_delay} seconds\n")
            sys.stdout.flush()
                    
    except AttributeError:
        pass

def on_release(key):
    """Handle key release events"""
    global shift_pressed
    
    if key == keyboard.Key.shift:
        shift_pressed = False

def main():
    # Clear terminal echo for cleaner output (Unix-like systems)
    if os.name == 'posix':
        os.system('stty -echo')
    
    sys.stdout.write("Welcome to Shift-Clicker Program!\n")
    sys.stdout.write("| Home: Enable | End: Disable | Insert: Delay Value | Backtick: Edit | Delete: Exit |\n")
    sys.stdout.flush()
    
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            while program_running:
                time.sleep(0.1)
            flush_input()
            listener.stop()
    finally:
        if os.name == 'posix':
            os.system('stty echo')

if __name__ == "__main__":
    pyautogui.PAUSE = 0
    
    try:
        main()
    except KeyboardInterrupt:
        if os.name == 'posix':
            os.system('stty echo')
        sys.stdout.write("\nProgram terminated by user\n")
        sys.stdout.flush()
        sys.exit(0)
