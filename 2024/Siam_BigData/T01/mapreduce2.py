from mrjob.job import MRJob

class EsameTesto(MRJob):
    def mapper(self, _, linea):
        yield "caratteri", len(linea)
        yield "parole", len(linea.split())
        yield "linee", 1
    
    def reducer(self, key, val):
        yield key, sum(val)
        
if __name__ == '__main__':
    EsameTesto.run()
