import arcade

arcade.open_window(800, 600, "Hills")

arcade.set_background_color(arcade.color.AERO_BLUE)

arcade.start_render()

# Grass
arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.GREEN)

# Sun Filled
arcade.draw_arc_filled(800, 650, 300, 300, arcade.color.ORANGE_PEEL, -200, 200)
# Sun Beam 1
arcade.draw_triangle_filled(550, 500, 600, 450, 650, 570, arcade.color.RED)
# Sun Beam 2
arcade.draw_triangle_filled(650, 450, 700, 400, 700, 520, arcade.color.ORANGE_PEEL)
# Sun Beam 3
arcade.draw_triangle_filled(730, 375, 780, 375, 755, 475, arcade.color.RED)

def draw_rocks(x, y):
    # middle rock
    arcade.draw_arc_outline(400 + x, 250 + y, 80, 60, arcade.color.COOL_BLACK, 0, 180)
    arcade.draw_arc_filled(400 + x, 250 + y, 80, 60, arcade.color.DARK_SLATE_GRAY, 0, 180)
    # right rock
    arcade.draw_arc_outline(450 + x, 270 + y, 50, 40, arcade.color.COOL_BLACK, 0, 180)
    arcade.draw_arc_filled(450 + x, 270 + y, 50, 40, arcade.color.DARK_SLATE_GRAY, 0, 180)

draw_rocks(0, 0)
draw_rocks(200, - 200)
draw_rocks(-320, -100)

def draw_cloud(x, y):
    arcade.draw_ellipse_filled(100 + x, 600 + y, 200, 100, arcade.color.WHITE_SMOKE, 30)

draw_cloud(0, 0)
draw_cloud(100, -120)
draw_cloud(300, -100)

def draw_ball(x, y, z):
    arcade.draw_circle_filled(200 + x, 200 + y, 50 + z, arcade.color.RED_ORANGE)

draw_ball(0, 0, 0)
draw_ball(200, 170, -20)
draw_ball(400, -50, +20)

arcade.finish_render()

arcade.run()