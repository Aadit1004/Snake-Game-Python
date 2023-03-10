# Snake-Game-Python
First python project on the Snake game using Pygame 

First project with python. Learning how to use the language but also how to create the classic snake game using Pygame.


TODO:
- ~~Create display screen~~
- ~~Create Snake head~~
- ~~Create Snake movement~~
- ~~Create boundaries for snake~~
- Create collectibles placed randomly on screen
- Create addition to length on Snake when collecting the collectibles 
- ~~Create Score on display and keep track~~
- ~~Create losing and winning screen/text~~
- Create losing game when snake overlaps and/or exits boundary


Known bugs:
1.  ~~Snake has ghost trail when moving around screen~~ 
* Fixed by updating location of when screen is filled to right before drawing the snake head
2. Food location doesn't get updated when snake is over it
3. Snake length doesn't get updated after consuming food