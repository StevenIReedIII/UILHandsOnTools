import java.util.*;
import java.io.*;

public class DryRun {
  public static void main(String[] args) {
    Scanner scan = new Scanner(new File("dryrun.dat"));
    int times = Integer.parseInt(scan.nextLine());
    for(int i = 0; i < times; i++){
      System.out.println("I love " + scan.nextLine() + ".");
    }
  }
}
