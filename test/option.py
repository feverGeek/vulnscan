from lib.core.data import *


def set_running_options(args):
    # print(args)
    # Namespace(banner=False, file=None, plugin=None, search=None, url=None)

    # 指定批量导入url
    if args.file:
        running_config.multiurl = True
    
    if args.search:
        search_plugin(args)


def search_plugin(args):
    plugins_path = '/home/zeta/Test/vulnscan/test/plugins'
    plugins = os.listdir(plugins_path)
    print(plugins)
    print(dir(plugins))
    print(plugins.index('thinkphp'))
    print(plugins.index('hahahhah'))

if __name__ == '__main__':
    search_plugin('1')
