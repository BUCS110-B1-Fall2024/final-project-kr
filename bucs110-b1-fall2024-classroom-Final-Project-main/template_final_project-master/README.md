
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Bird hunter game
## CS110 B1 Final Project  Fall, 2024

## Team Members

Kaleia Robinson

***

## Project Description

A simple game wherein the user uses a gun to shoot at birds and increase their score. The game gets harder as the user's score hits specific milestones. Birds escaping lowers the user's health, leading to a game over if the health reaches 0.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Gun which rotates and shoots bullets
2. Varitey of birds with different stats that can be shot
3. Scoreboard that keeps track of birds shot and the player's health
4. Increasing difficulty (more birds spawn, faster birds) tied to score milestones
5. Game over screen when player's health hits zero, providing player's score

### Classes

- background: background object with an image for the screen
- glock: player's glock object, which they can move and use to shoot the birds
- bullet: bullets which are shot from the gun when the player presses space, which kill the birds when they collide with them
- bird: bird objects that fall from the sky and can be shot by the player. if they escape by going off-screen, the player loses health. they have randombly chosen image and speed.
- scoreboard: object that displays the player's score and health onscreen
- controller: main gameplay loop

## ATP

| Step                 |Procedure                                                                           |Expected Results                   |
|----------------------|:--------------------:                                                              |----------------------------------:|
|  1                   | Start program, press and hold left arrow key, then press and hold right arrow key  | Glock object rotates in place direction of arrowkey pressed
|  2                   | Press space                                                                        | Bullet object shoots of out of glock
|  3                   | Point glock object at bird using arrowkeys, press space to shoot the bird          | Bird and bullet objects both disappear, score increases by 1
|  4                   | Wait for a bird object to descend off-screen                                       | Health decreases by 1
|  5                   | Repeat step 4 until health equals 0                                                | Game over screen appears, listing player's score
