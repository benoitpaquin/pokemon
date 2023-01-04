# Pokemon

## Overview
Get a list of all Pokémons that have played in the Red, Blue, Leafgreen and White games from the PokéApi https://pokeapi.co/
For each Pokémon get these attributes:
 - Id
 - Name
 - Height
 - Weight
 - Bmi (calculated from Height and Weight)
 - Base Experience
 - Order
 - Slot 1 and 2 if available
 - Sprite default image
 
 As the name is an identifiable GDPR component, an additional attribute is created 'Name_pii' containing the hash of the name. 
 
 The system exports a single JSON file as well as a CSV files. As the number of Pokémon is limited, a single file solution was selected. 
 
## Implementation
The solution was built using Visual Studio Code and Python on a Linux virtual machine running in a Chromebook. A virtual environment for Python was used (VENV) to hold all the environment and the dependencies (IMPORTS). 

The pokebase framework (https://github.com/PokeAPI/pokebase) was used to access the PokéApi. The CSV and JSON framework we used to generate the output files. 

## Process
As the amount of Pokémons and their attributes are limited in number and size, the data was collected into a Python vector. Each element of the vector represents a Pokémon and the data for the Pokémon is stored into a Python dictionary. This structure (a list of dictionaries) was selected as the utilities to export CSV and JSON data are compatible with this structure.

The high level process is simple: 
1. Initialize an empty list of Pokémons.
2. Get a list of all Pokémons using the pokebase framework. 
3. For each Pokémon, extract the games they were part of.
4. If the current Pokémon played in one of the 4 games we are interested in, extract its attributes. If not, skip the Pokémon.
5. Once all of the attributes are extracted, call a utility to create a dictionary with the attributes and append the dictionary to the list of Pokémons.
6. Once all Pokémons are processed, call a set of utilities to create a CSV and JSON file.
5. Append the dictionary to 
