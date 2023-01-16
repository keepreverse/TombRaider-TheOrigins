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
        self.__profile = [Image((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8), Surface((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/4))),
                          ImagePlayerBackground(),
                          ImagePlayer((80, 135)), LabelHP((160, 95)), LabelBullet((160, 125)),
                          LabelBuffName((160, 155)), LabelBuffTime((160, 185))]
        self.__equipment = [Image((SCREEN_SIZE[0]/6 + SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8), Surface((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/4))),
                            ImageArmorBackground((775, 175)), ImageArmor((775, 175)),
                            ImageWeaponBackground((775, 85)), ImageWeapon((775, 85)),
                            LabelArmorName((830, 150)), LabelArmorDefense((830, 170)),
                            LabelWeaponName((830, 55)), LabelWeaponDamage((830, 75)),
                            LabelWeaponReload((830, 95)), LabelWeaponInterval((830, 115))]
        self.__bag = [Image((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8 + SCREEN_SIZE[1]/4), Surface((SCREEN_SIZE[0]/1.5, SCREEN_SIZE[1]/4))), *[ButtonItem(i) for i in range(8)],
                      *[ImageItem(i) for i in range(8)], *[LabelItem(i) for i in range(8)],
                      ButtonUse((510, 350)), ButtonDrop((510, 450))]
        self.__information = [Image((SCREEN_SIZE[0]/3, SCREEN_SIZE[1] - SCREEN_SIZE[1]/4), Surface((SCREEN_SIZE[0]/1.5, SCREEN_SIZE[1] - SCREEN_SIZE[1]/4 * 2))),
                              ImageBackground((50, 750), (70, 70), (150, 150, 150), True),
                              ImageActiveItem((50, 750)), LabelInformationName((100, 735)),
                              LabelInformationType((100, 770)), LabelInformation1((20, 810)),
                              LabelInformation2((20, 840)), LabelInformation3((20, 870))]
        self.__map = [Image((SCREEN_SIZE[0] - SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/4), Surface((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/2))), ImageMap((SCREEN_SIZE[0] - SCREEN_SIZE[0]/12 * 2, 260))]
        self.__button = [Image((SCREEN_SIZE[0] - SCREEN_SIZE[0]/6, SCREEN_SIZE[1] - SCREEN_SIZE[1]/4), Surface((SCREEN_SIZE[0]/3, SCREEN_SIZE[1] - SCREEN_SIZE[1]/4 * 2))),
                         ButtonContinue((1520, 750)), ButtonTitle((1680, 800)), ButtonRestart((1520, 850))]

        self.__profile[0].image.fill((45, 45, 45))
        self.__equipment[0].image.fill((65, 65, 65))
        self.__bag[0].image.fill((90, 90, 90))
        self.__information[0].image.fill((60, 60, 60))
        self.__map[0].image.fill((120, 120, 120))
        self.__map[1].image.fill((200, 200, 200))
        self.__button[0].image.fill((80, 80, 80))

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

