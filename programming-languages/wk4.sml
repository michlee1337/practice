(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let
	val r = g f1 f2
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end


fun only_capitals (sl) =
    List.filter (fn s => Char.isUpper(String.sub(s,0))) sl

fun longest_string1 (sl) =
    List.foldl (fn (a,b) => if String.size(a) > String.size(b) then a else b) "" sl

fun longest_string2 (sl) =
    List.foldl (fn (a,b) => if String.size(a) >= String.size(b) then a else b) "" sl

fun longest_string_helper (sl, f) =
    List.foldl (fn (a,b) => if f(String.size(a),String.size(b)) then a else b) "" sl

fun longest_string3 (sl) =
    longest_string_helper(sl,fn (x,y) => x > y)

fun longest_string4 (sl) =
    longest_string_helper(sl,fn (x,y) => x >= y)

fun longest_capitalized (sl) =
    longest_string_helper(sl, fn(x,y) => x>y)


(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here **\
**)
