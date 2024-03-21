>> testing minigame

/* 20g = gamescene 1c = player bottom, 2c = player left, 3c = player right, 4c = player top, 5c = gamecollision, 6c = spike collision, 7c = playerglobal

>> imports
#include readme.rst

>> data
#define gamescene: group = 1
#define gamecollision: collision = 5
#define spikecollision: collision = 6
#define player: group = 21

#define health: int = 3

@class movement {
    #function move_left() {
        triggers.move(gamescene, -1, 0, 1, nulltype)
    }
    #function move_right() {
        triggers.move(gamescene, 1, 0, 1, nulltype)
    }

    #function gravity() {
        while (true) {
            if (1c.collide(gamecollision)) {
                >> break
            }
            triggers.move(player, 0, 30, 1, nulltype)
        }
    }

    #function jump() {
        if (1c.collide(gamecollision) == true) {
            triggers.move(player, 0, 30, 1, ease-in-out)
            movement.gravity()
        }
    }
}

>> touch
touch.on_hold(false, movement.move_left)
touch.on_reliese(false, triggers.stop, movement.move_left)
touch.on_hold(true, movement.move_right)
touch.on_reliese(true, triggers.stop, movement.move_right)

touch.on_double_touch(movement.jump)

>> collision
while (true) {
    if (2c.collide(gamecollision) == true) {
        triggers.stop(movement.move_left)
    }

    if (3c.collide(gamecollision) == true) {
        triggers.stop(movement.move_right)
    }

    if (4c.collide(gamecollision) == true) {
        triggers.stop(movement.jump)
        movement.gravity()
    }

    if (7c.collide(6c) == true) {
        >> player =- 1
    }

    if (health == 0) {
        triggers.move(30, 0, -10, 1, bounce-out)
    }
}