from src.UI.button_title import ButtonTitle
from src.UI.interface import Interface
from src.UI.label import Label
from src.UI.button_enemies_number import ButtonEnemiesDecrease, ButtonEnemiesIncrease
from src.UI.label_enemies_number import LabelEnemiesNumber


class OPTION(Interface):
    def __init__(self):
        super().__init__(
            Label((50, 100), 'Move Up:', is_left_center=True), Label((250, 100), 'W'),
            Label((50, 200), 'Move Down:', is_left_center=True), Label((250, 200), 'S'),
            Label((50, 300), 'Move Left:', is_left_center=True), Label((250, 300), 'A'),
            Label((50, 400), 'Move Right:', is_left_center=True), Label((250, 400), 'D'),
            Label((50, 500), 'Pick Up:', is_left_center=True), Label((250, 500), 'Space'),
            Label((530, 100), 'Pause:', is_left_center=True),  Label((730, 100), 'Esc'),
            Label((530, 200), 'Attack:', is_left_center=True),  Label((730, 200), 'Mouse Left'),
            Label((530, 300), 'Reload:', is_left_center=True),  Label((730, 300), 'R'),
            Label((530, 400), 'Enemies:', is_left_center=True),  LabelEnemiesNumber((730, 400)),
            ButtonEnemiesIncrease((800, 400)), ButtonEnemiesDecrease((860, 400)),
            ButtonTitle((590, 500)))

