from mrjob.job import MRJob

class EsameTesto(MRJob):
    def mapper(self, _, linea):
        yield 'chars', len(linea)
        yield 'words', len(linea.split(' '))
        yield 'rows', 1
    
    def reducer(self, key, val):
        yield key, sum(val)

if __name__ == '__main__':
    EsameTesto.run()
        