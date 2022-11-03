import ctypes
from  ctypes import c_void_p, c_char_p

libpath = "/Users/parhamoyan/Desktop/My_Framework/Mango/cmake-build-debug/libMango.dylib"
lib = ctypes.CDLL(libpath)


class CocoaWindow(object):
    def __init__(self):
        lib.CocoaWindow_create.argtypes = []
        lib.CocoaWindow_create.restype = c_void_p

        lib.CocoaWindow_center.argtypes = [c_void_p]
        lib.CocoaWindow_center.restype = c_void_p

        lib.CocoaWindow_display.argtypes = [c_void_p]
        lib.CocoaWindow_display.restype = c_void_p

        lib.CocoaWindow_windowTitle.argtypes = [c_void_p]
        lib.CocoaWindow_windowTitle.restype = c_char_p

        lib.CocoaWindow_setWindowTitle.argtypes = [c_void_p, c_char_p]
        lib.CocoaWindow_setWindowTitle.restype = c_void_p

        self.obj = lib.CocoaWindow_create()

    def center(self) -> None:
        return lib.CocoaWindow_center(self.obj)

    def display(self) -> None:
        return lib.CocoaWindow_display(self.obj)

    def windowTitle(self) -> str:
        return lib.CocoaWindow_windowTitle(self.obj)

    def setWindowTitle(self, title: str) -> None:
        return lib.CocoaWindow_setWindowTitle(self.obj, bytes(title))
