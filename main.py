import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.properties import ObjectProperty

class Paddle(Widget):
    pass

class PongBall(Widget):
    vx=NumericProperty(4)
    vy=NumericProperty(4)
    def Move(self,*args):
        self.pos[0]=self.pos[0] + self.vx
        self.pos[1]=self.pos[1] + self.vy

class PongGame(Widget):
    ball=ObjectProperty()
    def Update(self,*args):
        #move the ball
        self.ball.Move()
        #bouncing off the top and the bottom
        if self.ball.top>=self.top or self.ball.y<=self.y:
            self.ball.vy*=-1

        #bouncing off left and right
        if self.ball.right>=self.right or self.ball.x<=self.x:
            self.ball.vx*=-1

class PongApp(App):
    def build(self):
        g=PongGame()
        Clock.schedule_interval(g.Update,1/60)
        return g

if __name__=="__main__":
    PongApp().run()