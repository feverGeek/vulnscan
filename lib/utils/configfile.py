import os
import configparser

from lib.core.exceptions import ToolkitSystemException
from lib.core.enums import OPTION_TYPE
from lib.core.data import vulnscan_config

conf = None

optDict = {
    "Config": {
        "threads":     "integer",
        "TimeOut":     "integer",
        "UserAgent":   "string",
        "Cookie":      "string",
        "headers":     "string"
    }
}


def configFileProxy(section, option, datatype):
    """
    Parse configuration file and save settings into the configuration
    advanced dictionary.
    """

    global conf

    if conf.has_option(section, option):
        try:
            if datatype == OPTION_TYPE.BOOLEAN:
                value = conf.getboolean(section, option) if conf.get(
                    section, option) else False
            elif datatype == OPTION_TYPE.INTEGER:
                value = conf.getint(section, option) if conf.get(
                    section, option) else 0
            elif datatype == OPTION_TYPE.FLOAT:
                value = conf.getfloat(section, option) if conf.get(
                    section, option) else 0.0
            else:
                value = conf.get(section, option)
        except ValueError as ex:
            errMsg = "error occurred while processing the option "
            errMsg += "'%s' in provided configuration file ('%s')" % (
                option, ex)
            raise ToolkitSystemException(errMsg)

        if value:
            vulnscan_config[option] = value
        else:
            vulnscan_config[option] = None
    else:
        debugMsg = "missing requested option '%s' (section " % option
        debugMsg += "'%s') into the configuration file, " % section
        debugMsg += "ignoring. Skipping to next."
        print(debugMsg)


def checkFile(filename, raiseOnError=True):
    """
    Checks for file existence and readability
    """

    valid = True

    try:
        if filename is None or not os.path.isfile(filename):
            valid = False
    except UnicodeError:
        valid = False

    if valid:
        try:
            with open(filename, "rb"):
                pass
        except:
            valid = False

    if not valid and raiseOnError:
        raise ToolkitSystemException("unable to read file '%s'" % filename)

    return valid


def configFileParser(configFile):
    """
    Parse configuration file and save settings into the configuration
    advanced dictionary.
    """

    global conf

    # 检查文件
    checkFile(configFile)

    try:
        # 读取配置文件
        conf = configparser.ConfigParser()
        conf.read(configFile, encoding='utf-8')
    except Exception as ex:
        errMsg = "you have provided an invalid and/or unreadable configuration file ('%s')" % ex
        raise ToolkitSystemException(errMsg)

    if not conf.has_section("Config"):
        errMsg = "missing a mandatory section 'Config' in the configuration file"
        raise ToolkitSystemException(errMsg)

    mandatory = False

    # 检查是否缺少配置项
    for option in optDict['Config'].keys():
        if conf.has_option("Config", option):
            mandatory = True
            break

    if not mandatory:
        errMsg = "配置文件中缺少配置项"
        errMsg += "(threads, TimeOut, UserAgent, Cookie, headers)"
        raise ToolkitSystemException(errMsg)

    # 读取配置项
    for family, optionData in optDict.items():
        for option, datatype in optionData.items():
            # datatype = unArrayizeValue(datatype)
            # 将配置写入变量
            configFileProxy(family, option, datatype)


def modifyConfigFile(configFile, dict):
    # global conf

    checkFile(configFile)

    conf = configparser.ConfigParser()
    conf.read(configFile, encoding='utf-8')
    # print(conf.sections)
    # for s in conf.sections():
        # print(conf.items(s))

    parser = configparser.ConfigParser()
    parser.read_dict(dict)
    for section in parser.sections():
        for option in parser[section]:
            conf[section][option] = parser[section][option]

    # print(conf.sections)
    # for s in conf.sections():
        # print(conf.items(s))

    with open(configFile, 'w+') as f:
        conf.write(f)

    configFileParser(configFile)