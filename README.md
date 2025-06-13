# Pokémon Jungle Adventure Game

A simple Python game where you walk into a jungle and catch random Pokémon!  
Each Pokémon has a different power level. The game keeps track of the strongest and weakest Pokémon you've caught so far.

---

## How to Play

1. **Run the script**  
   Simply execute the Python file.  
   ```
   python pokemon_game.py
   ```

2. **Gameplay**  
   - The game will simulate you walking into a jungle multiple times (once for each unique Pokémon).
   - Each time, you catch a random Pokémon.
   - After each catch, the game displays:
     - The Pokémon you caught and its power.
     - The strongest Pokémon you've caught so far.
     - The weakest Pokémon you've caught so far.

---

## Example Output

```
    ---- WALKING INTO A JUNGLE ----
You caught Pikachu (Power: 5)
Strongest so far: Pikachu (Power: 5)
Weakest so far: Pikachu (Power: 5)

    ---- WALKING INTO A JUNGLE ----
You caught Pichu (Power: 1)
Strongest so far: Pikachu (Power: 5)
Weakest so far: Pichu (Power: 1)
...
```

---

## Pokémon in the Game

| Name       | Power |
|------------|-------|
| Pikachu    | 5     |
| Pichu      | 1     |
| Gaslee     | 3     |
| ALEGAXZAM  | 2     |
| Richu      | 4     |

---

## Code Structure

- **pokemons (dict):** Maps power to Pokémon name.
- **rpokemons (dict):** Maps Pokémon name to power.
- **pokemon_game():**  
  - Main function for the game loop.
  - Randomly selects a Pokémon to "catch".
  - Tracks and prints the strongest and weakest Pokémon caught so far.
- **Error Handling:**  
  - Catches and prints exceptions if something goes wrong.

---

## Requirements

- Python 3.x

---

## Notes

- All Pokémon catches are random.
- You can easily add or modify Pokémon in the `pokemons` and `rpokemons` dictionaries.
- For fun! #EZ

---

## License

Free to use for educational and fun purposes!
