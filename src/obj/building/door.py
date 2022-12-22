import var
from src.obj.building.trigger_building import TriggerBuilding
"""
If it's closed, player can't get through it.
If Player has key and collide with it, it will be open.
If it's opened, player can get through it.
When you set the can_access attribute to True, when player collide with it, it will be opened without using key. 
"""


class Door(TriggerBuilding):
    def __init__(self, pos, closed_image, opened_image):
        super().__init__(pos, closed_image, (0, -24), False, False, opened_image, (0, -24))

    def on_trigger(self, entity):
        if entity != var.player:
            return
        # If it's can_access was set to be True before player collide with it, it will open directly.
        elif self.can_access is True:
            self.can_trigger = False
            self.image = self.new_image
            self.vector = self.new_vector
        # Using key to open the door.
        elif self.can_trigger is True:
            if not var.bag.has_key:
                return
            # Check if the player has key and use it to open the door.
            for item in var.bag.items:
                if item.name == 'Key':
                    item.amount -= 1
                    self.can_trigger = False
                    self.can_access = True
                    self.image = self.new_image
                    self.vector = self.new_vector

