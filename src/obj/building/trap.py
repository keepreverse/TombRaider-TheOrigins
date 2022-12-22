import const
import var
from src.animation.animation_system import AnimationSystem
from src.buff.buff_slow import BuffSlow
from src.obj.building.trigger_building import TriggerBuilding
"""
It's the only building who has an animation.
When it shows the whole spine, it will hurt player and give a slow buff if player walk on it.
It makes no sense for the monster. 
"""


class Trap(TriggerBuilding):
    def __init__(self, pos):
        super().__init__(pos, None, (0, 0), True, False, None, (0, 0))
        self.__animation_system = AnimationSystem(**const.ANIMATION_REPOSITORY.animations['trap'])
        self.__animation_system.play('work')

    def update(self):
        self.__animation_system.update()
        self.image = self.__animation_system.image

    def on_trigger(self, entity):
        # Only player get hurt.
        if entity != var.player or self.image != const.IMAGE['trap'][3]:
            return
        var.player.take_damage(1)
        var.player.buff = BuffSlow(100, var.player, 3)
