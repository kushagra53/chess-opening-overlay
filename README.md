# Chess Opening Detector

A lightweight Tampermonkey userscript that identifies the current chess opening and variation during live games by matching played moves against the ECO (Encyclopaedia of Chess Openings) database.

## Features

* Detects opening names in real time
* Detects opening variations as the game progresses
* Displays ECO codes
* Updates automatically during the opening phase
* Marks games as "Out of Book" once no matching opening line exists
* Lightweight on system resources
* No engine analysis
* No move recommendations
* No evaluation bar
* No opening explorer statistics

## Example

During a game the overlay may display:

Opening: Sicilian Defense

Variation: Najdorf Variation

ECO: B90

If the game leaves known opening theory:

Opening: Sicilian Defense

Variation: Najdorf Variation

ECO: B90

Status: Out of Book

## Installation

### Step 1: Install Tampermonkey

Install Tampermonkey for your browser:

https://www.tampermonkey.net

### Step 2: Install the Script

1. Open `opening-detector.user.js`
2. Copy the contents
3. Open Tampermonkey Dashboard
4. Create a New Script
5. Replace the default template with the script contents
6. Save

### Step 3: Open Chess.com

Navigate to a live game on Chess.com.

The opening detector overlay should appear automatically.

## How It Works

The script:

1. Reads the moves played in the current game
2. Matches the move sequence against the ECO opening database
3. Finds the deepest matching opening line
4. Displays the opening name, variation name, and ECO code
5. Stops updating when the game leaves known opening theory

## Project Structure

```text
chess-opening-detector/
│
├── opening-detector.user.js
├── README.md
├── LICENSE
└── screenshots/
```

## Limitations

* Depends on Chess.com page structure
* Future Chess.com updates may require script updates
* Opening recognition is only as complete as the ECO database used
* Does not provide opening training, recommendations, or analysis

## Fair Play

This project is intended for opening identification only.

The script does not:

* Suggest moves
* Display engine evaluations
* Provide best-move recommendations
* Show opening explorer statistics
* Offer any form of computer-assisted analysis

Users are responsible for ensuring compliance with the rules and fair-play policies of the platforms on which they use this software.

## Contributing

Issues, bug reports, and pull requests are welcome.

If Chess.com updates its interface and breaks move detection, please open an issue with screenshots and browser information.

## License

MIT License
