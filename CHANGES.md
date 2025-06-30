# MCP Log Analyzer 修改说明

## 版本 0.1.1 (2025-06-26)
✅ **已发布到PyPI**

### 发布状态
- 包名: `mcp-log-analyzer`
- 版本: 0.1.1
- PyPI链接: https://pypi.org/project/mcp-log-analyzer/
- 安装命令: `pip install mcp-log-analyzer==0.1.1`

## 主要修改内容

### 1. 文件路径参数化
- **目标**: 将 `file_path` 修改为大模型调用时传入的参数
- **实现**: 每个MCP工具函数都接受 `file_path` 作为必需参数

### 2. 文件路径验证功能
- 添加了 `_validate_file_path()` 函数来验证传入的文件路径
- 支持相对路径自动转换为绝对路径
- 检查文件是否存在
- 验证路径是否为文件（而非目录）

### 3. 修改的文件

#### `mcp_server.py` (根目录)
- 添加了 `os` 模块导入
- 添加了 `_validate_file_path()` 验证函数
- 更新了所有工具函数的文档字符串，明确标注 `file_path` 为大模型调用时传入的参数
- 在每个工具函数中添加了路径验证调用

#### `src/mcp_log_analyzer/mcp_server.py`
- 与根目录文件保持一致的修改
- 使用相对导入 `from .log_parser import LogParser, LogEntry`

#### `src/mcp_log_analyzer/cli.py`
- 简化了命令行入口点，直接启动MCP服务器
- 移除了不必要的命令行参数解析
- MCP服务器通过stdio与客户端通信

#### `pyproject.toml`
- 添加了 `mcp-log-analyzer` 脚本入口点
- 保持了原有的 `mcp_log_analyze` 入口点

### 4. 工具函数列表
所有工具函数都已更新为接受 `file_path` 参数：

1. **`get_file_info(file_path: str)`** - 获取日志文件信息
2. **`read_log_lines(file_path: str, start_line: int = 0, count: int = None)`** - 读取指定范围的日志行
3. **`search_logs(file_path: str, keyword: str, max_results: int = 100)`** - 搜索包含关键词的日志条目
4. **`analyze_attack_types(file_path: str)`** - 分析攻击类型统计
5. **`analyze_ip_stats(file_path: str, top_n: int = 10)`** - 分析IP访问统计

### 5. 使用方式

#### 大模型调用示例
```json
{
  "tool": "get_file_info",
  "arguments": {
    "file_path": "/path/to/logfile.log"
  }
}
```

```json
{
  "tool": "search_logs",
  "arguments": {
    "file_path": "/path/to/logfile.log",
    "keyword": "GET",
    "max_results": 10
  }
}
```

#### 启动MCP服务器
```bash
# 方式1
mcp-log-analyzer

# 方式2
mcp_log_analyze

# 方式3 (使用uvx)
uvx --from mcp-log-analyzer mcp-log-analyzer
```

### 6. 安全性改进
- 文件路径验证防止访问不存在的文件
- 路径规范化防止路径遍历