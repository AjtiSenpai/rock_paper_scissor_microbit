def on_received_number(receivedNumber):
    global Ellenfél
    Ellenfél = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global anim, Saját
    if Accept == False:
        anim = 1
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        Saját = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def Összehasonlítás():
    global Nyertem
    if Saját == 1:
        if Ellenfél == 1:
            basic.show_icon(IconNames.ASLEEP)
        elif Ellenfél == 2:
            basic.show_icon(IconNames.SAD)
        else:
            basic.show_icon(IconNames.HAPPY)
            Nyertem += 1
    elif Saját == 2:
        if Ellenfél == 1:
            basic.show_icon(IconNames.HAPPY)
            Nyertem += 1
        elif Ellenfél == 2:
            basic.show_icon(IconNames.ASLEEP)
        else:
            basic.show_icon(IconNames.SAD)
    else:
        if Ellenfél == 1:
            basic.show_icon(IconNames.SAD)
        elif Ellenfél == 2:
            basic.show_icon(IconNames.HAPPY)
            Nyertem += 1
        else:
            basic.show_icon(IconNames.ASLEEP)

def on_gesture_shake():
    global Accept, anim2
    if Saját != 0:
        radio.send_number(Saját)
        Accept = True
        anim2 = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global anim, Saját
    if Accept == False:
        anim = 1
        basic.show_icon(IconNames.SCISSORS)
        Saját = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global anim, Saját
    if Accept == False:
        anim = 1
        basic.show_icon(IconNames.SQUARE)
        Saját = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

anim2 = 0
anim = 0
Saját = 0
Ellenfél = 0
Accept = False
Accept = False
Ellenfél = 0
Saját = 0
anim = 0
anim2 = 1
Nyertem = 0
radio.set_group(99)

def on_forever():
    global anim2, Ellenfél, Saját, Accept, anim
    if Accept == True and (not (Ellenfél == 0) and not (Saját == 0)):
        basic.pause(2000)
        anim2 = 1
        basic.pause(500)
        Összehasonlítás()
        Ellenfél = 0
        Saját = 0
        Accept = False
        basic.pause(5000)
        basic.show_number(Nyertem)
        basic.pause(5000)
        anim = 0
basic.forever(on_forever)

def on_forever2():
    if anim == 0:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        basic.pause(100)
    if anim == 0:
        basic.show_icon(IconNames.SQUARE)
        basic.pause(100)
    if anim == 0:
        basic.show_icon(IconNames.SCISSORS)
        basic.pause(100)
basic.forever(on_forever2)

def on_forever3():
    if anim2 == 0:
        basic.pause(100)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        . # . # .
                        # . . . #
                        # # # # #
        """)
    if anim2 == 0:
        basic.pause(100)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        . # # # .
                        # . . . #
                        # # # # #
        """)
    if anim2 == 0:
        basic.pause(100)
        basic.show_leds("""
            # # # # #
                        # . # . #
                        . # # # .
                        # . # . #
                        # # # # #
        """)
    if anim2 == 0:
        basic.pause(100)
        basic.show_leds("""
            # # # # #
                        # . . . #
                        . # # # .
                        # # # # #
                        # # # # #
        """)
    if anim2 == 0:
        basic.pause(100)
        basic.show_leds("""
            # # # # #
                        # . . . #
                        . # . # .
                        # # # # #
                        # # # # #
        """)
    if anim2 == 0:
        basic.pause(100)
        basic.show_leds("""
            # # . # #
                        # . # # #
                        # . . # #
                        # . # # #
                        # # . # #
        """)
basic.forever(on_forever3)