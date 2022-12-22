import pygame
import var
from const import SCREEN_SIZE
from src.UI.button_continue import ButtonContinue
from src.UI.button_drop import ButtonDrop
from src.UI.button_item import ButtonItem
from src.UI.button_restart import ButtonRestart
from src.UI.button_title import ButtonTitle
from src.UI.button_use import ButtonUse
from src.UI.image import Image
from src.UI.image_active_item import ImageActiveItem
from src.UI.image_armor import ImageArmor
from src.UI.image_armor_background import ImageArmorBackground
from src.UI.image_background import ImageBackground
from src.UI.image_item import ImageItem
from src.UI.image_map import ImageMap
from src.UI.image_player import ImagePlayer
from src.UI.image_player_background import ImagePlayerBackground
from src.UI.image_weapon import ImageWeapon
from src.UI.image_weapon_background import ImageWeaponBackground
from src.UI.interface import Interface
from pygame.surface import Surface
from src.UI.label_armor import LabelArmorName, LabelArmorDefense
from src.UI.label_buff import LabelBuffName, LabelBuffTime
from src.UI.label_bullet import LabelBullet
from src.UI.label_hp import LabelHP
from src.UI.label_information import LabelInformationName, LabelInformation1, LabelInformation2, LabelInformation3, \
    LabelInformationType
from src.UI.label_item import LabelItem
from src.UI.label_weapon import LabelWeaponName, LabelWeaponDamage, LabelWeaponReload, LabelWeaponInterval


class PAUSE(Interface):
    def __init__(self):
        super().__init__()
        self.__profile = [Image((160, 100), Surface((320, 200))),
                          ImagePlayerBackground(),
                          ImagePlayer((80, 100)), LabelHP((160, 55)), LabelBullet((160, 85)),
                          LabelBuffName((160, 115)), LabelBuffTime((160, 145))]
        self.__equipment = [Image((480, 100), Surface((320, 200))),
                            ImageArmorBackground((375, 145)), ImageArmor((375, 145)),
                            ImageWeaponBackground((375, 55)), ImageWeapon((375, 55)),
                            LabelArmorName((430, 115)), LabelArmorDefense((430, 135)),
                            LabelWeaponName((430, 25)), LabelWeaponDamage((430, 45)),
                            LabelWeaponReload((430, 65)), LabelWeaponInterval((430, 85))]
        self.__bag = [Image((320, 300), Surface((640, 200))), *[ButtonItem(i) for i in range(8)],
                      *[ImageItem(i) for i in range(8)], *[LabelItem(i) for i in range(8)],
                      ButtonUse((510, 250)), ButtonDrop((510, 350))]
        self.__information = [Image((320, 520), Surface((640, 240))),
                              ImageBackground((50, 450), (70, 70), (150, 150, 150), True),
                              ImageActiveItem((50, 450)), LabelInformationName((100, 435)),
                              LabelInformationType((100, 470)), LabelInformation1((20, 510)),
                              LabelInformation2((20, 540)), LabelInformation3((20, 570))]
        self.__map = [Image((800, 160), Surface((320, 320))), ImageMap((800, 160))]
        self.__button = [Image((800, 480), Surface((320, 320))),
                         ButtonContinue((720, 400)), ButtonTitle((880, 400)), ButtonRestart((720, 560))]

        self.__profile[0].image.fill((255, 100, 255))
        self.__equipment[0].image.fill((100, 100, 255))
        self.__bag[0].image.fill((100, 255, 255))
        self.__information[0].image.fill((255, 255, 255))
        self.__map[0].image.fill((255, 255, 100))
        self.__map[1].image.fill((0, 0, 0))
        self.__button[0].image.fill((100, 255, 100))

        self.__surface = Surface(SCREEN_SIZE)
        self.__update_list = [self.__profile, self.__equipment, self.__bag, self.__information, self.__map, self.__button]

    @property
    def profile(self):
        return self.__profile

    @property
    def equipment(self):
        return self.__equipment

    @property
    def bag(self):
        return self.__bag

    @property
    def information(self):
        return self.__information

    @property
    def map(self):
        return self.__map

    @property
    def button(self):
        return self.__button

    @property
    def update_list(self):
        return self.__update_list

    def refresh(self):
        # Refresh all the parts.
        self.__update_list = [self.__profile, self.__equipment, self.__bag, self.__information, self.__map, self.__button]
        for component_list in self.__update_list:
            for component in component_list:
                component.update()

    def update(self):
        # Update when mouse click something.
        if len(var.mouse_down) > 0:
            self.__update_list.append(self.__bag)
            self.__update_list.append(self.__information)
            self.__update_list.append(self.__equipment)
        for event in var.key_down:
            if event.key == pygame.K_ESCAPE:
                var.interface = var.play
        for component_list in self.__update_list:
            for component in component_list:
                component.update()

    def draw(self, surface):
        for component_list in self.__update_list:
            for component in component_list:
                component.draw(self.__surface)
        surface.blit(self.__surface, (0, 0))
        self.__update_list.clear()
        self.__update_list.append(self.__profile)
        self.__update_list.append(self.__button)
        # Update when mouse click something.
        if len(var.mouse_down) > 0:
            self.__update_list.append(self.__bag)
            self.__update_list.append(self.__information)
            self.__update_list.append(self.__equipment)

