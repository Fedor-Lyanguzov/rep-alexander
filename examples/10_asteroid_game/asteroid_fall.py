from cocos.scene import Scene
from cocos.director import director
from cocos.sprite import Sprite
from cocos.layer.base_layers import Layer
from cocos.actions.interval_actions import MoveBy, MoveTo
from cocos.actions.instant_actions import CallFunc, Place
from pyglet.window import key
import random

class Player(Sprite):
    def __init__(self):
        super().__init__("spacecraft.png")
        self.scale = 0.125
        self.x, self.y = director.get_window_size()
        self.x //= 2
        self.y = 40

class Asteroid(Sprite):        
    def __init__(self):
        super().__init__("meteorite.png")
        self.scale = 0.25
        width, height = director.get_window_size()
        x0 = random.randint(0, width)
        x1 = random.randint(0, width)
        self.x, self.y = x0, height
        self.do(MoveTo((x1,0),duration=random.randint(3,7)) + CallFunc(self.die))

    def die(self):
        gl = self.get_ancestor(GameLayer)
        gl.score += 1
        gl.remove(self)
        gl.asteroids.remove(self)
        gl.asteroids.extend([ Asteroid(), Asteroid()])
        for a in gl.asteroids:
            gl.add(a)
        

class GameLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.score = 0
        self.asteroids = [ Asteroid() for c in range(3) ]
        for a in self.asteroids:
            self.add(a)
        self.player = Player()
        self.add(self.player)
        
    def on_key_press(self, k, modifiers):
        if k == key.RIGHT: 
            self.player.do(MoveBy((15000,0),duration=100))
        if k == key.LEFT: 
            self.player.do(MoveBy((-15000,0), duration=100))

    def on_key_release(self, k, modifiers):
        self.player.stop()

class Background(Layer):
    def __init__(self):
        super().__init__()
        s = Sprite("bg.png")
        s.image_anchor = (0,0)
        self.add(s)

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.add(Background(), z=-1)
        self.add(GameLayer())

director.init(width=800, height=800)
director.run(MainScene())
