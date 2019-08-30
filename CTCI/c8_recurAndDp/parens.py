def parens(n_parens):
    # base case: parens is 1
    if n_parens == 1:
        return(["()"])
    # recursive step: put paren around, before, or after all possible subcombis
    else:
        parens_w = []
        parens_wo = parens(n_parens-1)
        for sub_p in parens_wo:
            parens_w.append("(" + sub_p + ")")
            parens_w.append("()" + sub_p)
            parens_w.append(sub_p + "()")
        # discard last combi as it will be duplicate (after and before non nested case is the same)
        parens_w = parens_w[:-1]
        return(parens_w)
if __name__ == "__main__":
    num = int(input("num parens: "))
    print(parens(num))
