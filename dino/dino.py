import arcade

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Динозавр"


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("desert.png")
        self.dino = Dino(0.5)
        self.dino.textures = []
        self.dino.textures.append(arcade.load_texture("dino1.png"))
        self.dino.textures.append(arcade.load_texture("dino2.png"))
        self.dino.textures.append(arcade.load_texture("dino3.png"))

    # начальные значения
    def setup(self):
        self.dino.center_x = 100
        self.dino.center_y = 200

        # отрисовка

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.dino.draw()

    # игровая логика
    def update(self, delta_time):
        self.dino.update_animation()
        self.dino.update()

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        pass

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        pass


class Dino(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
