import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x
        self.change_x
        self.radius
        self.color

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        arcade.start_render()
        # arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def on_update(self, delta_time):
        self.ball_x += 1
        self.ball_x += 1
        print(delta_time)


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()

main()