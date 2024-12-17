import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day6 {

    private static String[][] grid;
    private static int row;
    private static int col;

    public static void main(String[] args) {
        ArrayList<String> fileData = getFileData("src/InputFile");
        int rows = fileData.size();
        int columns = fileData.get(0).length();
        grid = new String[rows][columns];

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                grid[r][c] = fileData.get(r).substring(c, c+1);
            }
        }

        findGuard();
        
    }


    public static ArrayList<String> getFileData(String fileName) {
        ArrayList<String> fileData = new ArrayList<String>();
        try {
            File f = new File(fileName);
            Scanner s = new Scanner(f);
            while (s.hasNextLine()) {
                String line = s.nextLine();
                if (!line.equals(""))
                    fileData.add(line);
            }
            return fileData;
        }
        catch (FileNotFoundException e) {
            return fileData;
        }
    }

    public static void printMap() {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }
    }

    public static void findGuard() {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j].equals("^") || grid[i][j].equals(">") || grid[i][j].equals("v") || grid[i][j].equals("<")) {
                    row = i;
                    col = j;
                    break;
                }
            }
        }
    }

    public static void move() {
        String current = grid[row][col];
        if (current.equals("^")) {
            grid[row][col] = "X";
            if (row - 1 >= 0) {
                if (grid[row - 1][col].equals(".")) {
                    grid[row - 1][col] = "^"; 
                } else {
                    
                }
            }

        } else if (current.equals(">")) {
            grid[row][col] = "X";
            if (col + 1 < grid[0].length) {
                if (grid[row - 1][col].equals(".")) {
                    grid[row][col + 1] = ">";
                } else {
                    if (row + 1 < grid.length || (grid[row + 1][col].equals("."))) {
                        
                    }
                }
            }
        } else if (current.equals("v")) {
            grid[row][col] = "X";
            if (row + 1 < grid.length) {
                if (grid[row - 1][col].equals(".")) {
                    grid[row + 1][col] = "v";
                } else {
                    
                }
            }
        } else if (current.equals("<")) {
            grid[row][col] = "X";
            if (col - 1 >= 0) {
                if (grid[row - 1][col].equals(".")) {
                    grid[row][col - 1] = "<";
                } else {
                    
                }
            }
        }
    }

    public static boolean win(int rowIndex, int colIndex) {
        return (rowIndex < 0 || rowIndex >= grid.length || colIndex < 0 || colIndex >= grid[0].length);
    }

    public static int distinctPositions() {
        int sum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j].equals("X")) {
                    sum++;
                }
            }
        }
        return sum;
    }

}
