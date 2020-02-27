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


val only_capitals =
    List.filter (fn s => Char.isUpper(String.sub(s,0)))

val longest_string1 =
    foldl (fn (a,b) => if size(a) > size(b) then a else b) ""

val longest_string2 =
    foldl (fn (a,b) => if size(a) >= size(b) then a else b) ""

fun longest_string_helper (sl, f) =
    foldl (fn (a,b) => if f(size(a),size(b)) then a else b) "" sl

fun longest_string3 (sl) =
    longest_string_helper(sl,fn (x,y) => x > y)

fun longest_string4 (sl) =
    longest_string_helper(sl,fn (x,y) => x >= y)

val longest_capitalized =
    longest_string1 o only_capitals

val rev_string =
    implode o rev o explode

fun first_answer f x =
    case x of
	[] => raise NoAnswer
      | hd::tl => case f hd of
		      SOME ans => ans
		    | NONE => first_answer f tl

fun all_answers f x =
    let
	fun helper acc rem =
	    case rem of
		[] => SOME acc
	      | hd::tl => case f hd of
			      NONE => NONE
			    | SOME res => helper(acc@res) tl
    in
	helper [] x
    end
	
fun count_wildcards ls =
    g (fn () => 1) (fn x=> 0) ls

fun count_wild_and_variable_lengths ls =
    g (fn () => 1) size ls

fun count_some_var (str, ls) =
    g (fn() => 0) (fn x => if x=str then 1 else 0) ls

fun check_pat p =
    let
	fun get_vstr (rem, acc) =
	    case rem of
		Variable x => x::acc
	      | TupleP ps => foldl (fn (p,p_acc) => (get_vstr (p, acc) @ p_acc)) [] ps
	      |  ConstructorP(_,p) => get_vstr(p, acc) 
	      | _ => acc
 
	fun check_distinct ls =
	    case ls of
		[] => true
	      | hd::tl => (not(List.exists(fn x => x=hd) tl)) andalso check_distinct(tl)
    in
	check_distinct(get_vstr(p,[]))
    end

fun match (v,p) =
    case (v,p) of
	(var, Variable pat) => SOME[(pat,var)]
      | (Unit, UnitP) => SOME []
      | (Const x, ConstP y) => if x=y then SOME[] else NONE
      | (Tuple var, TupleP pat) => if length var = length pat
				   then all_answers match(ListPair.zip(var,pat)) (* pass the tuple into match*)
				   else NONE
      | (Constructor(_,var),ConstructorP(_,pat)) => match(var, pat)
      | (_, Wildcard) => SOME []
      | _ => NONE

fun first_match v pls =
    SOME (first_answer(fn p => match(v,p)) pls)
    handle NoAnswer => NONE
			   
(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here **\
**)
