'''a smart home system that controls different devices'''

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is turned ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is turned OFF")
    
    def display_status(self):
        status = "ON" if self.is_on else "OFF"
        print(f"{self.name} is {status}")

class SmartLight(SmartDevice):
    def __init__(self, name, brightness=0):
        super().__init__(name)
        self.brightness = brightness
    
    def turn_on(self):
        super().turn_on()
        self.brightness = 100
        print(f"Brightness set to {self.brightness}%")
    
    def turn_off(self):
        super().turn_off()
        self.brightness = 0
    
    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name} brightness set to {self.brightness}%")
        else:
            print("Brightness must be between 0 and 100")

class SmartFan(SmartDevice):
    def __init__(self, name, speed=0):
        super().__init__(name)
        self.speed = speed
    
    def turn_on(self):
        super().turn_on()
        self.speed = 1
        print(f"Speed set to level {self.speed}")
    
    def turn_off(self):
        super().turn_off()
        self.speed = 0
    
    def set_speed(self, level):
        if 0 <= level <= 3:
            self.speed = level
            print(f"{self.name} speed set to level {self.speed}")
        else:
            print("Speed must be between 0 and 3")

class SmartTV(SmartDevice):
    def __init__(self, name, channel=0):
        super().__init__(name)
        self.channel = channel
    
    def turn_on(self):
        super().turn_on()
        self.channel = 1
        print(f"Channel tuned to {self.channel}")
    
    def turn_off(self):
        super().turn_off()
        self.channel = 0
    
    def change_channel(self, channel):
        if self.is_on:
            self.channel = channel
            print(f"{self.name} tuned to channel {self.channel}")
        else:
            print(f"Turn on {self.name} first!")

# Create and control devices
print("SMART HOME DEVICE CONTROL SYSTEM\n")
light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
tv = SmartTV("Living Room TV")

print("1. Smart Light Control:")
light.turn_on()
light.set_brightness(50)
light.turn_off()

print("\n2. Smart Fan Control:")
fan.turn_on()
fan.set_speed(2)
fan.turn_off()

print("\n3. Smart TV Control:")
tv.turn_on()
tv.change_channel(10)
tv.turn_off()
tv.change_channel(5)