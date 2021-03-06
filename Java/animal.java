//importing
import java.util.scanner;

//to import everything in a library
import java.util.*

//classes are framework for objects
// public
public class Animal {

  // this is a field(attributes)
  // public is available by everything
  //static shared by every objects
  //final can't be changed
  //finals are uppercase
  // doubles have decimals
  public static final double FAVNUMBER = 1.7;

  // private can only be accessed by other methods in the classes
  private String name;
  private int weight;

  //this has default value
  private boolean hasOwner = false;

  // small number (-28, 127)
  private byte age;

  // long is a big number ()-2^63, 2^63)
  private long uniqueID;

  //char is unsighned utf16 codes
  private char favoriteChar;

  private double speed;

  //32 bit number w/o decimals
  private float height;

  //protected only accesible by other code in the package
  protected static int numberOfAnimals = 0;

  //scanner gets input
  static scanner userinput = new Scanner(Ssystem.in);

  //constructor needed to create new Animal

  public Animal() {
    numberOfAnimals++;
    // just checking printing
    int sumOfNumbers = 5+1;
    System.out.println("5+1 = " + sumOfNumbers);

    System.out.print("Enter the name: ");

    // if string entered
    // has next int/float/dpuble/byte/etc for other data types
    if(userInput.hasNextLine()){

      // references lasest object which is Animal
      // next line gets the input
      this.setName(userInput.nextLine());
    }
  }

  public String getName(){
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  // void main is main code that runs
  public static void main(String[] args) {
    Animal theAnimal = newAnimal();
  }
}


 
