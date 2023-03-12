# Snake-Game-Python
First python project on the Snake game using Pygame 

First project with python. Learning how to use the language but also how to create the classic snake game using Pygame.

# End-of-Project Reflection
In the end, the project was really fun and not too hard. Using Pygame, it was easy to set up the displays, texts, and the movement of the snake after looking at the documentation. My biggest issues were at the beginning, there was a ghost trail of the snake when I was just simply moving the snake head around. That was fixed by updating the location of when the screen is filled (background) to right before drawing the snake head. And another big issue was that the collision between the snake head and the food wouldn't render and update the score or snake. To debug that, I saw that the condition was too specific for checking if the snake head's position was equal to the food's position so it would rarely update. I had then changed i to just using the distance formula between the snake head and foods' location and checked if distance was <= diameter of snake's circle and it seemed to fix everything.

# TODO:
- ~~Create display screen~~
- ~~Create Snake head~~
- ~~Create Snake movement~~
- ~~Create boundaries for snake~~
- ~~Create collectibles placed randomly on screen~~
- ~~Create addition to length on Snake when collecting the collectibles~~
- ~~Create Score on display and keep track~~
- ~~Create losing screen/text~~
- ~~Create losing game when snake overlaps and/or exits boundary~~