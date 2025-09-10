# Connect 4 (Java)

A simple **two-player Connect 4 game** implemented in Java, playable in the console. Players take turns dropping their pieces into a 7x6 grid, aiming to connect four of their pieces **vertically, horizontally, or diagonally**.  

---

## Table of Contents
- [Features](#features)  
- [Gameplay](#gameplay)  
- [Rules](#rules)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Screenshots](#screenshots)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features
- Console-based 7x6 Connect 4 game.  
- Two-player mode.  
- Input validation to prevent invalid moves.  
- Automatic detection of win or draw.  
- Clear and updated game board display after each move.  

---

## Gameplay
1. Run the program.  
2. Choose either:
   - `start` → to begin the game immediately.  
   - `rules` → to read the rules before starting.  
3. Players take turns entering a column number (1–7) to drop their piece:
   - **Player 1:** `X`  
   - **Player 2:** `O`  
4. The game continues until:
   - A player connects 4 pieces, or  
   - All columns are full (resulting in a draw).  

---

## Rules
- Players alternate turns.  
- A player wins by connecting **four pieces** in a:
  - Row  
  - Column  
  - Diagonal (\ or /)  
- If the board is full and no player has connected 4, the game ends in a **draw**.  

---

## Installation
1. Ensure you have **Java JDK** installed (Java 8 or higher).  
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/connect4-java.git
