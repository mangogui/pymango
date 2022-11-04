from ctypes import c_void_p, c_char_p

from .Lib import LibMango


class CocoaWindow(object):
    def __init__(self) -> None:
        LibMango.CocoaWindow_create.argtypes = []
        LibMango.CocoaWindow_create.restype = c_void_p

        LibMango.CocoaWindow_center.argtypes = [c_void_p]
        LibMango.CocoaWindow_center.restype = c_void_p

        LibMango.CocoaWindow_display.argtypes = [c_void_p]
        LibMango.CocoaWindow_display.restype = c_void_p

        LibMango.CocoaWindow_windowTitle.argtypes = [c_void_p]
        LibMango.CocoaWindow_windowTitle.restype = c_char_p

        LibMango.CocoaWindow_setWindowTitle.argtypes = [c_void_p, c_char_p]
        LibMango.CocoaWindow_setWindowTitle.restype = c_void_p

        LibMango.CocoaWindow_maximize.argtypes = [c_void_p]
        LibMango.CocoaWindow_maximize.restype = c_void_p

        LibMango.CocoaWindow_fullscreen.argtypes = [c_void_p]
        LibMango.CocoaWindow_fullscreen.restype = c_void_p

        self.obj = LibMango.CocoaWindow_create()

    def center(self) -> None:
        return LibMango.CocoaWindow_center(self.obj)

    def display(self) -> None:
        return LibMango.CocoaWindow_display(self.obj)

    def windowTitle(self) -> str:
        return LibMango.CocoaWindow_windowTitle(self.obj)

    def setWindowTitle(self, title: str) -> None:
        return LibMango.CocoaWindow_setWindowTitle(self.obj, title.encode('utf-8'))

    def maximize(self) -> None:
        return LibMango.CocoaWindow_maximize(self.obj)

    def fullscreen(self) -> None:
        return LibMango.CocoaWindow_fullscreen(self.obj)
