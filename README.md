# Game Console Menu

A text-based game console menu built in Python using a `while` loop and `match-case` statements, including a nested settings menu.

## What it does

- Shows a game console menu in a loop until the user exits
- Handles commands with `match-case`: Start Game, Instructions, High Score, Settings, and Exit
- Includes a nested `match-case` inside Settings (Sound, Difficulty, Back)
- Normalizes input with `.title()`, so commands work in any letter case
- Falls back to an "Invalid command!" message for anything unrecognized

## How to run

```bash
python game_console.py
```

Type a command **by name** (not by number) when prompted, for example `start game` or `Instructions`. Matching is not case-sensitive.

## Commands

| Command | What it does |
|---|---|
| Start Game | Starts the game and wishes you luck |
| Instructions | Shows the controls (W/A/S/D) and the goal |
| High Score | Shows the current high score |
| Settings | Opens a sub-menu: Sound, Difficulty, or Back |
| Exit | Quits the program |

## Example

```
========= Game Console =========

1- Start Game
2- Instructions
3- High Scores
4- Settings
5- Exit

=================================
Enter your command: high score
High Score: 1299
```

## Status

This is a small learning project exploring `match-case`, nested menus, and loops.

Planned improvements:
- Accept menu numbers (1-5) as well as command names
- Make the settings actually change something (volume level, difficulty)
- Update and save the high score after a game

## Author

Built while learning Python fundamentals: `while` loops, `match-case`, and string methods.

## Regards 
Hasham-Hameed
