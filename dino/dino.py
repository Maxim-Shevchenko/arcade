import arcade

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ДИНОЗАВРИК"


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
        self.cactus = Cactus("cactus2.png",0.5)
        self.score = 0




    # начальные значения
    def setup(self):
        self.dino.center_x = 100
        self.dino.center_y = 200
        self.cactus.center_x = SCREEN_WIDTH
        self.cactus.center_y = 200
        self.cactus.change_x = -15




    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.dino.draw()
        self.cactus.draw()
        score_text = f"Счет: {self.score}"
        arcade.draw_text(score_text, 350, 500, arcade.color.BLACK, 30)
        if arcade.check_for_collision(self.dino, self.cactus):
            game_over = f"GAME OVER"
            arcade.draw_text(game_over, 270, 400, arcade.color.WHITE, 50)




        # игровая логика
    def update(self, delta_time):
        self.dino.update_animation()
        self.dino.update()
        self.cactus.update()
        if arcade.check_for_collision(self.dino, self.cactus):
            self.cactus.stop()
            self.dino.stop()

        if self.cactus.center_x >= 800:
            self.score +=1


    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.dino.jump == False:
            self.dino.change_y = 12
            self.dino.jump = True


    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        pass


class Dino(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.5
        if self.center_y <= 200:
            self.center_y = 200
            self.jump = False

class Cactus(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.center_x <=0:
            self.center_x = SCREEN_WIDTH



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
