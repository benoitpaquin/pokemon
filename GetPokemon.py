# get list of pokemon from the pokeapi
# Functions:
# get_pokemon_data: collects from the pokeapi, a set of pokamons and some of their attributes
# create_dict_entry: called by get_pokemon_data with the attributed of the pokemon to create a dictionary
# write_to_csv: write the CSV formatted result to a csv file
# write_to_json: write the JSON formatted result to a json file

## Imports
import pokebase as pb
import json
import csv

## Global variables
DEBUG = True # Print progress reports and stats for debugging
# retain only pokemons that have played in valid_games
valid_games = ["red", "blue", "leafgreen", "white"] 
# output file name
csv_file = 'pokemon.csv' 
json_file = 'pokemon.json'

def create_dict_entry(id, name, base_experience, height, weight, bmi, order, slot1, slot2, sprite):
# Take the attributes of a pokemon passed as argument and create a dictionary 
    return {
        "id": id,
        "name": name,
        "base_experience": base_experience,
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "order": order,
        "slot1": slot1,
        "slot2": slot2,
        "sprite": sprite
    }


def get_pokemon_data(valid_games):
    # arguments:
    #    valid_games: a list with game colours. Only retain pokemons that played in any of the colours on the list
    # results:
    #    a list of dictionaries that can easily be exported to JSON or CSV
    #
    # Get all the pokemons
    all_pokemons = (pb.APIResource("pokemon", "")).results
    # as each pokemon's attribute are read, they are stored into a dict and apprended to the list_of_dict
    # list_of_dict is the result of this function
    list_of_dict = []
    for pokemon in all_pokemons:
        # determine if pokemon played in our valid game set
        games = [x.version.name for x in pokemon.game_indices]
        if any(item in games for item in valid_games):
            id = pokemon.id
            name = pokemon.name.capitalize()
            height = pokemon.height / 10  # in meters
            weight = pokemon.weight / 10  # in kilos
            bmi = weight / (height**2)
            order = pokemon.order
            base_experience = pokemon.base_experience
            slots = [x.type.name for x in pokemon.types]  # assume first entry is always slot 1
            slot1 = slots[0]
            slot2 = slots[1] if len(slots) == 2 else ""
            sprite = pokemon.sprites.front_default
            if DEBUG:
                print(
                    "Id {}, Name {}, Base Experience {}, Heigh {}, Weight {}, BMI {:0.1f}, Order {}, Slot1 {}, Slot2 {}, Sprite URL {}".format(
                        id,
                        name,
                        base_experience,
                        height,
                        weight,
                        bmi,
                        order,
                        slot1,
                        slot2,
                        sprite
                    )
                )
            # append to result
            list_of_dict.append(create_dict_entry(id, name, base_experience, height, weight, bmi, order, slot1, slot2, sprite))
        else:
            if DEBUG: print("Skipping {}".format(pokemon.id))
    return list_of_dict

def write_to_csv(list_of_dict, file_name):
# Write a csv formatted file  
    file = open(file_name, 'w')
    writer = csv.DictWriter(file, fieldnames=["id", "name", "base_experience", "height", "weight", "bmi", "order", "slot1", "slot2", "sprite"])
    writer.writeheader()
    writer.writerows(list_of_dict)
    file.close()

def write_to_json(list_of_dict, file_name):
# Write a JSON formatted file  
    file = open(file_name, 'w')
    json.dump(list_of_dict,file)
    file.close()

# start of program
if DEBUG: print("starting")
list_of_dict = get_pokemon_data(valid_games)
write_to_csv(list_of_dict, csv_file)
write_to_json(list_of_dict, json_file)
if DEBUG: print(json.dumps(list_of_dict, indent=2))
if DEBUG: print("Found {} pokemons in {} games".format(len(list_of_dict),", ".join(valid_games)))