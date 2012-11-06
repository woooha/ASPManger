#!/usr/bin/env python
class BaseInstaller:
"""抽象出服务的安装动作，使用 Installer 来完成一项服务的安装行为"""
    def install(self):
        """用来安装一项服务"""
        return

    def uninstall(self):
        """用以删除一项服务"""
        return

class DownloadInstaller(BaseInstaller):
"""下载安装器，此类安装器直接从远程地址复制一份程序到本地，以实现安装"""
    source = None
    dest = None
    def __init___(self, source, dest):
        self.source = source
        self.dest = dest 
        
    def install(self):
        

    def uninstall(self):
        

class CompileInstaller(BaseInstaller):
"""编译安装器，此类安装器通过编译源代码进行安装"""

class BinaryInstaller(BaseInstaller):
"""通过二进制安装包进行安装的安装器"""
