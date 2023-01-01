import pygame ,os,time, random, math
from states.state import State
from _assets.Character import *
from states.pause_menu import PauseMenu

class Game_World(State):
    def __init__(self,game):
        State.__init__(self,game)
        self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir,"images","ฺBackground_N.jpg"))
        self.grass_img = pygame.transform.scale(self.grass_img, (game.SCREEN_WIDTH,game.SCREEN_HEIGHT)) 
        self.player = Player(self.game)
        self.window_w,  self.window_h = game.SCREEN_WIDTH, game.SCREEN_HEIGHT
        #
        self.numofFood = random.randint(1, 3)
        self.food_x_pos, self.food_y_pos = random.randint(1, self.window_w-60), random.randint(1, self.window_h -60)
        self.apple = pygame.image.load(os.path.join(self.game.assets_dir, "images", "Apple.png"))
        self.apple = pygame.transform.scale(self.apple, (25,25))
        self.scoreP1, self.scoreP2 = 0, 0

    def update(self, delta_time, actions):
        
        if((self.player.snake.x > self.window_w or self.player.snake.x < -40)  or (self.player.snake.y > self.window_h or self.player.snake.y < -40)):
            new_state = PauseMenu(self.game, "Blue", self.player.snake2.blue)
            new_state.enter_state()
        if((self.player.snake2.x > self.window_w or self.player.snake2.x < -40) or (self.player.snake2.y > self.window_h or self.player.snake2.y  < -40)):
            new_state = PauseMenu(self.game, "Black", self.player.snake.black)
            new_state.enter_state()

        self.player.update(delta_time,actions)
        self.fighting()
        print("P1 ", self.player.snake.sizeW, "score ",self.player.snake.score)
       

    def render(self, display):
        display.blit(self.grass_img, (0,0))
        self.spwan_food(display)
        self.player.render(display)
        self.scoerBoard(display, self.scoreP1, self.scoreP2)
        

    def spwan_food(self,display):
        display.blit(self.apple, (self.food_x_pos, self.food_y_pos))

        if (0 <= self.CalculateDistance(self.player.snake.x, self.food_x_pos, self.player.snake.y, self.food_y_pos) < 12):
            display.blit(self.apple, (self.food_x_pos, self.food_y_pos))
            self.food_x_pos, self.food_y_pos = random.randint(1, self.window_w - 60), random.randint(1, self.window_h - 60)
            self.scoreP1 += 5
            self.player.snake.score += 5

        if (0 <= self.CalculateDistance(self.player.snake2.x, self.food_x_pos, self.player.snake2.y, self.food_y_pos) < 10):
            display.blit(self.apple, (self.food_x_pos, self.food_y_pos))   
            self.food_x_pos, self.food_y_pos = random.randint(1, self.window_w - 60), random.randint(1, self.window_h - 60)
            self.scoreP2 += 5
            self.player.snake2.score +=self.scoreP2
            self.player.snake2.sizeW += 0.21
            self.player.snake2.sizeH += 0.21

    def fighting (self):
        if (self.CalculateDistance(self.player.snake.x, self.player.snake2.x, self.player.snake.y,self.player.snake2.y) < 12):
            if (self.player.snake.score > self.player.snake2.score):
                time.sleep(2)
                new_state = PauseMenu(self.game, "Black", self.player.snake.black)
                new_state.enter_state()
               # del self.player.snake
            if (self.player.snake.score < self.player.snake2.score):
                time.sleep(2)
                new_state = PauseMenu(self.game, "Blue", self.player.snake2.blue)
                new_state.enter_state()
                #del self.player.snake2

   

    def scoerBoard(self,display, scoreP1, scoreP2):    
        score_font = pygame.font.SysFont('System Bold', 25)
        value1 = score_font.render("Your Score: " + str(scoreP1), True, self.player.snake.black)
        display.blit(value1, (self.window_w/11,  self.window_h/2 - 360))
        value2 = score_font.render("Your Score: " + str(scoreP2), True, self.player.snake2.blue)
        display.blit(value2, (self.window_w/1.2,  self.window_h/2 - 360))
    
    def CalculateDistance(self, x1,x2,y1,y2):
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return distance
        

class Player():
    def __init__(self,game):
        self.game = game
        
        self.position_x, self.position_y = 200,200
        self.current_frame, self.last_frame_update = 0,0
        self.xsnake_1, self.ysnake_1,self.direction_1 = 200, 200, "right"
        self.xsnake_2, self.ysnake_2, self.direction_2 = 300, 200,"down"

        self.sizeSnake1_W, self.sizeSnake1_H,= 0,0
        self.sizeSnake2_W, self.sizeSnake2_H,= 0,0
        self.snake, self.snake2 = SNAKE_1(self.xsnake_1, self.ysnake_1), SNAKE_2(self.xsnake_2, self.ysnake_2)    


    def update(self,delta_time, actions): 
        
        if not pygame.event.get():        
            self.snake.draw(self.movement_snake1(actions))
            self.snake2.draw(self.movement_snake2(actions))
        

    def render(self, display):
        display.blit(self.snake.snake_body_1, (self.snake.x, self.snake.y))
        # snake_2    
        display.blit(self.snake2.snake_body_2, (self.snake2.x, self.snake2.y))

    def movement_snake1(self, actions):
        if (actions["up"] == True):
            self.direction_1 = "up"
           
        elif (actions["down"] == True):
            self.direction_1 = "down"
            
        elif (actions["left"] == True):
            self.direction_1 = "left"
           
        elif (actions["right"] == True):
            self.direction_1 = "right"

        return self.direction_1
    
    def movement_snake2(self, actions):
        if (actions["up_arrow"] == True):
            self.direction_2 = "up"
           
        elif (actions["down_arrow"] == True):
            self.direction_2 = "down"
            
        elif (actions["left_arrow"] == True):
            self.direction_2 = "left"
           
        elif (actions["right_arrow"] == True):
            self.direction_2 = "right"

        return self.direction_2
           