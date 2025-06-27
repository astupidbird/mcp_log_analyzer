"""
MCP Log Analyzer - MCP服务器用于读取和解析日志文件
"""

__version__ = "0.1.0"
__author__ = "Log Analyzer Team"

from .log_parser import LogParser, LogEntry

# 避免循环导入，延迟导入mcp服务器
def get_mcp_server():
    """获取MCP服务器实例"""
    from .mcp_server import mcp
    return mcp

__all__ = ["LogParser", "LogEntry", "get_mcp_server"]