# Roadmap
- Anadir torpedos en bullet
- Anadir somido r2d2
- Crear escena inicio, batalla y fin
- Anadir health / vidas / score (https://kidscancode.org/blog/tags/pygame/)
- Anadir explosiones
- Anadir power ups / health / topedos


# Frameworks
- Arcade
  - https://realpython.com/arcade-python-game-framework/
  - https://api.arcade.academy/en/latest/index.html

# Tutoriales usados
## Advanced tutorial with folder structure and ship acceleration
- https://realpython.com/asteroids-game-python/
- 
## Assets and original game
 https://github.com/attreyabhatt/Space-Invaders-Pygame

## Tutorial Mundo Python
https://www.youtube.com/watch?v=MY9Jbri3wnE
- https://github.com/mundo-python/pygame-Scripts/blob/master/17_game_over.py

## Project structure
- https://github.com/ehmatthes/pcc_2e/tree/master/chapter_13/creating_first_alien

- https://ncase.me/sight-and-light/ 
- https://opensource.com/article/20/9/add-sound-python-game

# Recursos
## Iconos
- https://www.flaticon.com/
- https://thenounproject.com/icon/tie-fighter-42403/
- https://opengameart.org/

## Editor imagenes
- https://www.photopea.com/

## Sonidos
- Star Wars :
  - https://starchives.tripod.com/swwav.html
  - https://www.thesoundarchive.com/star-wars.asp
  - http://www.moviewavs.com/Movies/Star_Wars.html
- https://freesound.org/ 
- http://www.sa-matra.net/sounds/starwars/

## Musica
- https://filmmusic.io/artists/kevin-macleod

## Assets meteoros torpedos etc..
Shooter Game tutorial con buenos assets
- https://www.youtube.com/watch?v=pyiMf6Vr94Y
- https://github.com/mundo-python/shooter-pygame

## TODO Tank battle tutorial with AI
- https://kidscancode.org/blog/2018/04/godot3_tanks_part1/


# Game Scenes
- https://stackoverflow.com/questions/11105836/multiple-displays-in-pygame
- Sample Games with scenes
  - https://github.com/MyreMylar/christmas_adventure
  - https://github.com/MyreMylar/tower_defence

The better solution is probably to divide your game into scenes. Create multiple scenes so that each one represent one stage of the game, something like MenuScene, MainScene, BattleScene, GameOverScene, OptionScene etc.

Then let each of those scenes handle input/drawing of that very part of the game.

MenuScene handles drawing and input etc. of the game's menu
MainScene handles drawing and input etc. of the running game
BattleScene handles drawing and input etc. of whatever you do in run_ani
In your mainloop, just pass control over to the current scene by implementing the methods draw(), handle_event(), and update().

Some example code to get the idea:

```python
scenes = {'Main': MainScene(),
          'Battle': BattleScene()} #etc

scene = scenes['Main']

class MainScene():
  ...
  def handle_event(self, event):
    if event.type == KEYUP:
      if event.key == K_a:
        scene = scenes['Battle']
  ...

class BattleScene():
  ...
  def draw(self):
    # draw your animation

  def update(self):
    # if animation is over:
    scene = scenes['Main']

...

def main_game():
  ending=False
  While Not ending:
      clock.tick(30)
      for event in pygame.event.get():
        scene.handle_event(event)
        scene.update()
        scene.draw()
```        
This is an easy way to cleanly seperate the game logic and allow context switching.