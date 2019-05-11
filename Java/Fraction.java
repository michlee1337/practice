import java.util.Collections;
import java.util.ArrayList;

public class Fraction extends Number implements Comparable<Fraction> {
  // declare attributes
  private Integer num;
  private Integer den;

  // getters and setters

  public void setNum(Integer num) {
    this.num = num;
  }

  public Integer getNum() {
    return num;
  }

  public void setDen(Integer den) {
    this.den = den;
  }

  public Integer getDen() {
    return den;
  }

  // helper
  private static Integer gcd(Integer m, Integer n) {
    while (m%n != 0) {
      Integer oM = m;
      Integer oN = n;

      m = oN;
      n = oM % oN;
    }
    return n;
  }

  // constructor

  public Fraction(Integer num, Integer den) {
    this.num = num;
    this.den = den;
  }

  public Fraction(Integer n) {
    this.num = n;
    this.den = 1;
  }

  // addition

  public Fraction add(Fraction f) {
    Integer nNum, nDen, comD;

    nNum = this.num*f.getDen() + f.getNum()*this.den;
    nDen = this.den * f.getDen();
    comD = gcd(nNum, nDen);
    return new Fraction(nNum/ comD, nDen/ comD);
  }

  public Fraction add(Integer n) {
    Fraction f = new Fraction(n);
    return add(f);
  }

  // object functions

  public String toString() {
    return num.toString() + "/" + den.toString();
  }

  // Number functions
  public double doubleValue(){
    return num.doubleValue() / den.doubleValue();
  }

  public float floatValue() {
    return num.floatValue() / den.floatValue();
  }

  public int intValue(){
    return num.intValue() / den.intValue();
  }

  public long longValue(){
    return num.longValue() / den.longValue();
  }

  // Comparable functions
  public int compareTo(Fraction f){
    if (num*f.den > f.num*den) {
      return 1;
    }
    else if (num*f.den < f.num*den) {
      return -1;
    }
    else {
      return 0;
    }
  }

  public static void main(String[] args) {
    Fraction f1 = new Fraction(6,5);

    System.out.println(f1.add(1));
    System.out.println(f1.floatValue());

    Fraction f2 = new Fraction(2,3);
    Fraction f3 = new Fraction(1,4);
    ArrayList<Fraction> myFracs = new ArrayList<Fraction>();
    myFracs.add(f1);
    myFracs.add(f2);
    myFracs.add(f3);
    Collections.sort(myFracs);

    for(Fraction f : myFracs) {
        System.out.println(f);
    }
  }

}
