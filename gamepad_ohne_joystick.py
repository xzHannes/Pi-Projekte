import RPi.GPIO as GPIO
import time
from evdev import UInput, ecodes

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

# Richtungs-Taster konfigurieren
for pin in direction_pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up-Widerstände aktivieren

# Button-Taster konfigurieren
for pin in button_pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up-Widerstände aktivieren

# HID-Eingabegerät initialisieren (für die Richtungstasten und die Knöpfe)
ui = UInput()

def read_buttons():
    """Liest den Zustand der Richtungstasten und der Knöpfe (A, B, X, Y)"""
    direction_states = {}
    button_states = {}

    for direction, pin in direction_pins.items():
        state = GPIO.input(pin)  # 0 = gedrückt, 1 = nicht gedrückt
        direction_states[direction] = state

    for button, pin in button_pins.items():
        state = GPIO.input(pin)  # 0 = gedrückt, 1 = nicht gedrückt
        button_states[button] = state

    return direction_states, button_states

try:
    print("Taster Test gestartet. Drücke die Richtungstasten, A, B, X oder Y...")
    while True:
        directions, buttons = read_buttons()

        # Richtungstasten auswerten
        if directions['Up'] == 0:
            print("Oben gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 1)  # Hoch-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 0)  # Hoch-Taste loslassen

        if directions['Down'] == 0:
            print("Unten gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 1)  # Runter-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_DOWN, 0)  # Runter-Taste loslassen

        if directions['Left'] == 0:
            print("Links gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 1)  # Links-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_LEFT, 0)  # Links-Taste loslassen

        if directions['Right'] == 0:
            print("Rechts gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 1)  # Rechts-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_RIGHT, 0)  # Rechts-Taste loslassen

        # A, B, X, Y Buttons auswerten
        if buttons['A'] == 0:
            print("A gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_A, 1)  # A-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_A, 0)  # A-Taste loslassen

        if buttons['B'] == 0:
            print("B gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_B, 1)  # B-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_B, 0)  # B-Taste loslassen

        if buttons['X'] == 0:
            print("X gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_X, 1)  # X-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_X, 0)  # X-Taste loslassen

        if buttons['Y'] == 0:
            print("Y gedrückt!")
            ui.write(ecodes.EV_KEY, ecodes.KEY_Y, 1)  # Y-Taste gedrückt
        else:
            ui.write(ecodes.EV_KEY, ecodes.KEY_Y, 0)  # Y-Taste loslassen

        # Synchronisieren der Eingaben
        ui.syn()

        # Kurze Pause, um die CPU nicht zu überlasten
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Taster Test beendet.")

finally:
    GPIO.cleanup()  # GPIO-Pins aufräumen
    ui.close()  # UInput schließen
