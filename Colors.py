from collections import namedtuple
import random
import re

Color = namedtuple('Color', '  R     G     B')

tunic_colors = {
    "Kokiri Green":      Color(0x1E, 0x69, 0x1B),
    "Goron Red":         Color(0x64, 0x14, 0x00),
    "Zora Blue":         Color(0x00, 0x3C, 0x64),
    "Black":             Color(0x30, 0x30, 0x30),
    "White":             Color(0xF0, 0xF0, 0xFF),
    "Azure Blue":        Color(0x13, 0x9E, 0xD8),
    "Vivid Cyan":        Color(0x13, 0xE9, 0xD8),
    "Light Red":         Color(0xF8, 0x7C, 0x6D),
    "Fuchsia":           Color(0xFF, 0x00, 0xFF),
    "Purple":            Color(0x95, 0x30, 0x80),
    "Majora Purple":     Color(0x40, 0x00, 0x40),
    "Twitch Purple":     Color(0x64, 0x41, 0xA5),
    "Purple Heart":      Color(0x8A, 0x2B, 0xE2),
    "Persian Rose":      Color(0xFF, 0x14, 0x93),
    "Dirty Yellow":      Color(0xE0, 0xD8, 0x60),
    "Blush Pink":        Color(0xF8, 0x6C, 0xF8),
    "Hot Pink":          Color(0xFF, 0x69, 0xB4),
    "Rose Pink":         Color(0xFF, 0x90, 0xB3),
    "Orange":            Color(0xE0, 0x79, 0x40),
    "Gray":              Color(0xA0, 0xA0, 0xB0),
    "Gold":              Color(0xD8, 0xB0, 0x60),
    "Silver":            Color(0xD0, 0xF0, 0xFF),
    "Beige":             Color(0xC0, 0xA0, 0xA0),
    "Teal":              Color(0x30, 0xD0, 0xB0),
    "Blood Red":         Color(0x83, 0x03, 0x03),
    "Blood Orange":      Color(0xFE, 0x4B, 0x03),
    "Royal Blue":        Color(0x40, 0x00, 0x90),
    "Sonic Blue":        Color(0x50, 0x90, 0xE0),
    "NES Green":         Color(0x00, 0xD0, 0x00),
    "Dark Green":        Color(0x00, 0x25, 0x18),
    "Lumen":             Color(0x50, 0x8C, 0xF0),
}

NaviColors = {          # Inner Core Color         Outer Glow Color
    "Rainbow":           (Color(0x00, 0x00, 0x00), Color(0x00, 0x00, 0x00)),
    "Gold":              (Color(0xFE, 0xCC, 0x3C), Color(0xFE, 0xC0, 0x07)),
    "White":             (Color(0xFF, 0xFF, 0xFF), Color(0x00, 0x00, 0xFF)),
    "Green":             (Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00)),
    "Light Blue":        (Color(0x96, 0x96, 0xFF), Color(0x96, 0x96, 0xFF)),
    "Yellow":            (Color(0xFF, 0xFF, 0x00), Color(0xC8, 0x9B, 0x00)),
    "Red":               (Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00)),
    "Magenta":           (Color(0xFF, 0x00, 0xFF), Color(0xC8, 0x00, 0x9B)),
    "Black":             (Color(0x00, 0x00, 0x00), Color(0x00, 0x00, 0x00)),
    "Tatl":              (Color(0xFF, 0xFF, 0xFF), Color(0xC8, 0x98, 0x00)),
    "Tael":              (Color(0x49, 0x14, 0x6C), Color(0xFF, 0x00, 0x00)),
    "Fi":                (Color(0x2C, 0x9E, 0xC4), Color(0x2C, 0x19, 0x83)),
    "Ciela":             (Color(0xE6, 0xDE, 0x83), Color(0xC6, 0xBE, 0x5B)),
    "Epona":             (Color(0xD1, 0x49, 0x02), Color(0x55, 0x1F, 0x08)),
    "Ezlo":              (Color(0x62, 0x9C, 0x5F), Color(0x3F, 0x5D, 0x37)),
    "King of Red Lions": (Color(0xA8, 0x33, 0x17), Color(0xDE, 0xD7, 0xC5)),
    "Linebeck":          (Color(0x03, 0x26, 0x60), Color(0xEF, 0xFF, 0xFF)),
    "Loftwing":          (Color(0xD6, 0x2E, 0x31), Color(0xFD, 0xE6, 0xCC)),
    "Midna":             (Color(0x19, 0x24, 0x26), Color(0xD2, 0x83, 0x30)),
    "Phantom Zelda":     (Color(0x97, 0x7A, 0x6C), Color(0x6F, 0x46, 0x67)),
}

sword_trail_colors = {
    "Rainbow":           Color(0x00, 0x00, 0x00),
    "White":             Color(0xFF, 0xFF, 0xFF),
    "Red":               Color(0xFF, 0x00, 0x00),
    "Green":             Color(0x00, 0xFF, 0x00),
    "Blue":              Color(0x00, 0x00, 0xFF),
    "Cyan":              Color(0x00, 0xFF, 0xFF),
    "Magenta":           Color(0xFF, 0x00, 0xFF),
    "Orange":            Color(0xFF, 0xA5, 0x00),
    "Gold":              Color(0xFF, 0xD7, 0x00),
    "Purple":            Color(0x80, 0x00, 0x80),
    "Pink":              Color(0xFF, 0x69, 0xB4),
}

bombchu_trail_colors = {
    "Rainbow":           Color(0x00, 0x00, 0x00),
    "Red":               Color(0xFA, 0x00, 0x00),
    "Green":             Color(0x00, 0xFF, 0x00),
    "Blue":              Color(0x00, 0x00, 0xFF),
    "Cyan":              Color(0x00, 0xFF, 0xFF),
    "Magenta":           Color(0xFF, 0x00, 0xFF),
    "Orange":            Color(0xFF, 0xA5, 0x00),
    "Gold":              Color(0xFF, 0xD7, 0x00),
    "Purple":            Color(0x80, 0x00, 0x80),
    "Pink":              Color(0xFF, 0x69, 0xB4),
}

boomerang_trail_colors = {
    "Rainbow":           Color(0x00, 0x00, 0x00),
    "Yellow":            Color(0xFF, 0xFF, 0x64),
    "Red":               Color(0xFF, 0x00, 0x00),
    "Green":             Color(0x00, 0xFF, 0x00),
    "Blue":              Color(0x00, 0x00, 0xFF),
    "Cyan":              Color(0x00, 0xFF, 0xFF),
    "Magenta":           Color(0xFF, 0x00, 0xFF),
    "Orange":            Color(0xFF, 0xA5, 0x00),
    "Gold":              Color(0xFF, 0xD7, 0x00),
    "Purple":            Color(0x80, 0x00, 0x80),
    "Pink":              Color(0xFF, 0x69, 0xB4),
}

gauntlet_colors = {
    "Silver":            Color(0xFF, 0xFF, 0xFF),
    "Gold":              Color(0xFE, 0xCF, 0x0F),
    "Black":             Color(0x00, 0x00, 0x06),
    "Green":             Color(0x02, 0x59, 0x18),
    "Blue":              Color(0x06, 0x02, 0x5A),
    "Bronze":            Color(0x60, 0x06, 0x02),
    "Red":               Color(0xFF, 0x00, 0x00),
    "Sky Blue":          Color(0x02, 0x5D, 0xB0),
    "Pink":              Color(0xFA, 0x6A, 0x90),
    "Magenta":           Color(0xFF, 0x00, 0xFF),
    "Orange":            Color(0xDA, 0x38, 0x00),
    "Lime":              Color(0x5B, 0xA8, 0x06),
    "Purple":            Color(0x80, 0x00, 0x80),
}

shield_frame_colors = {
    "Red":               Color(0xD7, 0x00, 0x00),
    "Green":             Color(0x00, 0xFF, 0x00),
    "Blue":              Color(0x00, 0x40, 0xD8),
    "Yellow":            Color(0xFF, 0xFF, 0x64),
    "Cyan":              Color(0x00, 0xFF, 0xFF),
    "Magenta":           Color(0xFF, 0x00, 0xFF),
    "Orange":            Color(0xFF, 0xA5, 0x00),
    "Gold":              Color(0xFF, 0xD7, 0x00),
    "Purple":            Color(0x80, 0x00, 0x80),
    "Pink":              Color(0xFF, 0x69, 0xB4),
}

heart_colors = {
    "Red":          Color(0xFF, 0x46, 0x32),
    "Green":        Color(0x46, 0xC8, 0x32),
    "Blue":         Color(0x32, 0x46, 0xFF),
    "Yellow":       Color(0xFF, 0xE0, 0x00),
}

magic_colors = {
    "Green":             Color(0x00, 0xC8, 0x00),
    "Red":               Color(0xC8, 0x00, 0x00),
    "Blue":              Color(0x00, 0x30, 0xFF),
    "Purple":            Color(0xB0, 0x00, 0xFF),
    "Pink":              Color(0xFF, 0x00, 0xC8),
    "Yellow":            Color(0xFF, 0xFF, 0x00),
    "White":             Color(0xFF, 0xFF, 0xFF),
}

#                        A Button                 Text Cursor              Shop Cursor              Save/Death Cursor
#                        Pause Menu A Cursor      Pause Menu A Icon        A Note
a_button_colors = {
    "N64 Blue":         (Color(0x5A, 0x5A, 0xFF), Color(0x00, 0x50, 0xC8), Color(0x00, 0x50, 0xFF), Color(0x64, 0x64, 0xFF),
                         Color(0x00, 0x32, 0xFF), Color(0x00, 0x64, 0xFF), Color(0x50, 0x96, 0xFF)),
    "N64 Green":        (Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00), Color(0x64, 0x96, 0x64),
                         Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00)),
    "N64 Red":          (Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00), Color(0xC8, 0x64, 0x64),
                         Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00)),
    "GameCube Green":   (Color(0x00, 0xC8, 0x32), Color(0x00, 0xC8, 0x50), Color(0x00, 0xFF, 0x50), Color(0x64, 0xFF, 0x64),
                         Color(0x00, 0xFF, 0x32), Color(0x00, 0xFF, 0x64), Color(0x50, 0xFF, 0x96)),
    "GameCube Red":     (Color(0xFF, 0x1E, 0x1E), Color(0xC8, 0x00, 0x00), Color(0xFF, 0x00, 0x50), Color(0xFF, 0x64, 0x64),
                         Color(0xFF, 0x1E, 0x1E), Color(0xFF, 0x1E, 0x1E), Color(0xFF, 0x1E, 0x1E)),
    "GameCube Grey":    (Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78),
                         Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78)),
    "Yellow":           (Color(0xFF, 0xA0, 0x00), Color(0xFF, 0xA0, 0x00), Color(0xFF, 0xA0, 0x00), Color(0xFF, 0xA0, 0x00),
                         Color(0xFF, 0xFF, 0x00), Color(0xFF, 0x96, 0x00), Color(0xFF, 0xFF, 0x32)),
    "Black":            (Color(0x10, 0x10, 0x10), Color(0x00, 0x00, 0x00), Color(0x00, 0x00, 0x00), Color(0x10, 0x10, 0x10),
                         Color(0x00, 0x00, 0x00), Color(0x18, 0x18, 0x18), Color(0x18, 0x18, 0x18)),
    "White":            (Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF),
                         Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF)),
    "Magenta":          (Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF),
                         Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF)),
    "Ruby":             (Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00),
                         Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00)),
    "Sapphire":         (Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF),
                         Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF)),
    "Lime":             (Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00),
                         Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00)),
    "Cyan":             (Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF),
                         Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF)),
    "Purple":           (Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80),
                         Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80)),
    "Orange":           (Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00),
                         Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00)),
}

#                       B Button
b_button_colors = {
    "N64 Blue":         Color(0x5A, 0x5A, 0xFF),
    "N64 Green":        Color(0x00, 0x96, 0x00),
    "N64 Red":          Color(0xC8, 0x00, 0x00),
    "GameCube Green":   Color(0x00, 0xC8, 0x32),
    "GameCube Red":     Color(0xFF, 0x1E, 0x1E),
    "GameCube Grey":    Color(0x78, 0x78, 0x78),
    "Yellow":           Color(0xFF, 0xA0, 0x00),
    "Black":            Color(0x10, 0x10, 0x10),
    "White":            Color(0xFF, 0xFF, 0xFF),
    "Magenta":          Color(0xFF, 0x00, 0xFF),
    "Ruby":             Color(0xFF, 0x00, 0x00),
    "Sapphire":         Color(0x00, 0x00, 0xFF),
    "Lime":             Color(0x00, 0xFF, 0x00),
    "Cyan":             Color(0x00, 0xFF, 0xFF),
    "Purple":           Color(0x80, 0x00, 0x80),
    "Orange":           Color(0xFF, 0x80, 0x00),
}

#                        C Button                 Pause Menu C Cursor      Pause Menu C Icon        C Note
c_button_colors = {
    "N64 Blue":         (Color(0x5A, 0x5A, 0xFF), Color(0x00, 0x32, 0xFF), Color(0x00, 0x64, 0xFF), Color(0x50, 0x96, 0xFF)),
    "N64 Green":        (Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00), Color(0x00, 0x96, 0x00)),
    "N64 Red":          (Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00), Color(0xC8, 0x00, 0x00)),
    "GameCube Green":   (Color(0x00, 0xC8, 0x32), Color(0x00, 0xFF, 0x32), Color(0x00, 0xFF, 0x64), Color(0x50, 0xFF, 0x96)),
    "GameCube Red":     (Color(0xFF, 0x1E, 0x1E), Color(0xFF, 0x1E, 0x1E), Color(0xFF, 0x1E, 0x1E), Color(0xFF, 0x1E, 0x1E)),
    "GameCube Grey":    (Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78), Color(0x78, 0x78, 0x78)),
    "Yellow":           (Color(0xFF, 0xA0, 0x00), Color(0xFF, 0xFF, 0x00), Color(0xFF, 0x96, 0x00), Color(0xFF, 0xFF, 0x32)),
    "Black":            (Color(0x10, 0x10, 0x10), Color(0x00, 0x00, 0x00), Color(0x18, 0x18, 0x18), Color(0x18, 0x18, 0x18)),
    "White":            (Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF), Color(0xFF, 0xFF, 0xFF)),
    "Magenta":          (Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF), Color(0xFF, 0x00, 0xFF)),
    "Ruby":             (Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00), Color(0xFF, 0x00, 0x00)),
    "Sapphire":         (Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF), Color(0x00, 0x00, 0xFF)),
    "Lime":             (Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00), Color(0x00, 0xFF, 0x00)),
    "Cyan":             (Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF), Color(0x00, 0xFF, 0xFF)),
    "Purple":           (Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80), Color(0x80, 0x00, 0x80)),
    "Orange":           (Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00), Color(0xFF, 0x80, 0x00)),
}

#                       Start Button
start_button_colors = {
    "N64 Blue":         Color(0x5A, 0x5A, 0xFF),
    "N64 Green":        Color(0x00, 0x96, 0x00),
    "N64 Red":          Color(0xC8, 0x00, 0x00),
    "GameCube Green":   Color(0x00, 0xC8, 0x32),
    "GameCube Red":     Color(0xFF, 0x1E, 0x1E),
    "GameCube Grey":    Color(0x78, 0x78, 0x78),
    "Yellow":           Color(0xFF, 0xA0, 0x00),
    "Black":            Color(0x10, 0x10, 0x10),
    "White":            Color(0xFF, 0xFF, 0xFF),
    "Magenta":          Color(0xFF, 0x00, 0xFF),
    "Ruby":             Color(0xFF, 0x00, 0x00),
    "Sapphire":         Color(0x00, 0x00, 0xFF),
    "Lime":             Color(0x00, 0xFF, 0x00),
    "Cyan":             Color(0x00, 0xFF, 0xFF),
    "Purple":           Color(0x80, 0x00, 0x80),
    "Orange":           Color(0xFF, 0x80, 0x00),
}

meta_color_choices = ["Random Choice", "Completely Random", "Custom Color"]


def get_tunic_colors():
    return list(tunic_colors.keys())


def get_tunic_color_options():
    return meta_color_choices + ["Rainbow"] + get_tunic_colors()


def get_navi_colors():
    return list(NaviColors.keys())


def get_navi_color_options(outer=False):
    if outer:
        return ["[Same as Inner]"] + meta_color_choices + get_navi_colors()
    else:
        return meta_color_choices + get_navi_colors()


def get_sword_trail_colors():
    return list(sword_trail_colors.keys())


def get_sword_trail_color_options(outer=False):
    if outer:
        return ["[Same as Inner]"] + meta_color_choices + get_sword_trail_colors()
    else:
        return meta_color_choices + get_sword_trail_colors()


def get_bombchu_trail_colors():
    return list(bombchu_trail_colors.keys())


def get_bombchu_trail_color_options(outer=False):
    if outer:
        return ["[Same as Inner]"] + meta_color_choices + get_bombchu_trail_colors()
    else:
        return meta_color_choices + get_bombchu_trail_colors()


def get_boomerang_trail_colors():
    return list(boomerang_trail_colors.keys())


def get_boomerang_trail_color_options(outer=False):
    if outer:
        return ["[Same as Inner]"] + meta_color_choices + get_boomerang_trail_colors()
    else:
        return meta_color_choices + get_boomerang_trail_colors()


def get_gauntlet_colors():
    return list(gauntlet_colors.keys())


def get_gauntlet_color_options():
    return meta_color_choices + get_gauntlet_colors()


def get_shield_frame_colors():
    return list(shield_frame_colors.keys())


def get_shield_frame_color_options():
    return meta_color_choices + get_shield_frame_colors()


def get_heart_colors():
    return list(heart_colors.keys())


def get_heart_color_options():
    return meta_color_choices + get_heart_colors()


def get_magic_colors():
    return list(magic_colors.keys())


def get_magic_color_options():
    return meta_color_choices + get_magic_colors()


def get_a_button_colors():
    return list(a_button_colors.keys())


def get_a_button_color_options():
    return meta_color_choices + get_a_button_colors()


def get_b_button_colors():
    return list(b_button_colors.keys())


def get_b_button_color_options():
    return meta_color_choices + get_b_button_colors()


def get_c_button_colors():
    return list(c_button_colors.keys())


def get_c_button_color_options():
    return meta_color_choices + get_c_button_colors()


def get_start_button_colors():
    return list(start_button_colors.keys())


def get_start_button_color_options():
    return meta_color_choices + get_start_button_colors()


def contrast_ratio(color1, color2):
    # Based on accessibility standards (WCAG 2.0)
    lum1 = relative_luminance(color1)
    lum2 = relative_luminance(color2)
    return (max(lum1, lum2) + 0.05) / (min(lum1, lum2) + 0.05)


def relative_luminance(color):
    color_ratios = list(map(lum_color_ratio, color))
    return color_ratios[0] * 0.299 + color_ratios[1] * 0.587 + color_ratios[2] * 0.114


def lum_color_ratio(val):
    val /= 255
    if val <= 0.03928:
        return val / 12.92
    else:
        return pow((val + 0.055) / 1.055, 2.4)


def generate_random_color():
    return [random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)]


def hex_to_color(option):
    # build color from hex code
    option = option[1:] if option[0] == "#" else option
    if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', option):
        raise Exception(f"Invalid color value provided: {option}")
    if len(option) > 3:
        return list(int(option[i:i + 2], 16) for i in (0, 2, 4))
    else:
        return list(int(f'{option[i]}{option[i]}', 16) for i in (0, 1, 2))


def color_to_hex(color):
    return '#' + ''.join(['{:02X}'.format(c) for c in color])
