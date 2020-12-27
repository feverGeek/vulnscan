"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import os
from lib.core.datatype import AttribDict

# vulnscan 文件路径
# 绝对路径,运行时获取
paths          = AttribDict()
cwd            = os.getcwd()                   # 当前路径
parent_path    = os.path.dirname(cwd)          # 父目录
root_path      = os.path.dirname(parent_path)  # 项目根目录
vulnscan_paths = {
    "vulnscan_root_path":      root_path,
    "vulnscan_lib_path":       root_path + '/lib',
    "vulnscan_lib_core_path":  root_path + '/lib/core',
    "vulnscan_lib_utils_path": root_path + '/lib/utils',
    "vulnscan_plugins_path":   root_path + '/plugins'
}

# w9scan cmder
#cmdLineOptions = AttribDict()

# vulnscan 配置文件选项
vulnscan_config = AttribDict()

# vulnscan 运行时参数
running_config = AttribDict()


# w9scan plugins pycode hash
#w9_hash_pycode = dict()
