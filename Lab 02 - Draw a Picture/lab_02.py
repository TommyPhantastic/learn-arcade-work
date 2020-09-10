import arcade

arcade.open_window(800, 600, "Hills")

arcade.set_background_color(arcade.color.AERO_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 450, 0, arcade.color.GREEN)

# Left Hill
arcade.draw_arc_outline(100, 20, 50,300, arcade.color.COOL_BLACK, 20, 50)

# Middle Hill
arcade.draw_arc_outline(300, 20, 50, 400, arcade.color.COOL_BLACK, 20, 50)

# Right Hill
arcade.draw_arc_outline(500, 20, 50, 200, arcade.color.COOL_BLACK, 20, 50)

arcade.finish_render()

arcade.run()