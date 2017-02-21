#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from ProjectFileBuilder.ProjectFileBuilder import ProjectFileBuilder
from ProjectFileBuilder import ProjectFileBuilder
from ProjectFileBuilder import ImportType
from ProjectFileBuilder import ProjectFileType

class ImplementationFileBuilder(ProjectFileBuilder):
    def __init__(self, fileName, baseClassName):
        ProjectFileBuilder.__init__(self, fileName, baseClassName)
        self.importFramework = importFramework

    # 生成 .m 文件内容
    def generatesImplementationContents(self):
        interfaceFileContent = '''
@interface %s : %s

@end
        ''' % (self.fileName, self.baseClassName)
        self.fileContent += interfaceFileContent

    def buildFile(self):
        self.generatesCommentContents()
        self.generatesImportContents(ImportType.Framework, self.importFramework)
        self.generatesImplementationContents()
        self.makeFile(ProjectFileType.Interface)

if __name__ == '__main__':
    implementationFileBuilder = ImplementationFileBuilder("DemoViewController", "UIViewController")
    implementationFileBuilder.buildFile()
