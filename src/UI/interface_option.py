from const import SCREEN_SIZE
from src.UI.button_title import ButtonTitle
from src.UI.interface import Interface
from src.UI.label import Label
from src.UI.button_enemies_number import ButtonEnemiesDecrease, ButtonEnemiesIncrease
from src.UI.label_enemies_number import LabelEnemiesNumber


class OPTION(Interface):
    def __init__(self):
        super().__init__(
            Label((SCREEN_SIZE[0]/20, SCREEN_SIZE[1]/6), 'Move Up:', is_left_center=True), Label((250, 100), 'W'),
            Label((SCREEN_SIZE[0]/20, SCREEN_SIZE[1]/6*2), 'Move Down:', is_left_center=True), Label((250, 200), 'S'),
            Label((SCREEN_SIZE[0]/20, SCREEN_SIZE[1]/6*3), 'Move Left:', is_left_center=True), Label((250, 300), 'A'),
            Label((SCREEN_SIZE[0]/20, SCREEN_SIZE[1]/6*4), 'Move Right:', is_left_center=True), Label((250, 400), 'D'),
            Label((SCREEN_SIZE[0]/20, SCREEN_SIZE[1]/6*5), 'Pick Up:', is_left_center=True), Label((250, 500), 'Space'),
            Label((SCREEN_SIZE[0]/32*11, SCREEN_SIZE[1]/6), 'Pause:', is_left_center=True),  Label((730, 100), 'Esc'),
            Label((SCREEN_SIZE[0]/32*11, SCREEN_SIZE[1]/6*2), 'Attack:', is_left_center=True),  Label((730, 200), 'Mouse Left'),
            Label((SCREEN_SIZE[0]/32*11, SCREEN_SIZE[1]/6*3), 'Reload:', is_left_center=True),  Label((730, 300), 'R'),
            Label((SCREEN_SIZE[0]/32*11, SCREEN_SIZE[1]/6*4), 'Enemies:', is_left_center=True),  LabelEnemiesNumber((730, 400)),
            ButtonEnemiesIncrease((SCREEN_SIZE[0]/32*11, SCREEN_SIZE[1]/2)), ButtonEnemiesDecrease((860, 400)),
            ButtonTitle((590, 500)))

