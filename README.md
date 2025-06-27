
# MCP Log Analyzer

MCP服务器用于读取和解析日志文件。

## 功能特性

- 解析日志文件
- 提供MCP工具接口用于日志分析
- 支持日志搜索和统计分析
- 命令行工具支持

## 安装

### 使用uv安装（推荐）

```bash
# 安装uv（如果还没有安装）
pip install uv

# 从源码安装
uv pip install .

# 或者开发模式安装
uv pip install -e .
```

### 使用pip安装

```bash
pip install .
```

## 使用方法

### 命令行工具

安装后，可以直接使用 `mcp_log_analyze` 命令启动MCP服务器：

```bash
# 启动MCP服务器
mcp_log_analyze

# 查看帮助
mcp_log_analyze --help

# 指定主机和端口
mcp_log_analyze --host 0.0.0.0 --port 8080
```

### 作为Python模块使用

```python
from mcp_log_analyzer import LogParser, mcp

# 创建日志解析器
parser = LogParser("path/to/logfile.log")

# 读取日志行
entries = parser.read_lines(start_line=0, count=10)

# 搜索日志
results = parser.search_logs("keyword", max_results=100)

# 获取文件信息
info = parser.get_file_info()

# 启动MCP服务器
mcp.run()
```

## MCP工具

该服务器提供以下MCP工具：

1. **get_file_info** - 获取日志文件信息
2. **read_log_lines** - 读取指定范围的日志行
3. **search_logs** - 搜索包含关键词的日志条目
4. **analyze_attack_types** - 分析攻击类型统计
5. **analyze_ip_stats** - 分析IP访问统计

## 开发

### 设置开发环境

```bash
# 克隆仓库
git clone <repository-url>
cd mcp-log-analyzer

# 安装开发依赖
uv pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
black src/ tests/
isort src/ tests/

# 代码检查
flake8 src/ tests/
```

### 项目结构

```
mcp-log-analyzer/
├── src/
│   └── mcp_log_analyzer/
│       ├── __init__.py
│       ├── cli.py          # 命令行入口点
│       ├── log_parser.py   # 日志解析器
│       └── mcp_server.py   # MCP服务器
├── tests/
│   ├── __init__.py
│   └── test_log_parser.py
├── pyproject.toml          # 项目配置
└── README.md
```

## 日志格式

支持的日志格式示例：

```
2024-01-01 12:00:00 100ms SQL blocked 192.168.1.1 10.0.0.1 example.com /test GET - miss 200 1024 Mozilla/5.0
```

字段说明：
- 请求时间
- 请求持续时间
- 攻击类型
- 拦截状态
- 客户端IP
- 代理IP
- 域名
- URL路径
- 请求方法
- 引用页面
- 缓存状态
- 状态码
- 页面大小
- 用户代理

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

