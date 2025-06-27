#!/usr/bin/env python3
"""
命令行入口点
"""

import sys
import argparse
from .mcp_server import run_server

def main():
    """主入口点函数 - 直接启动MCP服务器"""
    try:
        # 直接启动MCP服务器，不需要额外的命令行参数
        # MCP服务器通过stdio与客户端通信
        run_server()
        
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"启动MCP服务器时出错: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()