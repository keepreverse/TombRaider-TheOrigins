import pygame
import var
import const
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
from src.UI.label_debuff import LabelDebuffName, LabelDebuffTime
from src.UI.label_bullet import LabelBullet
from src.UI.label_hp import LabelHP
from src.UI.label_information import LabelInformationName, LabelInformation1, LabelInformation2, LabelInformation3, \
    LabelInformationType
from src.UI.label_item import LabelItem
from src.UI.label_weapon import LabelWeaponName, LabelWeaponDamage, LabelWeaponReload, LabelWeaponInterval


class PAUSE(Interface):
    def __init__(self):
        super().__init__()
        self.__profile = [Image((SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/8), const.IMAGE['pause'][0]),
                          ImagePlayerBackground(),
                          ImagePlayer((160, 135)), LabelHP((240, 95)), LabelBullet((240, 125)),
                          LabelDebuffName((240, 155)), LabelDebuffTime((240, 185))]
        self.__equipment = [Image((SCREEN_SIZE[0]/6 + SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8), const.IMAGE['pause'][1]),
                            ImageArmorBackground((775, 175)), ImageArmor((775, 175)),
                            ImageWeaponBackground((775, 85)), ImageWeapon((775, 85)),
                            LabelArmorName((830, 155)), LabelArmorDefense((830, 185)),
                            LabelWeaponName((830, 55)), LabelWeaponDamage((830, 75)),
                            LabelWeaponReload((830, 95)), LabelWeaponInterval((830, 115))]
        self.__bag = [Image((SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/8 + SCREEN_SIZE[1]/4), const.IMAGE['pause'][2]), *[ButtonItem(i) for i in range(8)],
                      *[ImageItem(i) for i in range(8)], *[LabelItem(i) for i in range(8)],
                      ButtonUse((1100, 370)), ButtonDrop((1100, 440))]
        self.__information = [Image((SCREEN_SIZE[0]/3, SCREEN_SIZE[1] - SCREEN_SIZE[1]/4), const.IMAGE['pause'][3]),
                              ImageBackground((130, 650), (70, 70), (60, 60, 60), True),
                              ImageActiveItem((130, 650)), LabelInformationName((200, 635)),
                              LabelInformationType((200, 670)), LabelInformation1((100, 750)),
                              LabelInformation2((100, 780)), LabelInformation3((100, 800))]
        self.__map = [Image((SCREEN_SIZE[0] - SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/4), const.IMAGE['pause'][4]), ImageMap((SCREEN_SIZE[0] - SCREEN_SIZE[0]/12 * 2, 260))]
        self.__button = [Image((SCREEN_SIZE[0] - SCREEN_SIZE[0]/6, SCREEN_SIZE[1] - SCREEN_SIZE[1]/4), const.IMAGE['pause'][5]),
                         ButtonContinue((1520, 750)), ButtonTitle((1680, 800)), ButtonRestart((1520, 850))]

        #self.__profile[0].image.fill((30, 30, 30))
        # self.__equipment[0].image.fill((200, 200, 200))
        # self.__bag[0].image.fill((100, 100, 100))
        # self.__information[0].image.fill((30, 30, 30))
        # self.__map[0].image.fill((60, 60, 60))
        # self.__map[1].image.fill((140, 140, 140))
        # self.__button[0].image.fill((55, 55, 55))

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