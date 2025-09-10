import java.security.cert.X509Certificate;
import java.util.Objects;
import java.util.Scanner;
 
public class Connect4 {
    public static final Scanner in = new Scanner(System.in);
    public static String[][] spaces = new String[6][7];
 
    public static void main(String[] args) { //main method that runs the game
        gameStart();
        //playerVSComputer();
    }
 
    //this method is executed at the start of the program
    // and introduces the game and asks for user input to start game or get rules
    public static void gameStart() {
        for (int j = 0; j < 6; j++) {
            for (int h = 0; h < 7; h++) {
                spaces[j][h] = " - ";
            }
        }
        System.out.println("||WELCOME TO CONNECT 4||");
        System.out.print("Type \033[3mrules\033[0m for the rules or type \033[3mstart\033[0m to start the game: ");
        String option = in.nextLine().toLowerCase();
        boolean game = false;
        while (!game) {
            if (option.equals("start")) { //if user types start this moves to the next method
                running();
                game = true;
            } else if (option.equals("rules")) { //part for if user types rules
                rules();
                System.out.print("Type start when ready: ");
                String newOption = in.nextLine();
                Boolean optionStart = false;
                while (!optionStart) { //tests for valid input and only stops when valid input is given
                    if (!newOption.equals("start")) {
                        System.out.print("Only input is start: ");
                        newOption = in.nextLine();
                    } else {
                        optionStart = true;
                    }
                }
                running();
                game = true;
            } else {
                option = options(option);
            }
 
        }
    }
 
    //This method is for if user doesn't type start or rules in gameStart method,
    // it will run until the user types a valid input
    public static String options(String option) {
        boolean input = false;
        while (!input) {
            if (option.equals("start")) {
                option = "start";
                input = true;
                //return option;
            } else if (option.equals("rules")) {
                option = "rules";
                input = true;
                //return option;
            } else {
                System.out.print("Must type either rules or start: ");
                option = in.nextLine();
            }
        }
        return option;
 
    }
 
    //this method is used when user asks for the rules and contains the statement with the rules
    public static void rules() {
        System.out.println("Rules are simple, first to connect 4 pieces of their color vertically, \nhorizontally, or diagonally wins.\n ");
    }
 
    //method that clears the screen each time the game board appears so the screen look cleaner
    public static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
 
 
    //method that prints out the game board so the player(s) can see it and use it to play game
    public static void gameBoard() {
        clearScreen();
        updatedGameBoard();
    }
 
 
    //method used for player1's input, used in both computer and 2 player games
    // it also prints out the first X on the board whenever the user types a number between 1 and 7
    public static void running() {
    boolean winner = false;

    while (!winner) {
        gameBoard();
        int moveP1 = properInt(getInt("Player 1 input a column from 1-7: "));
        int row = getRow(moveP1);
        if (row >= 0) {
            spaces[row][moveP1 - 1] = " X ";
            winner = isWinner();
        } else {
            System.out.println("Column is full! Try again.");
            continue;
        }

        if (winner) break;

        gameBoard();
        int moveP2 = properInt(getInt("Player 2 input a column from 1-7: "));
        row = getRow(moveP2);
        if (row >= 0) {
            spaces[row][moveP2 - 1] = " O ";
            winner = isWinner();
        } else {
            System.out.println("Column is full! Try again.");
        }
    }
}


    public static int properInt(int move) {
    while (move < 1 || move > 7) {
        System.out.print("Invalid input, must be between 1 and 7: ");
        move = in.nextInt();
        in.nextLine();
    }
    return move;
}


    public static int getInt(String prompt) {
    System.out.print(prompt);
    while (!in.hasNextInt()) {
        in.next(); // discard invalid input
        System.out.println("Not an integer; try again.");
        System.out.print(prompt);
    }
    int value = in.nextInt();
    in.nextLine();
    return value;
}

 
     // get next available opening from a column
    public static int getRow(int column) {
    for (int i = 5; i >= 0; i--) { // start from bottom
        if (spaces[i][column - 1].equals(" - ")) {
            return i;
        }
    }
    return -1; // column full
}
 
    public static boolean isWinner() {
    // Check horizontal
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            if (!spaces[i][j].equals(" - ") &&
                spaces[i][j].equals(spaces[i][j+1]) &&
                spaces[i][j].equals(spaces[i][j+2]) &&
                spaces[i][j].equals(spaces[i][j+3])) {
                gameBoard();
                System.out.println(spaces[i][j].equals(" X ") ? "Player 1 wins!" : "Player 2 wins!");
                return true;
            }
        }
    }

    // Check vertical
    for (int j = 0; j < 7; j++) {
        for (int i = 0; i < 3; i++) {
            if (!spaces[i][j].equals(" - ") &&
                spaces[i][j].equals(spaces[i+1][j]) &&
                spaces[i][j].equals(spaces[i+2][j]) &&
                spaces[i][j].equals(spaces[i+3][j])) {
                gameBoard();
                System.out.println(spaces[i][j].equals(" X ") ? "Player 1 wins!" : "Player 2 wins!");
                return true;
            }
        }
    }

    // Check diagonals (\)
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            if (!spaces[i][j].equals(" - ") &&
                spaces[i][j].equals(spaces[i+1][j+1]) &&
                spaces[i][j].equals(spaces[i+2][j+2]) &&
                spaces[i][j].equals(spaces[i+3][j+3])) {
                gameBoard();
                System.out.println(spaces[i][j].equals(" X ") ? "Player 1 wins!" : "Player 2 wins!");
                return true;
            }
        }
    }

    // Check diagonals (/)
    for (int i = 3; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            if (!spaces[i][j].equals(" - ") &&
                spaces[i][j].equals(spaces[i-1][j+1]) &&
                spaces[i][j].equals(spaces[i-2][j+2]) &&
                spaces[i][j].equals(spaces[i-3][j+3])) {
                gameBoard();
                System.out.println(spaces[i][j].equals(" X ") ? "Player 1 wins!" : "Player 2 wins!");
                return true;
            }
        }
    }

    // Check for draw
    boolean full = true;
    for (int j = 0; j < 7; j++) {
        if (getRow(j+1) != -1) {
            full = false;
            break;
        }
    }
    if (full) {
        gameBoard();
        System.out.println("It's a draw!");
        return true;
    }

    return false;
}
 
    // This method makes the grid with a bunch of null values and gets the size of the columns and rows
    public static void updatedGameBoard() {
        System.out.println(" 1  2  3  4  5  6  7");
        System.out.println();
        char[][] board = new char[6][7];
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(spaces[i][j]);
            }
            System.out.println();
        }
    }
 }
