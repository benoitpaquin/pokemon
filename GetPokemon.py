# get list of pokemon
import pokebase as pb
import json
import csv

## Global variables
DEBUG = True
valid_games = ["red", "blue", "leafgreen", "white"]
csv_file = 'pokemon.csv'
json_file = 'pokemon.json'


def create_dict_entry(id, name, base_experience, height, weight, bmi, order, slot1, slot2, sprite):
    # arguments:
    # all of the pokemon data that needs to be put in dictionary
    # result:
    # a dictionary
    # ---------
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
    #    a list of dictionaries that can easily be exported to JSON, each entries has:
    #       id: the id of the pokemon
    #       name: The name of the pokemon with the first letter capitalized
    #       ...
    # ---------------------
    # Get all the pokemons
    all_pokemons = (pb.APIResource("pokemon", "")).results
    #if DEBUG: all_pokemons = all_pokemons[:3]
    result = []
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
            slots = [
                x.type.name for x in pokemon.types
            ]  # assume first entry is always slot 1
            slot1 = slots[0]
            slot2 = slots[1] if len(slots) == 2 else ""
            sprite = pokemon.sprites.front_default
            print("---")
            print(sprite)
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
            result.append(create_dict_entry(id, name, base_experience, height, weight, bmi, order, slot1, slot2, sprite))
        else:
            if DEBUG: print("Skipping {}".format(pokemon.id))
    return result
def write_to_csv(list_of_dict):

    file = open(csv_file, 'w')
    writer = csv.DictWriter(file, fieldnames=["id", "name", "base_experience", "height", "weight", "bmi", "order", "slot1", "slot2", "sprite"])
    writer.writeheader()
    writer.writerows(list_of_dict)
    file.close()

def write_to_json(list_of_dict):

    file = open(json_file, 'w')
    json.dump(list_of_dict,file)
    file.close()
# start of program
if DEBUG: print("starting")
list_of_dict = get_pokemon_data(valid_games)
write_to_csv(list_of_dict)
write_to_json(list_of_dict)

print(json.dumps(list_of_dict, indent=2))
if DEBUG: print("Found {} pokemons in {} games".format(len(list_of_dict),", ".join(valid_games)))

