# get list of pokemon
import pokebase as pb
## Global variables
valid_games =  ["red", "blue1", "leafgreen1", "white1"]
def create_dict_entry(id, name, base_experience, height, weight, bmi, order):
    # arguments:
    # all of the pokemon data that needs to be put in dictionary
    # result: 
    # a dictionary
    #---------
    return {'id':id, "name": name, "base_experience" : base_experience, "height": height, "weight":weight, "bmi": bmi, "order":order}

def get_pokemon_data(valid_games):
    # arguments:
    #    valid_games: a list with game colours. Only retain pokemons that played in any of the colours on the list
    # results:
    #    a list of dictionaries that can easily be exported to JSON, each entries has:
    #       id: the id of the pokemon
    #       name: The name of the pokemon with the first letter capitalized
    #       ...
    #---------------------
    # Get all the pokemons
    all_pokemons = pb.APIResource('pokemon','')
    all_pokemons = all_pokemons.results
    for pokemon in all_pokemons:
        # determine if pokemon played in our valid game set
        result = []
        games = [x.version.name for x in pokemon.game_indices] 
        if any(item in games for item in  ["red", "blue", "leafgreen", "white"]):
            id = pokemon.id
            name = pokemon.name.capitalize()
            height = pokemon.height/10 # in meters
            weight = pokemon.weight/10 # in kilos
            bmi = weight/(height**2) 
            order = pokemon.order
            base_experience = pokemon.base_experience
            print("Id {}, Name {}, Base Experience {}, Heigh {}, Weight {}, BMI {:0.1f}, Order {}".format(id, name, base_experience, height, weight, bmi, order))
        else:
            print("Skipping {}".format(pokemon.id))

# def get_pokemon_data(id): 
#     data = pb.pokemon(id)
#     #get all games the pokemon is member of
#     games = [x.version.name for x in data.game_indices]
#     if any(item in games for item in  ["red", "blue1", "leafgreen1", "white1"]):
#         name = data.name.capitalize()
#         height = data.height/10 # in meter
#         weight = data.weight/10 # in kilo
#         bmi = weight/(height**2)  
#         print("Id {}, Name {}, Base Experience {}, Heigh {}, Weight {}, BMI {:0.1f}, Order {}".format(id, name, data.base_experience, height, weight, bmi, data.order))
#     else:
#         print("not in the right game")
print("starting")
get_pokemon_data(valid_games)
# View Pokemon from this generation number.
# cnt = 0
# for gen in list(range(1,9)):
        
#     gen_resource = pb.generation(gen)
#     # Iterate through the list of Pokemon introduced in that generation.
#     print("generation {}".format (gen))
#     for pokemon in gen_resource.pokemon_species:
#         cnt = cnt+1
#         print('{}: {} {}'.format(pokemon.id_,pokemon.name.title(),cnt))
#     #    get_pokemon_data(pokemon.id_)

#a=pb.APIResourceList('pokemon')
#for x in a:
#    a.name
