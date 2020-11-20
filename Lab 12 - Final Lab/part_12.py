import arcade

# Constants
SPRITE_SCALING_PIN = 0.01
SPRITE_SCALING_BALL = .3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_MODE_POWER = 1
GAME_MODE_DIRECTION = 2
GAME_MODE_BALL = 3

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Test")

        # Sprite Lists
        self.ball_list = None
        self.pin_list = None

        # Physics Engine
        self.physics_engine = None

    #     Power Level
        self.power = 0

    #     Direction
        self.direction = 0

    #   Game mode
        self.gamemode = GAME_MODE_POWER


    def setup(self):
        arcade.set_background_color(arcade.color.FRENCH_BEIGE)

        self.ball_list = arcade.SpriteList()
        self.pin_list = arcade.SpriteList()

        self.score = 0

        # Creating the ball
        # Ball_Bowling png is from Kenney.nl/assets/sports-pack but is currently not in use
        # Pink Bowling Ball and Green Bowling Ball are both from Clipart-library.com
        self.ball_sprite = arcade.Sprite("images/pink_bowling_ball.jpg", SPRITE_SCALING_BALL)
        self.ball_sprite.center_x = (SCREEN_WIDTH / 2)
        self.ball_sprite.center_y = 64
        self.ball_list.append(self.ball_sprite)

        # Creating Pins
        # Pin png is from pngkey.com/pngs/bowling-pin/
        pin = arcade.Sprite("images/bowling_pin.png", SPRITE_SCALING_PIN)
        pin.center_x = (SCREEN_WIDTH / 2)
        pin.center_y = (SCREEN_HEIGHT / 2)
        self.pin_list.append(pin)

        # # --- Place pins inside a loop
        # for x in range(173, 650, 64):
        #     pin = arcade.Sprite("images/bowling_pin.png", SPRITE_SCALING_PIN)
        #     pin.center_x = x
        #     pin.center_y = 350
        #     self.pin_list.append(pin)

        # --- Place pins with a list
        coordinate_list = [[SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150],
                           [SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/ 2 + 150],
                           [SCREEN_WIDTH/2 + 50, SCREEN_HEIGHT/ 2 + 150],
                           [SCREEN_WIDTH/2 - 25, SCREEN_HEIGHT/ 2 + 75],
                           [SCREEN_WIDTH/2 + 25, SCREEN_HEIGHT/ 2 + 75],
                           [SCREEN_WIDTH/2 - 25, SCREEN_HEIGHT/ 2 + 225],
                           [SCREEN_WIDTH/2 + 25, SCREEN_HEIGHT/ 2 + 225],
                           [SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT/ 2 + 225],
                           [SCREEN_WIDTH/2 + 75, SCREEN_HEIGHT/ 2 + 225],
                                ]

        # Loop through coordinates
        for coordinate in coordinate_list:
            pin = arcade.Sprite("images/bowling_pin.png", SPRITE_SCALING_PIN)
            pin.center_x = coordinate[0]
            pin.center_y = coordinate[1]
            self.pin_list.append(pin)

        # Creates the physics engine.
        self.physics_engine = arcade.PhysicsEngineSimple(self.ball_sprite, self.pin_list)

    def on_draw(self):
        arcade.start_render()
        self.pin_list.draw()
        self.ball_list.draw()

        # Power Meter
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 20, 200, 20, arcade.color.BLACK)
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 210 + (self.power / 300) * 100, SCREEN_HEIGHT - 20, (self.power / 300) * 200, 20, arcade.color.GREEN)

        # Direction Meter
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 50, 200, 20, arcade.color.BLACK)
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 210 + (self.direction / 300) * 100, SCREEN_HEIGHT - 50, (self.direction / 300) * 200, 20, arcade.color.GREEN)



    def update(self, delta_time):
        self.physics_engine.update()

        if self.gamemode == GAME_MODE_POWER:
            self.power +=5
            if self.power >= 300:
                self.power = 0

        if self.gamemode == GAME_MODE_DIRECTION:
            self.direction +=5
            if self.direction >= 300:
                self.direction = 0

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE and self.gamemode == GAME_MODE_POWER:
            self.gamemode = GAME_MODE_DIRECTION

        elif key == arcade.key.SPACE and self.gamemode == GAME_MODE_DIRECTION:
            self.gamemode = GAME_MODE_BALL
            print(self.power, self.direction)
            if self.power < 225:
                print ("You've got 8 pins.")
            elif self.power < 250:
                print ("You've got a strike!")
            else:
                print ("You've got a gutter ball.")

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()