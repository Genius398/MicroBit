from microbit import *
import music

display.scroll(temperature())
display.scroll(display.read_light_level())
while True:
        if display.read_light_level() > 50 and temperature() > 10:
            display.show(Image('00900:'
                               '00900:'
                               '00900:'
                               '00000:'
                               '00900'))
            music.play(music.POWER_UP)
        
        else:
            display.scroll("All clear")
