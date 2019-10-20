import logging
import sys
import time

from spaceapps.core.utils_drone_control import DroneControl

def clamp(n, minn, maxn): return max(min(maxn, n), minn)

drone = None
r = 127
p = 127
t = 127
y = 127
direction = 1

def _apply_clamp():
    r = clamp(r, 0, 255)
    p = clamp(p, 0, 255)
    t = clamp(t, 0, 255)
    y = clamp(y, 0, 255)

def _drone_rotate_left():
    y -= direction*30

def _drone_rotate_right():
    y += direction*30

def _drone_move_left():
    r -= direction*30

def _drone_move_right():
    r += direction*30

def _drone_move_front():
    p += direction*30

def _drone_move_back():
    p -= direction*30

def _drone_start():
    drone = DroneControl()
    drone.connect()

    airborne = False

    # video = DroneVideo()
    time.sleep(1.0)

    r = 127
    p = 127
    t = 0
    y = 127

def _drone_stop():
    drone.land()
    drone.stop()
    drone.disconnect()

def _drone_accelerate():
    t += 10

def _drone_decelerate():
    t -= 10