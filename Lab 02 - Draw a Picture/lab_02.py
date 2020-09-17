import arcade

arcade.open_window(800, 600, "Hills")

arcade.set_background_color(arcade.color.AERO_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 450, 0, arcade.color.GREEN)

# Middle Hill Outline
arcade.draw_arc_outline(400, 250, 400, 600, arcade.color.COOL_BLACK, 0, 180)
# Middle Hill Filled
arcade.draw_arc_filled(400, 250, 400, 600, arcade.color.GOLDEN_YELLOW, 0, 180)
# Middle Hill Bottom Outline
arcade.draw_line(400, 250, 550, 250, arcade.color.COOL_BLACK, 1)

# Left Hill Outline
arcade.draw_arc_outline(100, 80, 725, 675, arcade.color.COOL_BLACK, -200, 200)
arcade.draw_arc_filled(100, 80, 725, 675, arcade.color.RED_ORANGE, -200, 200)

# Right Hill Outline
arcade.draw_arc_outline(650, 20, 400, 600, arcade.color.COOL_BLACK, -200, 200)
# Right Hill Fill
arcade.draw_arc_filled(650, 20, 400, 600, arcade.color.APPLE_GREEN, -200, 200)

# Sun Filled
arcade.draw_arc_filled(800, 650, 300, 300, arcade.color.ORANGE_PEEL, -200, 200)
# Sun Beam 1
arcade.draw_triangle_filled(550, 500, 600, 450, 650, 570, arcade.color.RED)
# Sun Beam 2
arcade.draw_triangle_filled(650, 450, 700, 400, 700, 520, arcade.color.ORANGE_PEEL)
# Sun Beam 3
arcade.draw_triangle_filled(730, 375, 780, 375, 755, 475, arcade.color.RED)

arcade.finish_render()

arcade.run()

# # Middle Hill Outline
# arcade.draw_arc_outline(300, 300, 300, 300, arcade.color.COOL_BLACK, 0, 180)
#
# # Middle Hill Filled
# arcade.draw_arc_filled(300, 300, 300, 300, arcade.color.GOLDEN_YELLOW, -200, 200)