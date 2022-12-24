from const import SCREEN_SIZE
from src.UI.button_title import ButtonTitle
from src.UI.interface import Interface
from src.UI.label import Label
from src.UI.button_enemies_number import ButtonEnemiesDecrease, ButtonEnemiesIncrease
from src.UI.label_enemies_number import LabelEnemiesNumber


class OPTION(Interface):
    def __init__(self):
        super().__init__(
            Label((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8), 'Move Up:', is_left_center=True), Label((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8), 'W'),
            Label((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8 * 2), 'Move Down:', is_left_center=True), Label((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8 * 2), 'S'),
            Label((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8 * 3), 'Move Left:', is_left_center=True), Label((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8 * 3), 'A'),
            Label((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8 * 4), 'Move Right:', is_left_center=True), Label((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8 * 4), 'D'),
            Label((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8 * 5), 'Pick Up:', is_left_center=True), Label((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8 * 5), 'Space'),
            Label((SCREEN_SIZE[0]/1.65, SCREEN_SIZE[1]/8), 'Pause:', is_left_center=True),  Label((SCREEN_SIZE[0]/1.3, SCREEN_SIZE[1]/8), 'Esc'),
            Label((SCREEN_SIZE[0]/1.65, SCREEN_SIZE[1]/8 * 2), 'Attack:', is_left_center=True),  Label((SCREEN_SIZE[0]/1.3, SCREEN_SIZE[1]/8 * 2), 'Mouse Left'),
            Label((SCREEN_SIZE[0]/1.65, SCREEN_SIZE[1]/8 * 3), 'Reload:', is_left_center=True),  Label((SCREEN_SIZE[0]/1.3, SCREEN_SIZE[1]/8 * 3), 'R'),
            Label((SCREEN_SIZE[0]/1.65, SCREEN_SIZE[1]/8 * 4), 'Enemies:', is_left_center=True),  LabelEnemiesNumber((SCREEN_SIZE[0]/1.308, SCREEN_SIZE[1]/8 * 4)),
            ButtonEnemiesDecrease((SCREEN_SIZE[0]/3 + SCREEN_SIZE[0]/3 * 1.18, SCREEN_SIZE[1]/8 * 4.3)),
            ButtonEnemiesIncrease((SCREEN_SIZE[0]/3 + SCREEN_SIZE[0]/3 * 1.18, SCREEN_SIZE[1]/8 * 3.65)),
            ButtonTitle((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/8 * 6)))