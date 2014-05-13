How the engine works:

You can use F1 to get screenshots.
In Pic.PSD there are labels for many (but not even close to all) of the game v variables.

Your character first of all has an x and y coordinate.  This is the coordinate of the center of the top of the character.  
Dx and dy are the characters change in x and y each frame, in other words their speed.

The state of the character is used by if statements to know when a character has certain properties or can do certain things.

The movet variable is used to record in frames when the character changes their state, it is also used to calculate the drawstate().

Drawstate is based on the state of the character and is the actual picture file used when the character is in that state.  The collisions are taken from the draw state.

When you press for an attack while in another attack nextattack gets filled in, and that attack will immediately be done when movet is 0.

Chargeback and down are the number of frames you hold back and down continously.  The chargetimer is how much time you have after releasing back or down and pressing forw/up + the button to do the attack.

Facing is 1 when your facing right, and -1 when your facing left.  Hence p.x + p.w2()*p.facing is always the coordinate of the fornt of your character.