# xml
'''
<azienda>
    <reparti>
        <reparto id="12">
            <impiegato matricola="123" sesso='M'>Mario Rossi</impiegato>
            <impiegato matricola="124" sesso='M'>Luigi Bianchi</impiegato>
            <impiegato matricola="125" sesso='F'>Anna Verdi</impiegato>
        </reparto>
    </reparti>
    <indirizzi>
        <indirizzo tipo="sede legale">Via carducci, 12</indirizzo>
    </indirizzi>
</azienda>
'''

from xml.dom import minidom
azienda = minidom.parse('azienda.xml')

imp = azienda.getElementsByTagName('impiegato')
print(imp[0].attributes['matricola'].value)
print(imp[0].firstChild.data)

