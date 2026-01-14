voto = int( input("voto: ") )

giudizio = "n.a."

match voto:
    case 4:
        giudizio = "grav insuff"
    case 5:
        giudizio = "insuff"
    case 6:
        giudizio = "suff"

print (giudizio)