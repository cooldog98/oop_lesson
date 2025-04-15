import sys
import pygame

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class StartScreen:
    def __init__(self):
        self.running = True
        self.player_name = ""
        self.bg_image = pygame.image.load("assets/login_bg.jpg")  #  path to background image
        self.bg_image = pygame.transform.scale(self.bg_image,
                                               (screen_width, screen_height))  #  scale to screen size
        self.font = pygame.font.SysFont('Arial', 40)

    def prompt_for_name(self):
        text = ''
        font = pygame.font.SysFont('Arial', 40)
        # screen.blit(self.bg_image, (0, 0)) # draw background
        # txt_surface = font.render(text, True, BLACK) #make a tzt box and label
        input_box = pygame.Rect(400, 400, 300, 50)
        color_inactive = pygame.Color('lightskyblue')
        color_active = pygame.Color('dodgerblue')
        color = color_inactive
        active = False
        clock = pygame.time.Clock()

        # screen.blit(self.bg_image, (0, 0)) # draw background
        # txt_surface = font.render(text, True, BLACK) #make a tzt box and label

        while True:
            # screen.blit(self.bg_image, (0, 0))
            # txt_surface = font.render(text, True, BLACK)  # make a tzt box and label
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                        color = color_active if active else color_inactive
                    else:
                        active = False
                        color = color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            self.player_name = text  # Save player name when hitting Enter
                            return self.player_name
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            # Draw everything
            screen.blit(self.bg_image, (0, 0))  # draw background
            txt_surface = font.render(text, True, WHITE)  # make a tzt box and label
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)

            start_button = pygame.Rect(330, 315, 350, 70)
            pygame.draw.rect(screen, BLACK, start_button)
            start_text = font.render("Enter your name:", True, WHITE)
            screen.blit(start_text, (350, 330))
            # pygame.draw.rect(screen, BLACK, start_text)

            pygame.display.update()
            clock.tick(30)

    def display(self):
        # input_box = pygame.Rect((screen_width - 400) // 2, 350, 400, 60)
        # color_inactive = pygame.Color('lightskyblue')
        # color_active = pygame.Color('dodgerblue')
        # color = color_inactive
        # text = ''
        # font = pygame.font.SysFont('Arial', 40)
        while self.running:
            """make background"""
            screen.blit(self.bg_image, (0, 0))

            # Title
            start_button = pygame.Rect(340, 170, 320, 70)
            pygame.draw.rect(screen, BLACK, start_button)
            title_text = self.font.render('Enjoy the game', True, WHITE)
            title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
            screen.blit(title_text, title_rect)

            # # Input prompt
            # prompt_text = font.render("Enter your name:", True, BLACK)
            # screen.blit(prompt_text, (input_box.x, input_box.y - 50))
            #
            # # Input box
            # txt_surface = font.render(text, True, BLACK)
            # input_box.w = max(300, txt_surface.get_width() + 20)
            # pygame.draw.rect(screen, color, input_box, 2)
            # screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))

            # Start Button
            # pygame.Rect()
            start_button = pygame.Rect((screen_width - 300) // 2, 600, 300, 50)
            pygame.draw.rect(screen, GREEN, start_button)
            start_text = self.font.render('Start Game', True, BLACK)
            start_text_rect = start_text.get_rect(center=start_button.center)
            screen.blit(start_text, start_text_rect)

            # Exit Button
            exit_button = pygame.Rect((screen_width - 300) // 2, 670, 300, 50)
            pygame.draw.rect(screen, GREEN, exit_button)
            exit_text = self.font.render('Exit Game', True, BLACK)
            exit_text_rect = exit_text.get_rect(center=exit_button.center)
            screen.blit(exit_text, exit_text_rect)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button.collidepoint(mouse_pos):
                        player_name = self.prompt_for_name()
                        print(f"Starting game with player: {player_name}")
                        return player_name  # Pass player name to the game loop
                    elif exit_button.collidepoint(mouse_pos):
                        print("Exiting game")
                        pygame.quit()
                        sys.exit()

                pygame.display.update()