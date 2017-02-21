#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from ProjectFileBuilder.ProjectFileBuilder import ProjectFileBuilder
from ProjectFileBuilder import ProjectFileBuilder
from ProjectFileBuilder import ImportType
from ProjectFileBuilder import ProjectFileType

class InterfaceFileBuilder(ProjectFileBuilder):
    def __init__(self, fileName, baseClassName, importFramework):
        ProjectFileBuilder.__init__(self, fileName, baseClassName)
        self.importFramework = importFramework
    # 生成注释内容
    def generatesInterfaceContents(self):
        interfaceFileContent = '''
@interface %s : %s

@end
        ''' % (self.fileName, self.baseClassName)
        self.fileContent += interfaceFileContent
        
    def buildFile(self):
        self.generatesCommentContents()
        self.generatesImportContents(ImportType.Framework, self.importFramework)
        self.generatesInterfaceContents()
        self.makeFile(ProjectFileType.Interface)

if __name__ == '__main__':
    interfaceFileBuilder = InterfaceFileBuilder("DemoViewController", "UIViewController", "UIKit")
    interfaceFileBuilder.buildFile()
