import arcade
class OurPicture(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_circle_filled(300, 300, 200, arcade.color.YELLOW)
        arcade.draw_circle_filled(380, 350, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(220, 350, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(280, 280, 10, arcade.color.BLUEBERRY)
        arcade.draw_circle_filled(320, 280, 10, arcade.color.BLUEBERRY)
        center_x = 300
        center_y = 230
        width = 150
        height = 80
        start_angle = 180
        end_angle = 360
        line_width = 10
        arcade.draw_arc_outline(center_x, center_y, width, height, arcade.color.BLACK, start_angle, end_angle, line_width)













window = OurPicture(600,600,"Смайлик")
arcade.run()