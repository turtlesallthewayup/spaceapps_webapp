import logging
import sys
import time
import threading

from spaceapps.core.utils_drone_control import DroneControl

def clamp(n, minn, maxn): return max(min(maxn, n), minn)

class DroneKeyboard():
    def __init__(self):
        self.drone = None
        self.r = 127
        self.p = 127
        self.t = 127
        self.y = 127
        self.direction = 1
        self.connected = False
        
        #t = threading.Thread(target=self.keep_flying)
        #t.start()
        
    #def keep_flying(self):
        #while True:
            #if self.connected:
                #self._apply_clamp()
                #self._send_cmd()

    def _apply_clamp(self):
        if self.connected:
            self.r = clamp(self.r, 0, 255)
            self.p = clamp(self.p, 0, 255)
            self.t = clamp(self.t, 0, 255)
            self.y = clamp(self.y, 0, 255)
        
    def _send_cmd(self):
        if self.connected:
            self.drone.cmd(self.r, self.p, self.t, self.y)

    def _drone_rotate_left(self):
        if self.connected:
            print('DRONE ROTATE LEFT')
            self.y -= self.direction*30

    def _drone_rotate_right(self):
        if self.connected:
            print('DRONE ROTATE RIGHT')
            self.y += self.direction*30

    def _drone_move_left(self):
        if self.connected:
            print('DRONE MOVE LEFT')
            self.r -= self.direction*30

    def _drone_move_right(self):
        if self.connected:
            print('DRONE MOVE RIGHT')
            self.r += self.direction*30

    def _drone_move_front(self):
        if self.connected:
            print('DRONE MOVE FRONT')
            self.p += self.direction*30

    def _drone_move_back(self):
        if self.connected:
            print('DRONE MOVE BACK')
            self.p -= self.direction*30

    def _drone_start(self):
        if not self.connected:
            self.drone = DroneControl()
            self.drone.connect()

            self.airborne = False
            self.connected = True

            # video = DroneVideo()
            time.sleep(1.0)

            self.r = 127
            self.p = 127
            self.t = 30
            self.y = 127

    def _drone_stop(self):
        if self.connected:
            print('DRONE STOP')
            self.airborne = False
            self.drone.land()
            self.drone.stop()
            self.drone.disconnect()
            self.connected = False

    def _drone_accelerate(self):
        if self.connected:
            print('DRONE ACCELERATE')
            self.t += 10

    def _drone_decelerate(self):
        if self.connected:
            print('DRONE DECELERATE')
            self.t -= 10
    
# _apply_clamp()
# drone.cmd(r, p, t, y)
