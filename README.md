# set-variants

This repo has code to generate cards for several variants of the card game [SET](https://www.setgame.com/). The images generated are designed to be printed by [The Game Crafter](https://www.thegamecrafter.com/) as a Poker Deck.

There is also an [online implementation](https://tsetse.tck.mn/) of many of the same games made by Andy Tockman ([source code](https://github.com/tckmn/tsetse)), which also has [explanations and credits](https://tsetse.tck.mn/help.html).

# usage

Requires Python and [Pillow](https://python-pillow.org/). Run `make` to build all set games, or `make one=<name>` to build a specific one. (Once the directories are created, you can just run one of the files with Python.)
