# 安装指南

## 项目概述

MCP Log Analyzer 是一个使用 uv 打包的 Python 项目，提供了一个命令行工具 `mcp_log_analyze` 用于启动 MCP 服务器来分析日志文件。

## 项目结构

```
mcp-log-analyzer/
├── src/
│   └── mcp_log_analyzer/           # 主要源代码包
│       ├── __init__.py             # 包初始化文件
│       ├── cli.py                  # 命令行入口点
│       ├── log_parser.py           # 日志解析器
│       └── mcp_server.py           # MCP服务器实现
├── tests/                          # 测试文件
│   ├── __init__.py
│   └── test_log_parser.py
├── dist/                           # 构建的包文件
│   ├── mcp_log_analyzer-0.1.0-py3-none-any.whl
│   └── mcp_log_analyzer-0.1.0.tar.gz
├── pyproject.toml                  # 项目配置文件
├── README.md                       # 项目说明
├── build.py                        # 构建脚本
└── .gitignore                      # Git忽略文件
```

## 安装方法

### 方法1: 使用 uv（推荐）

```bash
# 1. 安装 uv
pip install uv

# 2. 从源码安装（开发模式）
uv pip install -e .

# 3. 或者从构建的包安装
uv pip install dist/mcp_log_analyzer-0.1.0-py3-none-any.whl
```

### 方法2: 使用 pip

```bash
# 从源码安装
pip install -e .

# 或者从构建的包安装
pip install dist/mcp_log_analyzer-0.1.0-py3-none-any.whl
```

## 使用方法

### 命令行工具

安装完成后，可以直接使用 `mcp_log_analyze` 命令：

```bash
# 启动 MCP 服务器
mcp_log_analyze

# 查看帮助信息
mcp_log_analyze --help

# 查看版本信息
mcp_log_analyze --version

# 指定主机和端口
mcp_log_analyze --host 0.0.0.0 --port 8080
```

### 作为 Python 模块使用

```python
from mcp_log_analyzer import LogParser, mcp

# 创建日志解析器
parser = LogParser("path/to/logfile.log")

# 读取日志
entries = parser.read_lines(start_line=0, count=10)

# 启动 MCP 服务器
mcp.run()
```

## 开发和构建

### 开发环境设置

```bash
# 克隆项目
git clone <repository-url>
cd mcp-log-analyzer

# 安装开发依赖
uv pip install -e ".[dev]"

# 运行测试
pytest tests/ -v
```

### 构建包

```bash
# 使用 uv 构建
uv build

# 或者使用构建脚本
python build.py
```

### 测试安装

```bash
# 运行测试
python -m pytest tests/ -v

# 测试命令行工具
mcp_log_analyze --version
mcp_log_analyze --help
```

## 验证安装

安装完成后，可以通过以下步骤验证：

1. **检查命令行工具**：
   ```bash
   mcp_log_analyze --version
   # 应该输出: mcp-log-analyzer 0.1.0
   ```

2. **运行测试**：
   ```bash
   python -m pytest tests/ -v
   # 所有测试应该通过
   ```

3. **检查包导入**：
   ```python
   from mcp_log_analyzer import LogParser, LogEntry, mcp
   print("导入成功！")
   ```

## 故障排除

### 常见问题

1. **命令未找到**：
   - 确保安装成功：`pip list | grep mcp-log-analyzer`
   - 检查 PATH 环境变量

2. **导入错误**：
   - 确保使用正确的 Python 环境
   - 重新安装：`pip uninstall mcp-log-analyzer && pip install -e .`

3. **依赖问题**：
   - 更新 pip：`pip install --upgrade pip`
   - 安装依赖：`pip install fastmcp>=0.1.0`

## 卸载

```bash
pip uninstall mcp-log-analyzer
```

## 支持

如有问题，请查看：
- README.md 文件
- 项目文档
- 提交 Issue