from src.animation.animation_guard import AnimationGuardStandLeft, AnimationGuardStandRight, AnimationGuardMoveLeft, \
    AnimationGuardMoveRight
from src.animation.animation_mummy import AnimationMummyStandLeft, AnimationMummyStandRight, AnimationMummyMoveLeft, \
    AnimationMummyMoveRight
from src.animation.animation_pharaoh import AnimationPharaohStandLeft, AnimationPharaohStandRight, \
    AnimationPharaohMoveLeft, AnimationPharaohMoveRight
from src.animation.animation_player import AnimationPlayerStandLeft, AnimationPlayerStandRight, \
    AnimationPlayerMoveLeft, AnimationPlayerMoveRight
from src.animation.animation_trap import AnimationTrap
"""
Store all the animation instance.
"""


class AnimationRepository:
    def __init__(self):
        self.animations = {'player': {'stand_left': AnimationPlayerStandLeft(),
                                      'stand_right': AnimationPlayerStandRight(),
                                      'move_left': AnimationPlayerMoveLeft(),
                                      'move_right': AnimationPlayerMoveRight()},
                           'guard': {'stand_left': AnimationGuardStandLeft(),
                                     'stand_right': AnimationGuardStandRight(),
                                     'move_left': AnimationGuardMoveLeft(),
                                     'move_right': AnimationGuardMoveRight()},
                           'mummy': {'stand_left': AnimationMummyStandLeft(),
                                     'stand_right': AnimationMummyStandRight(),
                                     'move_left': AnimationMummyMoveLeft(),
                                     'move_right': AnimationMummyMoveRight()},
                           'pharaoh': {'stand_left': AnimationPharaohStandLeft(),
                                       'stand_right': AnimationPharaohStandRight(),
                                       'move_left': AnimationPharaohMoveLeft(),
                                       'move_right': AnimationPharaohMoveRight()},
                           'trap': {'work': AnimationTrap()}}
