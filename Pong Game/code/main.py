import sys # 1. Import sys at the top
from settings import *
from sprites import *
import json
from groups import Allsprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption('pong')
        icon_image = pygame.image.load(join('icon','icon.png'))
        pygame.display.set_icon(icon_image) 
        self.clock = pygame.time.Clock()
        self.running = True

        #  sprites
        self.all_sprites = Allsprites()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites)) 
        self.ball = Ball(self.all_sprites, self.paddle_sprites, self.update_score)
        Opponent((self.all_sprites,self.paddle_sprites))

        #  scorre
        try:
            with open (join('data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:    
            self.score = {'player': 0 , 'opponent': 0}
        self.font = pygame.font.Font(None,160)

    def display_score(self):
        # player
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg ditail'])
        player_rect = player_surf.get_frect(center = (WINDOWS_WIDTH/2 + 100, WINDOWS_HEIGHT/2 ))
        self.display_surface.blit(player_surf,player_rect)
        # opponent
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg ditail'])
        opponent_rect = opponent_surf.get_frect(center = (WINDOWS_WIDTH/2 - 100, WINDOWS_HEIGHT/2 ))
        self.display_surface.blit(opponent_surf,opponent_rect)

        # line
        pygame.draw.line(self.display_surface,COLORS['bg ditail'],(WINDOWS_WIDTH/2, 0),(WINDOWS_WIDTH/2, WINDOWS_HEIGHT),5)

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data', "score.txt"), 'w') as score_file:
                        json.dump(self.score,score_file)

            # update
            self.all_sprites.update(dt)
            # draw

            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            pygame.display.update()


        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()