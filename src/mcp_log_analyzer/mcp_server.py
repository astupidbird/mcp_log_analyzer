#!/usr/bin/env python3
"""
MCP服务器用于读取和解析日志文件
大模型调用时需要传入file_path参数来指定要分析的日志文件
"""

import os
from typing import Dict, List
from fastmcp import FastMCP

# 使用绝对导入避免相对导入错误
try:
    from mcp_log_analyzer.log_parser import LogParser, LogEntry
except ImportError:
    # 如果作为脚本直接运行，尝试从当前目录导入
    from log_parser import LogParser, LogEntry

# 创建MCP服务器
mcp = FastMCP("Log Parser Server")

def _validate_file_path(file_path: str) -> str:
    """验证并规范化文件路径"""
    if not file_path:
        raise ValueError("文件路径不能为空")
    
    # 如果是相对路径，转换为绝对路径
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    
    # 检查是否为文件（不是目录）
    if not os.path.isfile(file_path):
        raise ValueError(f"路径不是文件: {file_path}")
    
    return file_path

def _convert_entry_to_dict(entry: LogEntry) -> Dict:
    """将LogEntry转换为字典格式"""
    return {
        "request_time": entry.request_time,
        "request_duration": entry.request_duration,
        "attack_type": entry.attack_type,
        "intercept_status": entry.intercept_status,
        "client_ip": entry.client_ip,
        "proxy_ip": entry.proxy_ip,
        "domain": entry.domain,
        "url": entry.url,
        "request_method": entry.request_method,
        "referer": entry.referer,
        "cache_status": entry.cache_status,
        "status_code": entry.status_code,
        "page_size": entry.page_size,
        "user_agent": entry.user_agent,
        "raw_line": entry.raw_line
    }

@mcp.tool()
def get_file_info(file_path: str) -> Dict:
    """获取日志文件信息
    
    Args:
        file_path: 日志文件路径（大模型调用时传入）
    """
    try:
        validated_path = _validate_file_path(file_path)
        parser = LogParser(validated_path)
        return parser.get_file_info()
    except Exception as e:
        return {"error": f"获取文件信息失败: {e}"}

@mcp.tool()
def read_log_lines(file_path: str, start_line: int = 0, count: int = None) -> List[Dict]:
    """读取指定范围的日志行
    
    Args:
        file_path: 日志文件路径（大模型调用时传入）
        start_line: 起始行号（从0开始）
        count: 读取行数，如果为None则读取所有行
    """
    try:
        validated_path = _validate_file_path(file_path)
        parser = LogParser(validated_path)
        entries = parser.read_lines(start_line, count)
        return [_convert_entry_to_dict(entry) for entry in entries]
    except Exception as e:
        return [{"error": f"读取日志失败: {e}"}]

@mcp.tool()
def search_logs(file_path: str, keyword: str, max_results: int = 100) -> List[Dict]:
    """搜索包含关键词的日志条目
    
    Args:
        file_path: 日志文件路径（大模型调用时传入）
        keyword: 搜索关键词
        max_results: 最大返回结果数
    """
    try:
        validated_path = _validate_file_path(file_path)
        parser = LogParser(validated_path)
        entries = parser.search_logs(keyword, max_results)
        return [_convert_entry_to_dict(entry) for entry in entries]
    except Exception as e:
        return [{"error": f"搜索日志失败: {e}"}]

@mcp.tool()
def analyze_attack_types(file_path: str) -> Dict:
    """分析攻击类型统计
    
    Args:
        file_path: 日志文件路径（大模型调用时传入）
    """
    try:
        validated_path = _validate_file_path(file_path)
        parser = LogParser(validated_path)
        attack_stats = {}
        
        with open(parser.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                entry = parser.parse_line(line.strip())
                if entry and entry.attack_type != '-':
                    attack_stats[entry.attack_type] = attack_stats.get(entry.attack_type, 0) + 1
        
        return attack_stats
    except Exception as e:
        return {"error": f"分析攻击类型时出错: {e}"}

@mcp.tool()
def analyze_ip_stats(file_path: str, top_n: int = 10) -> Dict:
    """分析IP访问统计
    
    Args:
        file_path: 日志文件路径（大模型调用时传入）
        top_n: 返回前N个IP
    """
    try:
        validated_path = _validate_file_path(file_path)
        parser = LogParser(validated_path)
        ip_stats = {}
        
        with open(parser.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                entry = parser.parse_line(line.strip())
                if entry:
                    ip_stats[entry.client_ip] = ip_stats.get(entry.client_ip, 0) + 1
        
        # 排序并返回前N个
        sorted_ips = sorted(ip_stats.items(), key=lambda x: x[1], reverse=True)[:top_n]
        return {"top_ips": sorted_ips, "total_unique_ips": len(ip_stats)}
    except Exception as e:
        return {"error": f"分析IP统计时出错: {e}"}

def run_server():
    """运行MCP服务器"""
    mcp.run()

if __name__ == "__main__":
    run_server()