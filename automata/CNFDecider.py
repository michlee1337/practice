def decideCNF(G):
    '''
    Assuming each grammar is a list of 2-tuples [V,P]
    where V is the variable and P is the production.

    Examples:
    decideCNF([('A','BC')]))
    >> True

    decideCNF([('A','')])
    >> True

    decideCNF([('A','a')])
    >> True

    decideCNF([('A','BC'),('B','g'),('C','h')])
    >> True

    decideCNF([('A','BC'),('B','g'),('C','h'),('C','hG')])
    >> False

    '''
    for R in G:
        eps = R[1] == ''
        term = len(R[1]) == 1 and R[1].islower()
        var = len(R[1]) == 2 and R[1].isupper()
        if not eps and not term and not var:
            return(False)
    return(True)

if __name__ == "__main__":
    print(decideCNF([('A','BC')]))
    print(decideCNF([('A','')]))
    print(decideCNF([('A','a')]))
    print(decideCNF([('A','BC'),('B','g'),('C','h')]))
    print(decideCNF([('A','BC'),('B','g'),('C','h'),('C','hG')]))
