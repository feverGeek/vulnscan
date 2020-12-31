from lib.utils.log     import MY_LOGGER
from lib.core.datatype import AttribDict

logger = MY_LOGGER

# vulnscan 文件路径
# 绝对路径,运行时获取
vulnscan_paths = AttribDict()

# vulnscan 配置文件选项
vulnscan_config = AttribDict()

# vulnscan 运行时参数
running_config = AttribDict()

# 所有插件
all_plugins = []