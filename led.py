import time
import board
import neopixel

# Anzahl der LEDs auf dem Streifen
NUM_LEDS = 144

# Initialisiere den LED-Streifen
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=0.1, auto_write=False)

# Farben für den Farbverlauf
color_palette = [
    (255, 0, 0),    # Rot
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Gelb
    (0, 255, 0),    # Grün
    (0, 0, 255),    # Blau
    (75, 0, 130),   # Indigo
    (148, 0, 211)   # Violett
]

def running_leds():
    for i in range(NUM_LEDS):
        # Bestimme die Farbe für die aktuelle LED aus der Farbpalette
        color = color_palette[i % len(color_palette)]
        
        # Diese LED läuft von der Position 0 bis zur Position (NUM_LEDS - 1 - i)
        for position in range(NUM_LEDS - 1 - i + 1):
            # Setze die LED auf ihre Farbe
            pixels[position] = color
            
            # Aktualisiere den Streifen
            pixels.show()
            
            # Lösche die vorherige LED, falls es nicht die Startposition ist
            if position > 0:
                pixels[position - 1] = (0, 0, 0)
            
            time.sleep(0.02)  # Geschwindigkeit der Animation

        # Wenn die LED ihre Endposition erreicht hat, bleibt sie stehen
        pixels[NUM_LEDS - 1 - i] = color
        pixels.show()

    # Am Ende bleiben alle LEDs in einem Farbverlauf statisch an
    time.sleep(1)  # Halte das Ergebnis für 1 Sekunde

try:
    running_leds()
except KeyboardInterrupt:
    # Setze alle LEDs aus, wenn das Programm abgebrochen wird
    pixels.fill((0, 0, 0))
    pixels.show()
