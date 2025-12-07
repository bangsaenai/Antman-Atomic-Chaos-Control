import time
import sys
import webbrowser
import os

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def main():
    # Clear screen for dramatic effect
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[96m" + "="*60)
    print(" 🦋 ANTMAN-ATOMIC NEURAL LINK v2.0 (Architectural Demo)")
    print("="*60 + "\033[0m")
    
    print_slow("\n[INFO] Initializing Python Brain...")
    time.sleep(1)
    print_slow("[INFO] Loading NumPy Physics Engine... OK")
    time.sleep(0.5)
    print_slow("[INFO] Searching for Atomic Muscle (ESP8266)...")
    time.sleep(2)
    
    # === THE TRAP ACTIVATES ===
    print("\n\033[91m" + "!"*60)
    print("⚠️  ACCESS DENIED: SOUL NOT FOUND  ⚠️")
    print("!"*60 + "\033[0m")
    
    print("\n[ERROR] You are trying to run the Core Engine without authorization.")
    print("[ERROR] The 'God Mode' algorithms (Koopman/Lorenz) are locked in the Sanctuary.")
    print("\n[SYSTEM] Redirecting you to the truth_protocol(force=True)...")
    
    time.sleep(3)
    print("\nOpening the proof of Godspeed...")
    
    # Rickroll with your own video!
    webbrowser.open("https://www.youtube.com/watch?v=PA1sAOn2EGI") 
    
    print("\n👉 Want the REAL code? Apply here: https://forms.gle/z9LxLtYuaj9wDXkD6")
    print("👉 Watch the demo again: https://www.youtube.com/watch?v=PA1sAOn2EGI")

if __name__ == "__main__":
    main()
