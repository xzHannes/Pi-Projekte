import storage
import usb_hid

# Deaktiviere das USB-Laufwerk (Massenspeicher)
storage.disable_usb_drive()

# Aktiviere HID (Tastatur, Maus, etc.)
usb_hid.enable((usb_hid.Device.KEYBOARD,))
