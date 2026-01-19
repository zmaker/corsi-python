from mrjob.job import MRJob

class Somma(MRJob):
    def mapper(self, _, riga):
        n = int(riga)
        if (n%2):
            #dispari
            yield 'D', n
        else:
            #pari
            yield 'P', n
        
    
    def reducer(self, key, val):
        yield key, sum(val)
    
if __name__ == '__main__':
    Somma.run()