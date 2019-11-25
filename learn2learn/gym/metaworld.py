"""
Wrappers for Metaworld compatibility
Implements full MetaEnv interface
"""

from metaworld.benchmarks import ML1 as ML1_
from metaworld.benchmarks import ML10 as ML10_
from metaworld.benchmarks import ML45 as ML45_


class ML1(ML1_):
    def reset_task(self, task):
        self.set_task(task)


class ML10(ML10_):
    def reset_task(self, task):
        self.set_task(task)


class ML45(ML45_):
    def reset_task(self, task):
        self.set_task(task)
