from random import choice

# Dictionary: Power -> Pokemon Name
pokemons = {5: "Pikachu", 1:"Pichu", 3: "Gaslee", 2: "ALEGAXZAM", 4: "Richu"}

# Reverse Dictionary: Pokemon Name -> Power
rpokemons = {"Pikachu": 5, "Pichu": 1, "Gaslee":3, "ALEGAXZAM": 2, "Richu": 4}

def pokemon_game():
    try: 
        caught = []
        max_pokemon = None
        min_pokemon = None

        for _ in range(len(pokemons)):
            print("\n\t---- WALKING INTO A JUNGLE ----")
            pokemon = choice(list(rpokemons.keys()))  # Randomly select a Pokémon name
            power = rpokemons[pokemon]
            print(f"You caught {pokemon} (Power: {power})")
            caught.append((pokemon, power))

            # Update max and min
            if not max_pokemon or power > max_pokemon[1]:
                max_pokemon = (pokemon, power)
            if not min_pokemon or power < min_pokemon[1]:
                min_pokemon = (pokemon, power)

            print(f"Strongest so far: {max_pokemon[0]} (Power: {max_pokemon[1]})")
            print(f"Weakest so far: {min_pokemon[0]} (Power: {min_pokemon[1]})")

    except Exception as e:
        print("ERROR:", e)

pokemon_game()

#EZ
