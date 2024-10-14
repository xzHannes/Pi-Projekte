import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode_win_de import Keycode

# Initialisiere die Tastatur
kbd = Keyboard(usb_hid.devices)

# Warte, bis der Computer bereit ist
time.sleep(1)

# Öffne das "Run"-Fenster
kbd.send(Keycode.WINDOWS, Keycode.R)
time.sleep(1)

# SSH-Befehl im Run-Fenster eingeben: ssh admin@169.254.103.252
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.SPACE)

# Benutzername "admin"
kbd.send(Keycode.A)
kbd.send(Keycode.D)
kbd.send(Keycode.M)
kbd.send(Keycode.I)
kbd.send(Keycode.N)

# Strg + Alt + Q für @-Zeichen auf deutschem Layout
kbd.press(Keycode.CONTROL)
kbd.press(Keycode.ALT)
kbd.send(Keycode.Q)
kbd.release(Keycode.CONTROL)
kbd.release(Keycode.ALT)

# IP-Adresse: 169.254.103.252
kbd.send(Keycode.ONE)
kbd.send(Keycode.SIX)
kbd.send(Keycode.NINE)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.TWO)
kbd.send(Keycode.FIVE)
kbd.send(Keycode.FOUR)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.ONE)
kbd.send(Keycode.ZERO)
kbd.send(Keycode.THREE)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.TWO)
kbd.send(Keycode.FIVE)
kbd.send(Keycode.TWO)

# Drücke Enter, um den Befehl auszuführen
kbd.send(Keycode.ENTER)
time.sleep(1)

# Passwort eingeben: admin
kbd.send(Keycode.A)
kbd.send(Keycode.D)
kbd.send(Keycode.M)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.ENTER)
time.sleep(1)

# Wechsle auf den Desktop
kbd.send(Keycode.C)
kbd.send(Keycode.D)
kbd.send(Keycode.SPACE)
kbd.press(Keycode.SHIFT)
kbd.send(Keycode.D)
kbd.release(Keycode.SHIFT)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.K)
kbd.send(Keycode.T)
kbd.send(Keycode.O)
kbd.send(Keycode.P)
kbd.send(Keycode.ENTER)
time.sleep(1)
