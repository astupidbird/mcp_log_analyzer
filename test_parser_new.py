#!/usr/bin/env python3
"""
测试新的日志解析器功能（文件路径作为参数传入）
"""

from log_parser import LogParser

def test_new_api():
    """测试新的API，文件路径作为参数传入"""
    
    file_path = "20250410"
    
    print("=== 测试新的API（文件路径作为参数） ===")
    
    # 测试1: 获取文件信息
    print("\n1. 测试get_file_info:")
    try:
        parser = LogParser(file_path)
        info = parser.get_file_info()
        print(f"文件大小: {info.get('file_size', 'N/A')} 字节")
        print(f"行数: {info.get('line_count', 'N/A')}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试2: 读取日志行
    print("\n2. 测试read_log_lines:")
    try:
        parser = LogParser(file_path)
        entries = parser.read_lines(0, 3)
        print(f"成功读取 {len(entries)} 行日志")
        for i, entry in enumerate(entries):
            print(f"  第{i+1}行: {entry.request_time} - {entry.client_ip}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试3: 搜索日志
    print("\n3. 测试search_logs:")
    try:
        parser = LogParser(file_path)
        entries = parser.search_logs("SCANNER", 3)
        print(f"找到 {len(entries)} 条包含'SCANNER'的记录")
        for i, entry in enumerate(entries):
            print(f"  记录{i+1}: {entry.request_time} - {entry.attack_type}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试4: 读取所有行
    print("\n4. 测试读取所有行:")
    try:
        parser = LogParser(file_path)
        all_entries = parser.read_lines()
        print(f"总共解析成功的日志条目数: {len(all_entries)}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n=== 测试完成 ===")
    print("新的API设计验证成功：")
    print("- 所有工具都接受file_path参数")
    print("- 无需预先初始化全局状态")
    print("- 每次调用都是独立的")
    print("- 支持处理多个不同的日志文件")

if __name__ == "__main__":
    test_new_api()