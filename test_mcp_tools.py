#!/usr/bin/env python3
"""
测试MCP工具函数，验证file_path参数传入功能
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp_server import get_file_info, read_log_lines, search_logs, analyze_attack_types, analyze_ip_stats

def test_mcp_tools():
    """测试MCP工具函数"""
    
    # 测试文件路径（使用项目中的示例日志文件）
    test_file = "20250410"
    
    print("=== 测试MCP工具函数 ===")
    print(f"使用测试文件: {test_file}")
    print()
    
    # 测试1: 获取文件信息
    print("1. 测试获取文件信息:")
    try:
        result = get_file_info(test_file)
        print(f"   结果: {result}")
    except Exception as e:
        print(f"   错误: {e}")
    print()
    
    # 测试2: 读取日志行
    print("2. 测试读取日志行 (前3行):")
    try:
        result = read_log_lines(test_file, start_line=0, count=3)
        print(f"   读取到 {len(result)} 行")
        if result and not result[0].get('error'):
            print(f"   第一行示例: {result[0].get('client_ip', 'N/A')} - {result[0].get('url', 'N/A')}")
    except Exception as e:
        print(f"   错误: {e}")
    print()
    
    # 测试3: 搜索日志
    print("3. 测试搜索日志 (搜索关键词 'GET'):")
    try:
        result = search_logs(test_file, keyword="GET", max_results=5)
        print(f"   找到 {len(result)} 条匹配记录")
        if result and not result[0].get('error'):
            print(f"   第一条匹配: {result[0].get('request_method', 'N/A')} {result[0].get('url', 'N/A')}")
    except Exception as e:
        print(f"   错误: {e}")
    print()
    
    # 测试4: 分析攻击类型
    print("4. 测试分析攻击类型:")
    try:
        result = analyze_attack_types(test_file)
        if result.get('error'):
            print(f"   错误: {result['error']}")
        else:
            print(f"   攻击类型统计: {result}")
    except Exception as e:
        print(f"   错误: {e}")
    print()
    
    # 测试5: 分析IP统计
    print("5. 测试分析IP统计 (前5个):")
    try:
        result = analyze_ip_stats(test_file, top_n=5)
        if result.get('error'):
            print(f"   错误: {result['error']}")
        else:
            print(f"   总唯一IP数: {result.get('total_unique_ips', 0)}")
            print(f"   前5个IP: {result.get('top_ips', [])}")
    except Exception as e:
        print(f"   错误: {e}")
    print()

if __name__ == "__main__":
    test_mcp_tools()