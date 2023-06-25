# Battle of the Knights

Created Friday June 23, 2023

### How to play:

Attack deals random damage to opponent. Defend prevents the attack. Rest gains health points.

You may not perform the same action more than twice in a row.

Choose 'a', 'd', or 'r':
* 'a' => ATTACK
* 'd' => DEFEND
* 'r' => REST

Modes:
* One Player = 'one'
* Two Player = 'two'

#### Constraints:
* Game does not allow greater than 100 health points for a player.
* Zero or less health points results in death within the game.

#### Possibilities
* A -> <- A
* D -- -- D
* R +   + R
* A -- -- D
* D -- -- A
* A ->  + R
* R +  <- A
* R +  -- D
* D --  + R

#### LATER IDEAS

* additional choices other than A, D, R
* classes / archetypes for player to choose from?? Class inheritance
* CPU opponent strategies and difficulties...
* fix two player mode to use socket programming or something else so you cannot see the other players input