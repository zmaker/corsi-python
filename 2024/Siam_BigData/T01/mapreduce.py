#https://mrjob.readthedocs.io/en/latest/index.html
from mrjob.job import MRJob

class Somma(MRJob):
    def mapper(self, _, numero):
        n = int(numero)
        if (n%2):
            yield 'DISPARI', n
        else:
            yield 'PARI', n
    
    def reducer(self, key, val):
        yield key, sum(val)
        
if __name__ == '__main__':
    Somma.run()