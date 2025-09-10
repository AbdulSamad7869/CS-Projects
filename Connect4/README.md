# Connect 4 (Java Console Game)

A simple two-player **Connect 4** game implemented in Java.  
The game is played entirely in the terminal and supports two human players taking turns.

---

## 🎮 Features
- Classic **6x7 Connect 4 board**
- Two-player mode (Player 1 = `X`, Player 2 = `O`)
- Input validation for moves:
  - Only accepts numbers `1–7`
  - Prevents moves in full columns
- Win detection:
  - Horizontal
  - Vertical
  - Diagonal (both directions)
- Detects draws when the board is full
- Clear console output for a cleaner game board

---

## 📖 Rules
1. Players take turns dropping their pieces (`X` for Player 1, `O` for Player 2) into one of the 7 columns.
2. The piece will fall to the lowest available space in the chosen column.
3. The first player to connect **4 in a row** (horizontally, vertically, or diagonally) wins.
4. If the board fills up with no winner, the game ends in a **draw**.

---

## ▶️ How to Run

1. Save the file as **`Connect4.java`**.
2. Compile the program:
   ```bash
   javac Connect4.java
3. Run the game:
   ```bash
   java Final_Connect4.java
   ```
   ---

## ⌨️ Gameplay Example

```text
||WELCOME TO CONNECT 4||
Type rules for the rules or type start to start the game: start
 1  2  3  4  5  6  7

 -  -  -  -  -  -  - 
 -  -  -  -  -  -  - 
 -  -  -  -  -  -  - 
 -  -  -  -  -  -  - 
 -  -  -  -  -  -  - 
 -  -  -  -  -  -  - 

Player 1 input a column from 1-7:
```
---
