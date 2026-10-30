# Alex Moreno
# Gathering of ideas such as villain name, locust army, translation
# Any additional context related to specific theme of game
# Was researched online & use of ChatGPT for idea generation to enrich story

# Customized sample code
directions = ['North', 'South', 'East', 'West']
exit_command = 'Exit'
valid_inputs = directions + [exit_command]
invalid_direction = 'The locusts begin digging through the walls...\n' +  'Try these directions: ' + \
    str(valid_inputs) + '.'
wrong_way = 'Abaddon snickers at your choice of direction...'
game_over = 'Thank you for playing.'
exit_room_sentinel = 'exit'

# Function to show introduction to game
def show_intro():
    print('Evil Deterred: a Text-Based Dungeon Game')
    print("Navigate through Abaddon's Underworld Challenge")
    print('Collect all six items to survive...')
    print('Or be trapped for eternity by the locust minions')
    print('\n')

show_intro()

# Function to show instructions to game
def show_instructions():
    print('You have 4 movement commands:')
    print('North, South, East, or West')
    print('You have 2 interaction commands:')
    print('Yes, No')
    print('\n')

show_instructions()

# Function for if player is killed
def killed():
    print('You have not gathered the items to fight...')
    print('The locusts erupt through the walls.')
    print("You're enveloped...")
    print('Abaddon condemns your soul for Eternity.')
    print(game_over)

# Main function to play game
def main():

    # 2-D Dictionary linking rooms and items
    rooms = {
        'Awakening': {'North': 'Agony', 'East': 'Calamity', 'South': 'Sorrow', 'West': 'Turmoil'},
        'Agony': {'East': 'Hall of Entrapment', 'South': 'Awakening', 'item': 'Holy Urn'},
        'Hall of Entrapment': {'West': 'Agony', 'item': 'Abaddon'},  # Villain
        'Turmoil': {'East': 'Awakening', 'item': 'Vial 2'},
        'Calamity': {'West': 'Awakening', 'North': 'Cruelty', 'item': 'Vial 1'},
        'Cruelty': {'South': 'Calamity', 'item': 'Sigil Stone'},
        'Sorrow': {'North': 'Awakening', 'East': 'Malice', 'item': 'Soulshield Amulet'},
        'Malice': {'West': 'Sorrow', 'item': 'Vial 3'}
    }

    # Setting current room, initiate empty inventory, incomplete inventory boolean
    current_room = 'Awakening'
    inventory = []
    complete_inventory = False

    # Function to get item with if-else scenarios
    def get_item():
        print('You see: {}'.format(rooms[current_room]['item']))
        acquire_item = input('Do you pick it up? [Yes/No]\n')

        if acquire_item == 'Yes':
            inventory.append(rooms[current_room]['item'])

        else:
            print('Well, you really should. Leave the room and try again.')

    # Function to handle navigation, decision branches for various scenarios, listed if-else statements
    def navigate(current_room: str, user_input: str):
        next_room = current_room
        err_msg = ""

        if user_input == exit_command:
            next_room = exit_room_sentinel
            err_msg = game_over

        elif user_input in directions:

            if user_input in rooms[current_room]:
                next_room = rooms[current_room][user_input]

            else:
                err_msg = wrong_way
                print('You can go:')

                for key, value in rooms[current_room].items():
                    print('{} to {}'.format(key, value))

        else:
            err_msg = invalid_direction

        return next_room, err_msg

    # while statement for displaying room, inventory
    while current_room != exit_room_sentinel:
        print('\n')
        print("You're in", current_room)
        print('You have acquired: ', inventory)

        # Nested if statement for non-villain room & room has an item
        if rooms[current_room].get('item') != None:

            if rooms[current_room].get('item') != 'Abaddon':
                print('You see:', rooms[current_room].get('item'))

        # Line separator for ease of reading
        print('-----' * 5, '\n')

        # Nested if-else statements for only showing item in room if item is in the room
        # If the player does not have item in inventory
        # Deleting the item key from rooms dictionary
        # Will complete the inventory variable = True once all items collected
        if rooms[current_room].get('item') != None:

            if (rooms[current_room].get('item') not in inventory) and (rooms[current_room].get('item') != 'Abaddon'):
                grab = input('Do you grab it? [Yes/No]\n')

                if grab == 'Yes':
                    inventory.append(rooms[current_room]['item'])
                    del rooms[current_room]['item']

                    if len(inventory) == 6:
                        print('You have now collected all of the items')
                        print('Next objective: Find the Baphomet Symbol')
                        complete_inventory = True

                else:
                    print('Are you sure? Exit the room and try again.')

            # Meeting villain without complete inventory, player is killed, game over
            elif (rooms[current_room].get('item') == 'Abaddon') and (complete_inventory == False):
                killed()
                break

            # Handling villain room with complete inventory
            # Decision branching based on choices of user input
            elif (rooms[current_room].get('item') == 'Abaddon') and (complete_inventory == True):
                print('You have found the Baphoment symbol.')
                print('You can choose to end evil for good, or let the world burn...')
                spawn = input('Do you spawn Abaddon? [Yes/No]\n')

                if spawn == 'Yes':
                    print('You pour the vials onto the Baphomet Symbol.')
                    print('Abaddon rises through the depths...')
                    cast = input('Do you use your Sigil Stone to cast the Confiment Spell? [Yes/No]\n')

                    if cast == 'Yes':
                        # Confinement phrase was a mytholigical Enochian translation via ChatGPT
                        # Roughly translates to "I confine you to the Holy Urn."
                        print(
                            "You speak the Enochian Confinement phrase: Zodar e'laran belthorium kha'zel, melchonar en'karithor."
                        )
                        print('Congratulations, you have successfully ended evil.')
                        print(game_over)
                        current_room = exit_room_sentinel
                        break

                    # If input wasn't Yes, player has a unique death
                    else:
                        print('Abaddon: HAHA I knew you were a weakling.')
                        print('Abaddon: Face damnation, weak one.')
                        print('The locusts envelope your soul...')
                        print(game_over)
                        current_room = exit_room_sentinel
                        break

                # If No was explicitly input, player has a different unique death
                elif spawn == 'No':
                    print('Abaddon: Your inability to fight is laughable.')
                    print('Abaddon: Face eternity!')
                    print('The locusts envelope your soul.')
                    print(game_over)
                    current_room = exit_room_sentinel
                    break

                # If player enters anything other than Yes/No at spawn, reminder of only two options.
                else:
                    print('Yes and no are the only options.')
                    cast = input('Do you use your Sigil Stone to cast the Confinement Spell? [Yes/No]\n')

        user_input = input('Which direction do you go?\n')
        current_room, err_msg = navigate(current_room, user_input)

        if err_msg != "":
            print(err_msg)



main()