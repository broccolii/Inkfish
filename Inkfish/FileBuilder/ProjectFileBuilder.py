#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum

ImportType = Enum('ImportType', ('Framework', 'File'))
ProjectFileType = Enum('ProjectFileTyep', ('Interface', 'Implementation'))

import getpass
import time

COMPANY_NAME = "Youzan"

# 工程文件生成的基类
class ProjectFileBuilder:

    def __init__(self, fileName, baseClassName):
        self.fileName = fileName
        self.baseClassName = baseClassName
        self.fileContent = ""

    # 生成注释内容
    def generatesCommentContents(self):
        createDate = time.strftime("%d/%m/%Y", time.localtime())
        createYear = time.strftime("%Y", time.localtime())
        userName = getpass.getuser()

        commentContents = '''
//
//  %s
//
//  Created by %s on %s.
//  Copyright © %s %s. All rights reserved.
//
        ''' % (self.fileName, userName, createDate, createYear, COMPANY_NAME)
        self.fileContent += commentContents

    # 生成引用 frameworkName 是可选参数 当 importType 是 Framework 的时候才需要
    def generatesImportContents(self, importType, frameworkName = ""):
        if importType == ImportType.Framework:
            importContents = '''
#import <%s/%s.h>
            ''' % (frameworkName, frameworkName)
        else:
            importContents = '''
#import "%s.h"
            ''' %(self.fileName)

        self.fileContent += importContents

    # 生成文件
    def makeFile(self, projectFileType):

        if projectFileType == ProjectFileType.Interface:
            makeFileName = '%s.h' %(self.fileName)
        else:
            makeFileName = '%s.m' %(self.fileName)

        f = open('%s' %(makeFileName),'w')
        f.write(self.fileContent)
        f.close()

if __name__ == '__main__':
    projectFileBuilder = ProjectFileBuilder("DemoViewController", "ViewController")
    projectFileBuilder.generatesCommentContents()
    projectFileBuilder.generatesImportContents(ImportType.File)

    print(projectFileBuilder.fileContent)
    projectFileBuilder.makeFile(ProjectFileType.Implementation)
