from os import name
from dearpygui.core import *
from dearpygui.simple import *
from functions import Encrypt

# functions


def start(sender, data):
    print("Started")
    key = get_value(name="key")
    filename = get_value(name="file")

    Encrypt(filename, key)


# window object settings
set_main_window_size(1010, 890)
set_global_font_scale(1.35)
set_theme("Dark Grey")
set_style_window_padding(50, 50)

with window("Encrypter", width=1000, height=860):
    # top text & logo
    print("GUI is running.")
    set_window_pos("Encrypter", 0, 0)
    add_image(name="logo", value="logo.png", width=206, height=206)
    add_spacing(count=12)
    add_text("This is a file encoder and decoder! \n\nSimply choose to encode or decode \nand then the file to do it on. \nMake sure the file is in the same folder as me.")
    add_spacing(count=12)
    add_separator()
    # options
    add_spacing(count=12)
    add_radio_button(name="encode_decode", items=[
                     "Encode", "Decode"], default_value=0, horizontal=True)
    add_spacing(count=12)
    add_text("Add a key inbetween 1 & 255")
    add_input_int(name="key", min_value=1, max_value=255)
    add_spacing(count=12)
    add_input_text(
        name="file", default_value="Make sure you include the extention of the file at the end.")
    add_spacing(count=12)
    add_separator()
    # start encrypting/decrypting
    add_spacing(count=6)
    add_button(name="Start", callback=start)


start_dearpygui()
