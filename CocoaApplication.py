import ctypes

libpath = "/Users/parhamoyan/Desktop/My_Framework/Mango/cmake-build-debug/libMango.dylib"
lib = ctypes.CDLL(libpath)


class CocoaApplication(object):
    def __init__(self):
        lib.CocoaApplication_create.argtypes = []
        lib.CocoaApplication_create.restype = ctypes.c_void_p

        lib.CocoaApplication_run.argtypes = [ctypes.c_void_p]
        lib.CocoaApplication_run.restype = ctypes.c_void_p

        self.obj = lib.CocoaApplication_create()

    def run(self) -> None:
        lib.CocoaApplication_run(self.obj)
