from nanoclock_impl cimport clock_impl

MICROSECOND = 1000
MILLISECOND = 1000000
SECOND =      1000000000

def nanoclock():
    return clock_impl()

