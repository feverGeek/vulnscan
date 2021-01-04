import os

from lib.core import data
from lib.core.data import vulnscan_paths, running_config, vulnscan_config 
from lib.core.common import makeurl
from lib.core.datatype import AttribDict
from lib.utils.configfile import checkFile

def init_project_path():
    # 初始化项目路径
    root_path = os.getcwd()
    vulnscan_paths.vulnscan_root_path = root_path
    vulnscan_paths.vulnscan_lib_path = os.path.join(root_path, 'lib') # root_path + '/lib',
    vulnscan_paths.vulnscan_lib_core_path = os.path.join(root_path, 'lib', 'core') # root_path + '/lib/core'
    vulnscan_paths.vulnscan_lib_utils_path = os.path.join(root_path, 'lib', 'utils') # root_path + '/lib/utils'
    vulnscan_paths.vulnscan_plugins_path = os.path.join(root_path, 'plugins') # root_path + '/plugins'
    vulnscan_paths.vulnscan_results_path = os.path.join(root_path, 'results') # root_path + '/results'

def set_running_options(args):

    running_config.multiurl = False
    running_config.urls = []
    running_config.custom_plugin = False
    running_config.plugins = []

    # 指定单个url
    if args.url:
        running_config.urls.append(makeurl(args.url))

    # 指定批量导入url
    if args.file:
        running_config.multiurl = True
        checkFile(args.file)
        with open(args.file, 'r') as fd:
            contents = fd.readlines()
            for _ in contents:
                running_config.urls.append(makeurl(_.strip()))
        print(running_config.urls)

    # 查找插件
    if args.search:
        search_plugin(args.search)

    # 注册用户指定插件
    if args.plugins:
        # print(args.plugins)
        search_plugin(args.plugins)
        running_config.custom_plugin = True
        register_plugins(args.plugins)
    elif args.graphic:
        running_config.custom_plugin = True
    else:
        plugins = os.listdir(vulnscan_paths['vulnscan_plugins_path'])
        try:
            plugins.remove('__init__.py')
            plugins.remove('__pycache__')
        except:
            pass
        register_plugins(plugins)
        # print(running_config.plugins)

    # 自定义线程数
    running_config.threads = vulnscan_config.threads
    if running_config.threads is None:
        running_config.threads = 10
    running_config.threads = int(running_config.threads)

    # 自定义超时时间
    running_config.timeout = vulnscan_config.TimeOut
    if running_config.timeout is None:
        running_config.timeout = 10
    running_config.timeout = int(running_config.timeout)

def init_all_plugins():
    data.all_plugins = os.listdir(vulnscan_paths['vulnscan_plugins_path'])
    try:
        data.all_plugins.remove('__init__.py')
        data.all_plugins.remove('__pycache__')
    except:
        pass

    # print('all_plugins')
    # print(data.all_plugins)

def search_plugin(custom_plugins):
    plugins_path = vulnscan_paths['vulnscan_plugins_path']
    plugins = os.listdir(plugins_path)

    # for p in plugins:
    #     print(p)

    for _ in custom_plugins:
        try:
            plugins.index(_)
            print(f"插件{_}存在")
        except ValueError:
            print(f"插件{_}不存在")


def register_plugins(plugins):
    running_config.plugins = plugins
