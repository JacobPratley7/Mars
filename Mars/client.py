import socket
import sys

all_tiles = []
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []



#function is provided with a list of strings
#function iterates through this list a converts each string to a new list
#returns a list of generated lists
def generate_tuples(new_list):
    current_tuples = []
    for current_item in new_list:
        current_tuple = []
        new_item = current_item.split(",")
        x_coor = int(new_item[0].lstrip("("))
        y_coor = int(new_item[1])
        elev = int(new_item[2])
        rot = int(new_item[3])
        mot = int(new_item[4].rstrip(")"))
        current_tuple.append(x_coor)
        current_tuple.append(y_coor)
        current_tuple.append(elev)
        current_tuple.append(rot)
        current_tuple.append(mot)
        current_tuples.append(current_tuple)
    return current_tuples

#iterates through the list returned bu the previous function and adds each item to their corresponding row
def generate_rows(current_tiles):
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    i = 0
    while i < 7:
        row1.append(current_tiles[i])
        i+=1

    while i < 14:
        row2.append(current_tiles[i])
        i+=1

    while i < 21:
        row3.append(current_tiles[i])
        i+=1

    while i < 28:
        row4.append(current_tiles[i])
        i+=1

    while i < 35:
        row5.append(current_tiles[i])
        i+=1

    all_rows = [row1, row2, row3, row4, row5]
    return all_rows

#reponsible for drawing the grid after the observe command is called
def draw(all_rows):
    #we know the player's location is the tile at row 3 column 4
    rover_location = all_rows[2][3]
    #we also know the rover's eleveation is the number at index 2
    rover_elevation = rover_location[2]
    first = "|"
    second = "|"
    third = "|"
    fourth = "|"
    fifth = "|"
    blank = "  |"
    for value in all_rows[0]:
        #in the first block of conditionals, we check to see whether there is a rover or message on the particular tile
        #we then add the appropriate character to the ouput string
        line = ""
        if(value[3] == 1):
            first += "R"
        elif(value[4] == 1 and value[3] == 0):
            first += "M"
        else:
            first += " "

        #the eleveation of a tile is relevant to the elevation to the rover
        #hence, we subtract the rover's elevation form the tile's elevation
        elev_value = value[2] - rover_elevation

        #in this next block of conditionals, we check the value of elev_value, and add the appropriate character to the output string
        if elev_value == 0:
            first += " "
        elif elev_value > 0 and elev_value <= 9:
            first += str(elev_value)
        elif elev_value < 0:
            first += "-"
        else:
            first += "9"

        #finally, we add a pipe character to the end of the string
        first += "|"

    #tasks performed here follow the same process as the code block above
    for value in all_rows[1]:
        line = ""
        if(value[3] == 1):
            second += "R"
        elif(value[4] == 1 and value[3] == 0):
            second += "M"
        else:
            second += " "

        elev_value = value[2] - rover_elevation
        if elev_value == 0:
            second += " "
        elif elev_value > 0 and elev_value <= 9:
            second += str(elev_value)
        elif elev_value < 0:
            second += "-"
        else:
            second += "9"

        second += "|"

    #performs the same tasks as previous code blocks
    for value in all_rows[2]:
        line = ""
        #here, we have an extra conditional as, being the middle row, we must check if the current tile is the tile with the player on it
        #if it is, we must add the "RR" characters to the output string
        if(value == all_rows[2][3]):
            third += "RR"
            #player.setX(value.getX())
            #player.setY(value.getY())
        else:
            if(value[3] == 1):
                third += "R"
            elif(value[4] == 1 and value[3] == 0):
                second += "M"
            else:
                third += " "

            elev_value = value[2] - rover_elevation
            if elev_value == 0:
                third += " "
            elif elev_value > 0 and elev_value <= 9:
                third += str(elev_value)
            elif elev_value < 0:
                third += "-"
            else:
                third += "9"

        third += "|"

    #performs the same tasks as previous code blocks
    for value in all_rows[3]:
        line = ""
        if(value[3] == 1):
            fourth += "R"
        elif(value[4] == 1 and value[3] == 0):
            fourth += "M"
        else:
            fourth += " "

        elev_value = value[2] - rover_elevation
        if elev_value == 0:
            fourth += " "
        elif elev_value > 0 and elev_value <= 9:
            fourth += str(elev_value)
        elif elev_value < 0:
            fourth += "-"
        else:
            fourth += "9"

        fourth += "|"

    #performs the same tasks as previous code blocks
    for value in all_rows[4]:
        line = ""
        if(value[3] == 1):
            fifth += "R"
        elif(value[4] == 1 and value[3] == 0):
            fifth += "M"
        else:
            fifth += " "

        elev_value = value[2] - rover_elevation
        if elev_value == 0:
            fifth += " "
        elif elev_value > 0 and elev_value <= 9:
            fifth += str(elev_value)
        elif elev_value < 0:
            fifth += "-"
        else:
            fifth += "9"

        fifth += "|"

    return (first, second, third, fourth, fifth)

#iterates through the list return form the generate_tuples() function
#adds each item to all_tiles so long as it is not already in there
def add_to_all(more_tuples):
    for tup in tuples:
        if tup not in all_tiles:
            all_tiles.append(tup)

    return






def check_event():
    ret_size = s.recv(256).decode("ascii")
    new_size = int(str(ret_size).strip("\x00"))
    msg1 = s.recv(new_size).decode()
    split_msg1 = msg1.split(" ")
    if split_msg1[0] == "error":
        output = "Error:"
        j = 1
        while j < len(split_msg1):
            output += " " + split_msg[j]
            j += 1
        print(output)
        return
    elif split_msg1[0] == "event":
        if split_msg1[1] == "message":
            output = split_msg[2] + ":"
            j = 3
            while j < len(split_msg1):
                output += " " + split_msg1[j]
                j += 1
            print(output)
            return
        elif split_msg1[1] == "notify":
            output = "Server:"
            j = 2
            while j < len(split_msg1):
                output += " " + split_msg1[j]
                j += 1
            print(output)
            return
    else:
        return












s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #new socket object
my_current_tiles = []
my_current_rows = []
formated_vals = []


#main method
if __name__ == "__main__":
    running = True
    stage = 0 #keeps track of which stage of connection the user it currently at
    while(running):
        command = input("> ")
        whole_command = command.split(" ")

        #user is still at connection stage
        if stage == 0:
            #checks if the command was "connect"
            if whole_command[0].upper() == "CONNECT":
                if(len(whole_command) != 3):
                    #means that either too much input was provided or not enough input was provided
                    print("Unable to connect to the server, check command arguments")
                else:
                    address = whole_command[1]
                    port = whole_command[2]
                    try:
                        #we try to connect to the server using the address and port provided by the user
                        s.connect((address, int(port)))
                        s.recv(256)
                        #we decode the server's response
                        msg = s.recv(256).decode()
                        if msg == "ok connected":
                            #if the connection was successful, we print the following message and move on to the nect stage
                            print("Connected, please log in")
                            stage+=1
                    except Exception:
                        #if an exception occurs, the connection attempt must have been unsuccessful
                        print("Unable to connect to the server, check command arguments")

            #if the command is quit, the program exits
            elif whole_command[0].upper() == "QUIT":
                sys.exit()

            #if the command is neither connect nor quit, then it must be invalid
            else:
                print("invalid command.")

        #login stage
        elif stage == 1:
            #check to see if the command is "login"
            if whole_command[0].upper() == "LOGIN":
                #check to see if the correct amount of input is provided
                if(len(whole_command) != 3):
                    print("Incomplete login criteria")
                else:
                    #we assign the item at index 1 to username and the item at index 2 to passwd
                    username = whole_command[1]
                    passwd = whole_command[2]
                    all_details = "login " + username + " " + passwd #string containing all details needed for the server
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii")) #we send the size to the server, followed by all_details
                    s.send(all_details.encode("ascii"))
                    s.recv(256) #recieves the size of the server response
                    msg1 = s.recv(256).decode() #decodes server response
                    if msg1 == "ok login":
                        #prints following ouput and increments stage if login is successfule
                        print("Logged In!")
                        stage +=1
                    else:
                        #an error must have occured during the login stage
                        print("Invalid login details")
            #if command is quit, the program exits
            elif whole_command[0].upper() == "QUIT":
                sys.exit()
            else:
                print("invalid command")

        #final stage
        else:
            #checks to see if the command is "observe"
            if whole_command[0].upper() == "OBSERVE":
                #check to see if the correct amount of input is provided
                if len(whole_command) != 1:
                    print("invalid command")
                else:
                    #following code block follows similar send/recive process as seen earlier
                    #however, from here on I also strip away the "\x00" from the size returned by the server
                    all_details = "action observe"
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    ret_size = s.recv(256).decode("ascii")
                    new_size = int(str(ret_size).strip("\x00"))
                    msg1 = s.recv(new_size).decode()
                    split_msg1 = msg1.split(" ")
                    i = 2
                    tuples = []
                    #here, we iterate through the message returned from the server and add each item to tuples
                    while i < len(split_msg1):
                        tuples.append(split_msg1[i])
                        i+=1

                    formated_vals = generate_tuples(tuples) #runs generate_tuples function on tuples
                    add_to_all(formated_vals) #runs add_to_all function on formated_vals
                    my_current_rows = generate_rows(formated_vals) #generates current rows based on formated_vals
                    print_vals = draw(my_current_rows) #generates the rows to be outputed for display
                    print("")
                    num_explored_tiles = len(all_tiles)
                    #iterates through print_vals and prints each row to output
                    for element in print_vals:
                        print(element)


            #checks whether the command is "move"
            elif whole_command[0].upper() == "MOVE" or whole_command[0].upper() == "M":
                #checks whether the correct amount of input has been provided
                if len(whole_command) != 2:
                    print("invalid command")
                else:
                    #send/recieve process same as seen earlier
                    all_details = "action move "
                    if whole_command[1].upper() == "N":
                        all_details += "north"
                    elif whole_command[1].upper() == "S":
                        all_details += "south"
                    elif whole_command[1].upper() == "E":
                        all_details += "east"
                    elif whole_command[1].upper() == "W":
                        all_details += "west"
                    else:
                        all_details += whole_command[1]
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    s.recv(256)
                    msg1 = s.recv(256).decode()
                    split_msg1 = msg1.split(" ")
                    #if the response from the server does not begin eith "ok", we print the error message
                    if split_msg1[0] != "ok":
                        print("invalid command")

            #checks if the command is "stats"
            elif whole_command[0].upper() == "STATS":
                #checks if the correct amount of input has been provided
                if len(whole_command) != 1:
                    print("invalid command")
                else:
                    all_details = "action stats"
                    #send/recieve process same as seen earlier
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    s.recv(256)
                    msg1 = s.recv(256).decode()
                    split_msg1 = msg1.split(" ")
                    #if we recieve an "ok" response from the server, then the following code block executes
                    if split_msg1[0] == "ok":
                        #the following code extracts the player's x and y coordinates, as well as the number of tiles explored
                        #after this, the x and y coordinates are added to another string for output
                        #number of tiles explored is also printed to output
                        values = split_msg1[2].split(",")
                        x_coor = values[0].lstrip("(")
                        y_coor = values[1]
                        tiles = values[2].rstrip(")")
                        coor_output = "(" + x_coor + "," + y_coor + ")"
                        print("Number of tiles explored: " + tiles)
                        print("Current position: " + coor_output)


            #checks if the command is the inspect command
            elif whole_command[0].upper() == "INSPECT":
                #checks that the correct amount of inpur has been provided
                if len(whole_command) != 2:
                    print("invalid command")
                else:

                    all_details = "action " + command
                    #send/recieve process same as seen earlier
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    ret_size = s.recv(256).decode("ascii")
                    new_size = int(str(ret_size).strip("\x00"))
                    msg1 = s.recv(new_size).decode()
                    split_msg1 = msg1.split(" ")
                    if split_msg1[0] == "ok":
                        #if the server replies with an "ok" response and the length of the response is 2, then no message must have been sent by the server
                        if len(split_msg1) <=2:
                            print("Nothing interesting was found here")
                        #if the previous conditional was not met, then a message must have been recieved
                        else:
                            #the following code strips "ok inspect" as well as the brackets away from the message
                            #after this, the message is printed to output
                            j = 2
                            message = ""
                            message = msg1.lstrip("ok inspect")
                            message = message.lstrip("(")
                            message = message.rstrip(")")
                            print("You found a note: " + message)

            #checks to see if the command is "note"
            elif whole_command[0].upper() == "NOTE":
                #checks that the correct amount of input is provided
                if len(whole_command) <= 1:
                    print("invalid command")
                else:
                    #send/recieve process same as seen earlier
                    all_details = "action " + command
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    ret_size = s.recv(256).decode("ascii")
                    new_size = int(str(ret_size).strip("\x00"))
                    msg1 = s.recv(new_size).decode()
                    split_msg1 = msg1.split(" ")
                    if split_msg1[0] != "ok":
                        print("invalid command")

            #checks if the command is "message"
            elif whole_command[0].upper() == "MESSAGE":
                #checks that the correct amount of input is provided
                if len(whole_command) <= 1:
                    print("invalid command")
                else:
                    #send/recieve process same as seen earlier
                    all_details = "action " + command
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    ret_size = s.recv(256).decode("ascii")
                    new_size = int(str(ret_size).strip("\x00"))
                    msg1 = s.recv(new_size).decode()
                    split_msg1 = msg1.split(" ")
                    if split_msg1[0] != "ok":
                        print("invalid command")

            #checks to see if the command is the "commit" comand
            elif whole_command[0].upper() == "COMMIT":
                #checks if the correct amount of input is provided
                if len(whole_command) < 1:
                    print("invalid command")
                else:
                    all_details = "action commit"
                    #here, we iterate through all_tiles, and add to all_details the x and y coordinates of each tile, in brackets
                    for item in all_tiles:
                        output = " (" + item[1] + "," + item[3] + ")"
                        all_details += output
                    #send/recieve process same as seen earlier
                    length = len(all_details)
                    size = str(length)
                    s.send(size.ljust(256, ' ').encode("ascii"))
                    s.send(all_details.encode("ascii"))
                    ret_size = s.recv(256).decode("ascii")
                    new_size = int(str(ret_size).strip("\x00"))
                    msg1 = s.recv(new_size).decode()
                    split_msg1 = msg1.split(" ")
                    if split_msg1[0] != "ok":
                        print("error")

            #if the command is quit, the program exits
            elif whole_command[0].upper() == "QUIT":
                sys.exit()

            #if the command is anything else, it is deemed invalid
            else:
                print("invalid command")

