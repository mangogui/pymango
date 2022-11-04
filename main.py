from pymango import CocoaApplication
from pymango import CocoaWindow

if __name__ == "__main__":

    application = CocoaApplication()

    window = CocoaWindow()
    window.center()
    window.display()

    application.run()
