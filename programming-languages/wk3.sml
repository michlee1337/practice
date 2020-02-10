(* Dan Grossman, Coursera PL, HW2 Provided Code *)

fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* Problem 1 *)
fun all_except_option(option: string, all: string list) =
    case all of
	[] => NONE
      | hd::tl => if same_string(option, hd)
		  then SOME tl
		  else case all_except_option(option,tl) of
			   NONE => NONE
			 | SOME res => SOME(hd::res)

fun get_substitutions1(substitutions: string list list, option: string) =
    case substitutions of
	[] => []
      | hd::tl  => case all_except_option(option,hd) of
		      NONE => get_substitutions1(tl, option)
		    | SOME res => res@get_substitutions1(tl, option)

fun get_substitutions2(subs: string list list, option: string) =
    let fun helper(subs, acc: string list) =
	    case subs of
		[] => acc
		| hd::tl  => case all_except_option(option,hd) of
				 NONE => helper(tl, acc)
			       | SOME res => helper(tl, acc@res)
    in
	helper(subs, [])
    end

fun similar_names(subs: string list list, name: {first: string, middle: string, last: string}) =
    let
	val {first=f, middle=m, last=l} = name
	val fs = get_substitutions2(subs,f)
	fun helper(name_subs, acc) =
	    case name_subs of
		[] => acc
	      | hd::tl => helper(tl,acc@[{first=hd,middle=m,last=l}])
    in
	helper(fs,[name])
    end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw

exception IllegalMove

(* Problem 2 *)
fun card_color(suit, _) =
    case suit of
	Clubs => Black
      | Spades => Black
      | _ => Red

fun card_value(_, rank) =
    case rank of
	Ace => 11
      | Num x => x
      | _  => 10

fun remove_card(cs, c, e) =
    case cs of
	[] => raise e
      | hd::tl => if hd = c
		  then tl
		  else hd::remove_card(tl,c,e)

fun all_same_color(cs) =
    case cs of
	[] => true
      | hd::[] => true
      | hd::tl1::tl2 => card_color(hd) = card_color(tl1) andalso all_same_color(tl1::tl2)

fun sum_cards(cs) =
    let
	fun helper(cs,acc) =
	    case cs of
		[] => acc
	      | hd::tl => helper(tl,acc+card_value(hd))
    in
	helper(cs,0)
    end

fun score(cs, goal) =
    let
	val held = sum_cards(cs)
	val ps = if held < goal
		 then goal - held
		 else (held-goal)*3
    in
	if all_same_color(cs)
	then ps div 2
	else ps
    end

(* written seperately to make officiate_challange neater *)
fun officiate_helper(hs,cs,ms,g) =
    case ms of
	[] => hs
      | (Discard c)::mtl => officiate_helper(remove_card(hs,c,IllegalMove),cs,ms,g)
      | (Draw)::mtl => case cs of
			   [] => hs
			 | chd::ctl => if sum_cards(chd::hs) > g
				       then chd::hs
				       else officiate_helper(chd::hs,ctl,mtl,g)

fun officiate(cards,moves,goal) =
    score(officiate_helper([],cards,moves,goal),goal)

(* Challenge *)

(* Returns first Ace card if hand contains one, else NONE *)
fun hasAce(cs) =
    case cs of
	[] => NONE
      | (rank, Ace)::_ => SOME (rank, Ace)
      | _::tl => hasAce(tl)

fun score_challenge(cs, goal) =
    let
	val old = score(cs,goal)
    in
	case hasAce(cs) of
	    NONE => old
	  | SOME (suit,rank) =>
	    let
		(* Get a new score subbing an Ace w a 1 *)
		val new = score_challenge((suit,Num 1)::remove_card(cs,(suit,rank),IllegalMove),goal)
	    in
		(* Return best score *)
		if new < old
		then new
		else old
	    end
    end

fun officiate_challenge(cards,moves,goal) =
    score_challenge(officiate_helper([],cards,moves,goal),goal)
