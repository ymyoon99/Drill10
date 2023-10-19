from pico2d import *

import game_world
from grass import Grass
from boy import Boy


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def create_world(): # 초기의 세계를 만든다.
    global running
    global grass
    global team
    global boy

    running = True

    boy = Boy()  # 소년 객체 추가.
    game_world.add_object(boy, 1) # 레이어 추가

    grass = Grass()  # grass 객체 추가.
    game_world.add_object(grass, 0) # 맨뒤 레이어



def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
create_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
