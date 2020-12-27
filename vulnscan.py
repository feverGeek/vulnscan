#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import traceback

from lib.core.common import banner, systemQuit
from lib.core.enums import EXIT_STATUS
from lib.core.option import set_running_options, init_project_path
from lib.core.start import start_scan
from lib.core.exceptions import ToolkitMissingPrivileges, ToolkitSystemException, ToolkitUserQuitException
from lib.core.data import logger

from lib.utils.configfile import configFileParser

from lib.ui.vulnscan_ui import Ui_Form
from lib.ui.vulnscan_mform import MForm

from PyQt5 import QtWidgets

def console_main():
    # 开始扫描
    start_scan()


def graphic_main():
    app = QtWidgets.QApplication(sys.argv)
    m = MForm()
    m.show()
    sys.exit(app.exec_())

def init_args():
    parser = argparse.ArgumentParser(description='vulnscan scanner')
    parser.add_argument(
        '--banner', help='output the banner', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', '--graphic', help='graphic mode', default=False, type=bool, required=False)
    group.add_argument('-u', '--url', help='url')
    group.add_argument('-f', '--file', help='load urls from a file')
    group.add_argument('-s', '--search', nargs='+',
                       help='find infomation of plugin')

    parser.add_argument('-p', '--plugins', nargs='+', help='plugins')
    parser.add_argument('-t', '--timeout', help='maximum timeout')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # 打印程序版本、banner信息
    banner()

    # 初始化命令参数
    args = init_args()

    try:
        # 读取配置文件
        configFileParser('./config.conf')

        # 设置运行时选项
        init_project_path()
        set_running_options(args)

        # 开始扫描
        # 默认使用console模式
        if not args.graphic:
            console_main()
        else:
            graphic_main()

    except ToolkitMissingPrivileges as e:
        logger.error(e)
        systemQuit(EXIT_STATUS.ERROR_EXIT)

    except ToolkitSystemException as e:
        logger.error(e)
        systemQuit(EXIT_STATUS.ERROR_EXIT)

    except ToolkitUserQuitException:
        systemQuit(EXIT_STATUS.USER_QUIT)

    except KeyboardInterrupt:
        print('\nCtrl+C Stop running\n')
        sys.exit(0)
        systemQuit(EXIT_STATUS.USER_QUIT)

    except Exception:
        print(traceback.format_exc())
        logger.warning('It seems like you reached a unhandled exception.')
    