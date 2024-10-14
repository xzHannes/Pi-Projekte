import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import time
from evdev import UInput, ecodes

# ADC initialisieren (für den Joystick)
adc = Adafruit_ADS1x15.ADS1115()
joystick_button_pin = 4  # GPIO-Pin für den Joystick-Button

# GPIO-Pins für die Richtungstasten
direction_pins = {
    'Up': 20,    # GPIO20
    'Left': 21,  # GPIO21
    'Down': 12,  # GPIO12
    'Right': 16  # GPIO16
}

# GPIO-Pins für die Taster (A, B, X, Y)
button_pins = {
    'A': 17,  # GPIO17
    'B': 27,  # GPIO27
    'X': 22,  # GPIO22
    'Y': 23   # GPIO23
}

# GPIO konfigurieren
GPIO.setmode(GPIO.BCM)

# Joystick-Button konfigurieren
GPIO.setup(joystick_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Richtungs-Taster konfigurieren
for pin in direction_pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up-Widerstände aktivieren

# Button-Taster konfigurieren
for pin in button_pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up-Widerstände aktivieren

# HID-Eingabegerät initialisieren (für den Joystick und die Taster)
ui = UInput()

# Kalibrierungswerte für den Joystick
calibration_x = 20800  # Mittelwert der X-Achse (Ruheposition)
calibration_y = 20400  # Mittelwert der Y-Achse (Ruheposition)
deadzone = 1000  # Anpassung der Deadzone

# Grenzwerte für die Joystick-Richtungen
left_limit = calibration_x - 5000  # Linke Grenze
right_limit = calibration_x + 5000  # Rechte Grenze
up_limit = calibration_y - 5000  # Obere Grenze
down_limit = calibration_y + 5000  # Untere Grenze

# Zeitabstand zwischen den Eingaben
input_delay = 0.2  # Sekunden, um Doppelsignale zu vermeiden

def read_joystick():
    """Liest die X- und Y-Achse sowie den Button-Zustand des Joysticks aus"""
    x_value = adc.read_adc(0, gain=1)  # X-Achse
    y_value = adc.read_adc(1, gain=1)  # Y-Achse
    button_state = GPIO.input(joystick_button_pin)  # Button SW abfragen
    return x_value, y_value, button_state

def read_directions():
    """Liest den Zustand der Richtungstasten (Up, Down, Left, Right)"""
    direction_states = {}
    for direction, pin in direction_pins.items():
        state = GPIO.input(pin)  # 0 = gedrückt, 1 = nicht gedrückt
        direction_states[direction] = state
    return direction_states

def read_buttons():
    """Liest den Zustand der Taster (A, B, X, Y)"""
    button_states = {}
    for button, pin in button_pins.items():
        state = GPIO.input(pin)  # 0 = gedrückt, 1 = nicht gedrückt
        button_states[button] = state
    return button_states

try:
    print("Taster und Joystick Test gestartet. Drücke die Richtungstasten, A, B, X, Y oder bewege den Joystick...")

    while True:
        # Joystick und Buttons lesen
        x, y, joystick_button = read_joystick()
        direction_states = read_directions()
        button_states = read_buttons()

        # Deadzone für Joystick anwenden
        x_output = 0
        y_output = 0

        if x < left_limit:
            x_output = -1
            print("Linke Richtung aktiviert (Joystick).")
            ui.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 1)
        elif x > right_limit:
            x_output = 1
            print("Rechte Richtung aktiviert (Joystick).")
            ui.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 1)

        if y < up_limit:
            y_output = -1
            print("Obere Richtung aktiviert (Joystick).")
            ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 1)
        elif y > down_limit:
            y_output = 1
            print("Untere Richtung aktiviert (Joystick).")
            ui.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 1)

        # Joystick Button
        if joystick_button == 0:
            print("Joystick Button gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.BTN_TRIGGER, 1)
        else:
            ui.write(ecodes.EV_KEY, ecodes.BTN_TRIGGER, 0)

        # Tastereingaben für Richtungen
        if direction_states['Up'] == 0:
            print("Oben gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 1)
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 0)

        if direction_states['Down'] == 0:
            print("Unten gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 1)
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 0)

        if direction_states['Left'] == 0:
            print("Links gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 1)
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 0)

        if direction_states['Right'] == 0:
            print("Rechts gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 1)
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 0)

        # Tastereingaben für A, B, X, Y
        for button, state in button_states.items():
            if state == 0:
                print(f"{button} gedrückt!")
                if button == 'A':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
                elif button == 'B':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_B, 1)
                elif button == 'X':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_X, 1)
                elif button == 'Y':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_Y, 1)
            else:
                if button == 'A':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
                elif button == 'B':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_B, 0)
                elif button == 'X':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_X, 0)
                elif button == 'Y':
                    ui.write(ecodes.EV_KEY, ecodes.KEY_Y, 0)

        ui.syn()  # Synchronisieren der Eingaben
        time.sleep(0.1)  # Kurze Pause, um die CPU-Auslastung zu reduzieren

except KeyboardInterrupt:
    GPIO.cleanup()
