from pygame import draw
from setting import black

def draw_key_effect(screen, rect, is_pressed = False):
    if not is_pressed:
        base_color = (220,220,220)
    else:
        base_color = (170,220,255)
    border_color = black
    draw.rect(screen, base_color, rect, border_radius=8)
    draw.rect(screen, border_color, rect, 2, border_radius=8)