import sys

fileName = ""
HeaderFileContent = ""
ImplementationFileContent = ""

def addHeaderInterface():
    interfaceContent = '''
        #import <UIKit/UIKit.h>

        @interface %s : UIViewController

        @end
    ''' % (fileName)
    global HeaderFileContent
    HeaderFileContent += interfaceContent

def createViewControllerFile():
    addHeaderAnnotate()
    addHeaderInterface()
    print(HeaderFileContent)

if __name__ == '__main__':
    if sys.argv[1] == "vc":
        fileName = sys.argv[2]
        createViewControllerFile()
