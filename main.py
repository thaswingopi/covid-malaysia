"""

Coded by Mazareef ProjectMika for MS Drive Thru

"""

def on_a_pressed():
    global Fire
    Fire = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . 2 2 2 . . . . . . . . . . 
                    . . . . 2 2 6 6 6 6 . . 2 . . . 
                    . . 2 4 6 6 6 6 6 6 6 2 2 2 . . 
                    . 2 4 . . 2 2 2 6 6 6 2 2 2 2 . 
                    . . 2 4 6 6 6 6 6 6 6 2 2 2 . . 
                    . . . . 2 2 6 6 6 6 . . 2 . . . 
                    . . . 2 2 2 . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        DigitalHeroes,
        200,
        0)
    # Avoid to many Projectiles
    pause(300)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.warm_radial, 100)
    sprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Covid19: Sprite = None
Stars: Sprite = None
Fire: Sprite = None
DigitalHeroes: Sprite = None
# Additional MDM2020 Splash Screen
Splash = sprites.create(img("""
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bcd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111dddddddddddddddddddddddddd11dddddddddddddddddddddddddd111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114443dddd11111111111111111111111111111111111111111111dddd5511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd11111111111144444444444443dddd1111111111111d1111111111dddd55555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd111111111111444444444444444444d111111969111bb111111d55555555555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd11111111111144444444444444444d1111119669111aaad111111d555555555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd111111111111444444444444444d111111966669111aaaab111111d55555555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444444444444411111119666669111aaaaaad111111d555555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd111111111111444444444444d111111966666669111aaaaaaab111111155555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444444444d11111119666666669111aaaaaaaaad111111d555555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd111111111111444444444d111111d66666666669111aaaaaaaaaab1111111d5555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444444d11111119666666666669111aaaaaaaaaaaad111111d555555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444441111111166666666666669111aaaaaaaaaaaaa31111111d5555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444d11111119666666666669669111aaab3aaaaaaaaabd1111111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111111166666666666911669111aaab1daaaaaaaaaa3111111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111119666666666666911669111aaab111baaaaaaaaabd1111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd11111111111144441111966666666669669d6669111aaab11154aaaaaaaaaad111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111166666666669166666661111aaab111555baaaaaaaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111166666666691166666911111aaab11155554aaaaaaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111166666666691966666111111aaab111555555baaaaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111166666916666666666111111aaab11155555554aaaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111166666116666669966969111aaab11155555555baaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111166666116666611966669111aaab11155555555baaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111169966966666611966669111aaab11155555555baaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111111966666996699666669111aaab11155555555baaab111555511111111111
            111111111d222222222222222222222222231d7777777777777777777777777d111111111111bfd1111111111114444111111966669196666669669111aaab11155555555baaab111555511111111111
            1111111111ddddddddddddddddddddddddd111dddddddddddddddddddddddddd111111111111bfd1111111111114444111119666661196666611669111aaab11155555555baaab111555511111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd1111111111114444111166669661966666911669111aaab11155555555baaab111555511111111111
            11111111119999999999999999999999999111ddddddddddddddddddddddddd1111111111111bfd1111111111114444111166619666666666919669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166919666669166666661111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166919666691166666611111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166966666691966666111111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166666616699666666111111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166666116666669966969111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166666116666691966669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111169666d66666611966669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111191966666696619666669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111111966669196666669669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111119666661196666691669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111196666661166666911669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166699669666666919669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166919666669166966669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166919666691166666669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166996666691166666669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166666696699666666669111aaab11155555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166666116666666666661111baab111d5555555baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd11111111111144441111666661166666666666111111dab1111111ddd5baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111114444111166666196666666669111111111d11111111111baaab111555511111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111113ddd111191966666666666911111111111111111111111baaab1111ddd11111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111111111111111966666666669111111111111111111111111baaab111111111111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111111111111119666666666911111111111111111111111111baaab111111111111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111111111111196666666691111111111111111111111111111baaab111111111111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111111111111166666666911111111111111111111111111111baaab111111111111111111
            1111111119666666666666666666666666691d5555555555555555555555555d111111111111bfd1111111111111111111166666691111111111111111111111111111111baaab111111111111111111
            11111111119999999999999999999999999111ddddddddddddddddddddddddd1111111111111bfd1111111111111111111166666d11111111111111111111111111111111baaab111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd1111111111111111111166691111111111111111111111111111111111dbaab111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111116911111111111111111111111111111111111111dab111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd11111111111111111111911111111111111111111111111111111111111111d111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111bfd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111dbd111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    """),
    SpriteKind.player)
Splash.set_flag(SpriteFlag.GHOST, True)
pause(1000)
Splash.destroy()
pause(200)
game.splash("Help Us, Defend Malaysia", "Against COVID19 Virus")
DigitalHeroes = sprites.create(img("""
        ..............fffcc.................
            ..............fbbddc................
            ...............fbbddc...............
            ccc............fcbbccf..............
            cbbcc.........ffccccccffffff........
            .cbbdc.....fffcbbbbbbbbbbbbbff......
            .fbbddc..ffcccbbbbcbcbbbbbbbbbff....
            ..fbbdfffcccccbbbcbcbbffbbbbbcbf....
            ..fcbbbcccccccbbbcbcb1ff1111bbbf....
            ..fccbcccccccccbbbbbb11111111bf.....
            .fcbbfffccccccccbbbb11cc33cccf......
            .fbbf...cbdbcccccbbb111c131cf.......
            fbbf.....ccdddddfbbbc111c33f........
            fff........ccddfbbdbf1111ff.........
            .............cfbbdbfccccc...........
            ..............fffff.................
    """),
    SpriteKind.player)
controller.move_sprite(DigitalHeroes, 200, 200)
DigitalHeroes.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)

def on_forever():
    global Stars
    if Math.percent_chance(5):
        # Let's Add some Stars to show effects of space traveling
        Stars = sprites.create_projectile_from_side(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 6 . 6 . . . . . . . 
                            . . . . . . . 6 . . . . . . . . 
                            . . . . . . 6 . 6 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            -50,
            0)
        Stars.set_flag(SpriteFlag.GHOST, True)
        Stars.set_position(scene.screen_width(), randint(0, scene.screen_height()))
        Stars.ax = -20
forever(on_forever)

def on_update_interval():
    global Covid19
    Covid19 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . 2 . 8 6 8 . 2 . . . . . 
                    . . . . . 6 8 8 8 6 . . . . . . 
                    . . . . 8 8 2 8 2 8 8 . . . . . 
                    . . . 2 6 8 8 8 8 8 6 2 . . . . 
                    . . . . 8 8 2 8 2 8 8 . . . . . 
                    . . . . . 6 8 8 8 6 . . . . . . 
                    . . . . 2 . 8 6 8 . 2 . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Covid19.set_position(160, randint(0, 120))
    Covid19.set_velocity(-50, 0)
game.on_update_interval(500, on_update_interval)
