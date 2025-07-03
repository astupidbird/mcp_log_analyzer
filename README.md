
# MCP Log Analyzer

创宇盾云防御平台日志分析MCP服务器用于AI大模型调用分析被防护网站的日志文件。

## MCP工具

该MCP服务器提供以下工具调用：

1. **get_file_info** - 获取日志文件信息
2. **read_log_lines** - 读取指定范围的日志行
3. **search_logs** - 搜索包含关键词的日志条目
4. **analyze_attack_types** - 分析攻击类型统计
5. **analyze_ip_stats** - 分析IP访问统计

## 支持的 MCP 客户端
🔧 完全兼容领先的 MCP 环境：
- 爱派 Aipy
- Claude Desktop
- Cursor
- Windsurf
- Cline
- Continue
- Zed
- Cherry Studio
- Chatbox

## 如何使用

### 环境准备

你需要安装Python 3.10 或更高版本的 Python 环境

### 安装

#### 使用 pip

````
pip install mcp-log-analyzer
````
安装后，您可以使用以下命令将其作为脚本运行

````
python -m mcp_log_analyzer.cli
````

#### 使用 uv

uv 是一个用 Rust 编写的快速 Python 软件包安装程序和解析器。它是 pip 的现代替代品，性能显著提升。

##### 安装 uv

```
# Install uv using curl (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using PowerShell (Windows)
irm https://astral.sh/uv/install.ps1 | iex

# Or using Homebrew (macOS)
brew install uv
```

#### 安装 mcp-log-analyzer

使用 uv 安装 mcp-log-analyzer：

```
uv pip install mcp-log-analyzer
```

## 配置使用
### Cherry Studio 配置
1. 打开 Cherry Studio，选择“设置”。
2. 在左侧导航栏中，选择“MCP 服务器”。
3. 点击 “添加服务器” 选择 “从 JSON”导入
4. 粘贴下面配置后确定
````
{
  "mcpServers": {
    "日志分析": {
      "command": "python3",
      "args": [
        "-m",
        "mcp_log_analyzer.cli"
      ]
    }
  }
}
````
![CherryStudio](./cherrystudio.png)
5. 在 MCP 服务器配置中启用 “日志分析” MCP服务器即可使用


### Trae 配置
1. 打开 Trae，选择“设置”。
2. 在右侧导航栏中，选择“MCP”。
3. 点击 “添加” 选择 “手动添加”
4. 粘贴下面配置后确定
````
{
  "mcpServers": {
    "日志分析": {
      "command": "python3",
      "args": [
        "-m",
        "mcp_log_analyzer.cli"
      ]
    }
  }
}
````
![Trae](./trae.png)

5. 在 Trae 中使用 “Builder with MCP” 即可使用


## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

