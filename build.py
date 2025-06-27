#!/usr/bin/env python3
"""
构建脚本 - 使用uv构建和安装包
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """运行命令并处理错误"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description}成功")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description}失败")
        print(f"错误: {e}")
        if e.stdout:
            print(f"输出: {e.stdout}")
        if e.stderr:
            print(f"错误输出: {e.stderr}")
        return False

def main():
    """主函数"""
    print("🚀 MCP Log Analyzer 构建脚本")
    print("=" * 50)
    
    # 检查uv是否安装
    if not run_command("uv --version", "检查uv版本"):
        print("请先安装uv: pip install uv")
        sys.exit(1)
    
    # 清理之前的构建
    print("\n🧹 清理之前的构建文件...")
    for dir_name in ["build", "dist", "*.egg-info"]:
        if os.path.exists(dir_name):
            run_command(f"rmdir /s /q {dir_name}", f"删除 {dir_name}")
    
    # 构建包
    if not run_command("uv build", "构建包"):
        sys.exit(1)
    
    # 显示构建结果
    if os.path.exists("dist"):
        print("\n📦 构建的包文件:")
        for file in os.listdir("dist"):
            print(f"  - dist/{file}")
    
    # 安装包（开发模式）
    if not run_command("uv pip install -e .", "安装包（开发模式）"):
        sys.exit(1)
    
    # 测试安装
    if not run_command("mcp_log_analyze --version", "测试命令行工具"):
        sys.exit(1)
    
    # 运行测试
    if not run_command("python -m pytest tests/ -v", "运行测试"):
        sys.exit(1)
    
    print("\n🎉 构建和安装完成！")
    print("\n📋 使用方法:")
    print("  mcp_log_analyze --help    # 查看帮助")
    print("  mcp_log_analyze           # 启动MCP服务器")
    print("\n📁 项目结构:")
    print("  src/mcp_log_analyzer/     # 源代码")
    print("  tests/                    # 测试文件")
    print("  dist/                     # 构建的包")

if __name__ == "__main__":
    main()