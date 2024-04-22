import sys
import pygame
from hud import *
from players import *
from card import new_deck

BACKGROUND_COLOR = (53, 101, 77)

player = [Player("hazardzista"), Player("krupier")]


def bj_game_font(size):
    return pygame.font.SysFont('consolas', size)


def deck_empty(deck):
    return len(deck) == 0 or all(len(subdeck) == 0 for subdeck in deck)


def show_cards_info(screen):
    screen.fill(BACKGROUND_COLOR)
    gambler_hand = bj_game_font(12).render(str(player[0].cards_info()), True, (255, 255, 255))
    gambler_score = bj_game_font(34).render(str(player[0].score), True, (255, 255, 255))
    croupier_hand = bj_game_font(12).render(str(player[1].cards_info()), True, (255, 255, 255))
    screen.blit(gambler_hand, (240, 12))
    screen.blit(gambler_score, (120, 24))
    screen.blit(croupier_hand, (240, 36))


def end_game_screen(screen, score):
    while True:
        end_score = bj_game_font(56).render(str(player[0].score) + " vs " + str(player[1].score), True, (255, 255, 255))

        screen.fill(BACKGROUND_COLOR)
        screen.blit(end_score, ((1280 - end_score.get_width()) // 2, (720 - end_score.get_height()) // 2))

        button_quit = Button(image=None, position=(16, 24),
                             text="X", font=bj_game_font(48), color_normal="#d7fcd4", color_onclick="Gray")

        mouse_position = pygame.mouse.get_pos()
        for button in [button_quit]:
            button.change_color(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_quit.check_input(mouse_position):
                    return

        pygame.display.update()


def match(screen):
    # new game initalization
    game_status = 0
    game_deck = new_deck()
    player[0].throw_cards()
    player[1].throw_cards()
    player_turn = True

    screen.fill(BACKGROUND_COLOR)

    button_quit = Button(image=None, position=(16, 24),
                         text="X", font=bj_game_font(48), color_normal="#d7fcd4", color_onclick="Gray")
    hit_text_surface = bj_game_font(48).render("HIT", True, (255, 255, 255))
    button_hit = Button(image=None, position=((1280 - hit_text_surface.get_width()) // 2 - 50, 680),
                        text="HIT", font=bj_game_font(48), color_normal="#d7fcd4", color_onclick="Gray")
    stand_text_surface = bj_game_font(48).render("STAND", True, (255, 255, 255))
    button_stand = Button(image=None, position=((1280 + stand_text_surface.get_width()) // 2 + 50, 680),
                          text="STAND", font=bj_game_font(48), color_normal="#d7fcd4", color_onclick="Gray")
    if game_status == 0:
        print("GAME INFO: Croupier deals the cards")
        for i in range(0, 3):
            player[i % 2].add_card(game_deck, True)
            show_cards_info(screen)
            pygame.display.update()
            pygame.time.delay(1000)

        player[1].add_card(game_deck, False)
        print("Croupier recieved a card")
        pygame.time.delay(1000)

        game_status = 1

    pygame.display.update()

    while True:
        screen.fill(BACKGROUND_COLOR)
        show_cards_info(screen)

        mouse_position = pygame.mouse.get_pos()
        for button in [button_quit, button_hit, button_stand]:
            button.change_color(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_quit.check_input(mouse_position):
                    return
                if button_hit.check_input(mouse_position):
                    print("hit")
                    player[0].add_card(game_deck, True)

                    if player[0].score >= 21:
                        player_turn = False
                        pygame.time.delay(1000)

                if button_stand.check_input(mouse_position):
                    print("stand")
                    player_turn = False
                    pygame.time.delay(1000)

        if not player_turn:
            if not player[1].cards[1].visibility:
                player[1].cards[1].visibility = True
                show_cards_info(screen)
                pygame.display.update()
                pygame.time.delay(1000)

            while player[1].score < 17:
                pygame.time.delay(1000)
                player[1].add_card(game_deck, True)
                show_cards_info(screen)
                pygame.display.update()

            pygame.time.delay(2000)
            end_game_screen(screen, player[0].score)
            break
        pygame.display.update()


def blackjack_game(screen):
    while True:
        screen.fill(BACKGROUND_COLOR)

        button_quit = Button(image=None, position=(16, 24),
                             text="X", font=bj_game_font(48), color_normal="#d7fcd4", color_onclick="Gray")
        button_play = Button(image=None, position=(640, 460),
                             text="PLAY", font=bj_game_font(48), color_normal="#d7fcd4", color_onclick="Gray")

        mouse_position = pygame.mouse.get_pos()
        for button in [button_quit, button_play]:
            button.change_color(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_quit.check_input(mouse_position):
                    return
                if button_play.check_input(mouse_position):
                    match(screen)

        pygame.display.update()
