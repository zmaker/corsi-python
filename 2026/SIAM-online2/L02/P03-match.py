voto = int( input("voto (0-10)? ") )

giudizio = "n.a."

match voto:
    case 4:
        giudizio = "grav. insuff."
    case 5:
        giudizio = "insuff"
    case 6:
        giudizio = "suff"
    case 7:
        giudizio = "discreto"
    case _:
        giudizio = "?"
    
print(giudizio)