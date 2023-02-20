# Mars

Mars is a multiplayer game where you control a single rover, explore and interact with the planet. Since this is
a beta version of the game, the game focuses on an exploration component.

The planet is defined as a two-dimensional grid of tiles. All tiles are square-shaped and of unit length. Each tile
will hold information related to its current coordinates. Planets are spherical and not flat. This means the left-most column of the grid should "meet up" with the right-most column. Similarly, the top-most row should
meet up with the bottom-most.

# Commands

## Connect

This is the first command that the user will need to input.

- connect (hostname/ip) (port)

If the connection succeeds, the user should receive 'Connected, please log in' from the server. Otherwise, the user will receive 'Unable to connect to the server, check command arguments'.

## Login

This should be the first command user after establishing a connection to the server.

 - login (ident) (password)
 
 If either ident or password are left out, the user will receive 'Incomplete login criteria'. If the login fails, the user will receive 'Invalid login details', otherwise, if successful, the user will receive 'Logged In!'.

## Observe

This will allow the user to get a simple look at the area around the rover. The server will provide a of 7x5 grid
of the user’s location with the rover at the centre.

- observe

Afterwards, the program will display a representation of the grid to the user where each tile is represented
by two characters and separated by | symbols.

Elevation will appear on the grid as a number on the right column of the cell. The displayed elevation of each
tile is relative to the current elevation of the rover. e.g. if a rover is on a tile of elevation of 1 and a tile
retrieved from an observe command has an elevation of 3, it will appear as an elevation of 2. The server
sends an absolute elevation value for each tile.

Any tile which has a relative elevation of > 9 will only show the maximum elevation (9). Any tile which has a
relative elevation of < 0 will show a ‘-’ symbol on the right column. If the tile’s relative elevation is 0, only a
space will be shown. If the relative elevation is > 0 and <= 9, it will show the elevation in the right column of
the cell.

The left column of the cell will contain a 'R' symbol if there is a rover on that tile, or a 'M' symbol if there is a
message there. If there is both a rover and a message, the 'R' symbol will appear. If there is neither, it will
contain a space.

## Move

This will move the user's rover one space (in north, west, east or south). This can be abbreviated to m
followed by the first character of the direction.

- move (north | west | east | south)

## Stats

Shows the current stats of the player. It will return the current number of tiles that have been explored and the
current position of the rover.

- stats


## Inspect

The inspect command will allow the user to inspect an adjacent tile and gather information from it. This can
reveal messages which have been left on tiles with the note command.

- inspect (north | west | east | south)

If there is a note on the adjacent tile, the message will outputed to the client, otherwise, the client will see 'Nothing interesting was found here'.

## Note

Places a message on the rover's current tile. This allows for simple communication within the game
itself. If a message is placed on a tile which already has a message, the server will overwrite the old message.

- note (message)

## Message

Similar to the note command, this allows the user to send a message directly to another rover.

- message (ident) (message)

## Commit

When the user has finished playing, they can commit their exploration data to the server. The client will need
to maintain all the terrain information which has been retrieved from observe commands.

- commit

## Quit

The quit command will close the session and exit the game. If you have not committed your data to the
server, it will be lost. When the user has issued the quit command, it must wait for an ok from the server
before terminating the connection.

- quit



