
import pyttsx3

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
        
    def boot_up(self):
        print(f"The {self.brand} laptop with {self.ram}GB RAM is turning on!")
        
    def speak_specs(self):
        engine = pyttsx3.init()
        # Adjusting the speech rate slightly slower for crisp, clear audio
        engine.setProperty('rate', 150)
        message = f"This is your custom {self.brand} computer, equipped with {self.ram} gigabytes of memory."
        engine.say(message)
        engine.runAndWait()

# --- INSTANTIATION ZONE ---
# 1. Create a real object instance based on the Laptop blueprint
# Replace "L2E" with whatever your laptop brand is!
my_laptop = Laptop("L2E", 16)

# 2. Call the methods to watch it work
my_laptop.boot_up()     # This will print the message in your terminal
my_laptop.speak_specs() # This will make your laptop speakers talk!





import pyttsx3

def speak_text(text):
    # Initialize the voice engine
    engine = pyttsx3.init()
    
    # Adjust speed (150 is clear and standard)
    engine.setProperty('rate', 150)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Put whatever you want your laptop to say right here!
    message = "HOW! how did you let that happen?"
    
    print("Speaking...")
    speak_text(message)
    print("Done!")

