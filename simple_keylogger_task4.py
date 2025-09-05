
"""
Simple Keylogger using only built-in Python modules
FOR EDUCATIONAL PURPOSES ONLY
"""

import sys
import os
import time
from datetime import datetime


if os.name == 'nt':  
    import msvcrt
else:  
    import tty
    import termios

class SimpleKeylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.is_logging = False
        self.special_keys = {
            '\r': '[ENTER]',
            '\n': '[ENTER]',
            '\t': '[TAB]',
            ' ': '[SPACE]',
            '\x1b': '[ESC]',
            '\x7f': '[BACKSPACE]',
        }
    
    def show_warning(self):
        """Display ethical warning"""
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                 ETHICAL KEYLOGGER WARNING               ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  FOR EDUCATIONAL PURPOSES ONLY                          ║")
        print("║  Use only on devices you own                            ║")
        print("║  Get explicit permission before monitoring others       ║")
        print("║  Illegal use may result in criminal charges             ║")
        print("╚══════════════════════════════════════════════════════════╝")
        
        consent = input("Do you understand and agree? (yes/no): ").lower().strip()
        return consent in ['yes', 'y']
    
    def get_char(self):
        """Get a single character from input"""
        if os.name == 'nt': 
            return msvcrt.getch().decode('utf-8', errors='ignore')
        else:  
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    
    def log_key(self, key):
        """Log a key press to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        formatted_key = self.special_keys.get(key, key)
        
     
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"{timestamp}: {formatted_key}\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")
    
    def start_logging(self):
        """Start the keylogger"""
        if not self.show_warning():
            print("Logging cancelled.")
            return False
        
        print("\nKeylogger started. Press ESC to stop.")
        print("Now typing will be logged to:", self.log_file)
        print("-" * 50)
        
        
        try:
            with open(self.log_file, "w", encoding="utf-8") as f:
                f.write("Keylogger Started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                f.write("=" * 50 + "\n\n")
        except Exception as e:
            print(f"Error creating log file: {e}")
            return False
        
        self.is_logging = True
        return True
    
    def run(self):
        """Main logging loop"""
        if not self.start_logging():
            return
        
        try:
            while self.is_logging:
                try:
                    
                    char = self.get_char()
                    
                    
                    if char == '\x1b':  
                        print("\nESC pressed. Stopping...")
                        break
                    
                    
                    self.log_key(char)
                    
                   
                    if char == '\r' or char == '\n':
                        print()  
                    elif char == '\x7f':  
                        sys.stdout.write('\b \b')  
                    else:
                        sys.stdout.write(char)
                    
                    sys.stdout.flush()
                    
                except KeyboardInterrupt:
                    print("\nCTRL+C detected. Stopping...")
                    break
                except Exception as e:
                    print(f"\nError: {e}")
                    break
                    
        finally:
            self.stop_logging()
    
    def stop_logging(self):
        """Stop the keylogger"""
        if self.is_logging:
            self.is_logging = False
            
           
            try:
                with open(self.log_file, "a", encoding="utf-8") as f:
                    f.write("\n" + "=" * 50 + "\n")
                    f.write("Keylogger Stopped: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                print("Log saved to:", self.log_file)
            except Exception as e:
                print(f"Error closing log file: {e}")

def view_log():
    """View the log file contents"""
    log_file = "keylog.txt"
    if os.path.exists(log_file):
        try:
            print("\n" + "=" * 60)
            print("LOG FILE CONTENTS:")
            print("=" * 60)
            with open(log_file, "r", encoding="utf-8") as f:
                content = f.read()
                print(content)
        except Exception as e:
            print(f"Error reading log file: {e}")
    else:
        print("No log file found.")

def main():
    """Main function"""
    print("Simple Built-in Keylogger")
    print("Educational purposes only!")
    print("-" * 30)
    
    keylogger = SimpleKeylogger()
    
    try:
        keylogger.run()
        
     
        view = input("\nWould you like to view the log file? (yes/no): ").lower().strip()
        if view in ['yes', 'y']:
            view_log()
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nProgram exited. Remember to use this knowledge ethically!")

if __name__ == "__main__":
    main()