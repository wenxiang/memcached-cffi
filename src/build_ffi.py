from cffi import FFI

ffi = FFI()

ffi.cdef(open("src/_memcached.h", "r").read())

ffi.set_source("memcached_cffi._memcached", open("src/_memcached.c", "r").read(),
    libraries=["memcached"])

if __name__ == "__main__":
    ffi.compile(verbose=True)
