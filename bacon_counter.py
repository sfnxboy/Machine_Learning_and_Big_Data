from mrjob.job import MRJob
class bacon_counter(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == "__main__":
   bacon_counter.run()

# run the line below in a python terminal. Make sure you are in the correct directory
# python bacon_counter.py input.txt