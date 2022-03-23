import arcade
import random
import tkinter.messagebox as mb
# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Гонки с препятствиями"


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("background.png")
        self.car = Car("car.png", 0.6)



    # начальные значения
    def setup(self):
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = 100


    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.car.draw()




    # игровая логика
    def update(self, delta_time):
        self.car.update()



    # нажать на клавишу
    def on_key_press(self, key, modifiers):
      pass

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
      pass
class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x






window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()