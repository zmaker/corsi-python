from mrjob.job import MRJob

class MRSomma(MRJob):
    
    def mapper(self, _, numero):
        n = int(numero)
        if (n%2) == 0:
            yield 'PARI', n
        else:
            yield 'DISPARI', n
        
    def reducer(self, chiave, valore):
        yield chiave, sum(valore)
    
if __name__ == '__main__':
    MRSomma.run()