cdef extern from "nanoclock_impl.h":
    ctypedef unsigned long long uint64_t
    uint64_t clock_impl()
