#!/usr/bin/env python3
"""
测试日志解析器功能
"""

from log_parser import LogParser

def test_parser():
    """测试日志解析器基本功能"""
    
    # 初始化解析器
    parser = LogParser("20250410")
    
    # 检查文件是否存在
    if not parser.file_path.exists():
        print("错误: 日志文件不存在")
        return
    
    print("=== 文件信息 ===")
    file_info = parser.get_file_info()
    for key, value in file_info.items():
        print(f"{key}: {value}")
    
    print("\n=== 读取前5行日志 ===")
    entries = parser.read_lines(0, 5)
    for i, entry in enumerate(entries):
        print(f"第{i+1}行:")
        print(f"  请求时间: {entry.request_time}")
        print(f"  客户端IP: {entry.client_ip}")
        print(f"  域名: {entry.domain}")
        print(f"  URL: {entry.url}")
        print(f"  攻击类型: {entry.attack_type}")
        print(f"  拦截状态: {entry.intercept_status}")
        print()
    
    print("=== 读取所有日志行数统计 ===")
    all_entries = parser.read_lines()  # 默认读取所有行
    print(f"总共解析成功的日志条目数: {len(all_entries)}")
    
    print("=== 搜索SCANNER相关日志 ===")
    scanner_logs = parser.search_logs("SCANNER", 3)
    for i, entry in enumerate(scanner_logs):
        print(f"SCANNER日志{i+1}:")
        print(f"  时间: {entry.request_time}")
        print(f"  IP: {entry.client_ip}")
        print(f"  URL: {entry.url}")
        print()
    
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_parser()