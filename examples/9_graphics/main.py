from cocos.scene import Scene
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions.interval_actions import *
import random

class Ball(Sprite):

    def __init__(self):
        super().__init__('Ball.png')
        width, height = director.get_window_size()
        self.x = 1/2*width #random.randint(0,500)
        self.y = 3/4*height #random.randint(0,500)
        target_x, target_y = random.randint(0,width), 0
        self.do( MoveTo((target_x,target_y),10) | RotateBy(random.randint(0,90),1) )

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        balls = [ Ball() for i in range(3,random.randint(5,8)) ]
        for b in balls:
            self.add(b)

director.init()
director.run(MainScene())
