import time
import subprocess

from .benchmarks import Benchmarks


class Import(Benchmarks):

    def __init__(self, comm, params):
        super(Import, self).__init__(name='import', comm=comm, params=params)

    def run(self):

        t0 = time.time()
        subprocess.call(['python', '-c', 'import numpy'])
        t1 = time.time()

        return t1 - t0



