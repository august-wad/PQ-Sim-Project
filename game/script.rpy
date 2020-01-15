# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Stephen")
define r = Character("Ramzina")
image ramzina neutral = im.Scale("ramzina neutral.png", 443, 1000)
image august neutral = im.Scale("august neutral.png", 352, 870)
image tonya neutral = im.Scale("tonya_neutral.png", 310, 800)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ramzina neutral at left
    show august neutral at right
    show tonya neutral

    # These display lines of dialogue.

    r "filler text"

    r "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
