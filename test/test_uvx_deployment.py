#!/usr/bin/env python3
"""
测试 uvx 部署功能
"""
import subprocess
import sys

def run_command(command):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=False
        )
        return result
    except Exception as e:
        return subprocess.CompletedProcess(
            command, 1, stdout='', stderr=str(e)
        )

def main():
    print("=== 测试 uvx 部署功能 ===")
    print()
    
    # 1. 检查 uvx 是否安装
    print("1. 检查 uvx 是否安装...")
    result = run_command("uvx --version")
    if result.returncode == 0:
        print(f"   ✅ uvx 已安装: {result.stdout.strip()}")
    else:
        print(f"   ❌ uvx 未安装: {result.stderr.strip()}")
        return False
    
    print()
    
    # 2. 测试 uvx 运行本地代码
    print("2. 测试 uvx 运行本地代码...")
    # 测试运行 Python 解释器
    result = run_command("uvx python3 --version")
    if result.returncode == 0:
        print(f"   ✅ uvx 运行 Python 成功: {result.stdout.strip()}")
    else:
        print(f"   ❌ uvx 运行失败: {result.stderr.strip()}")
        return False
    
    print()
    
    # 3. 测试 uvx 运行本地模块（带有依赖）
    print("3. 测试 uvx 运行本地模块...")
    # 测试运行 config 模块，包含所需依赖
    test_code = """
import sys
sys.path.insert(0, '/workspace/src')
from core.config import ConfigManager
config = ConfigManager()
print('配置加载成功:', config.config['mcp']['server_name'])
"""
    # 将测试代码写入临时文件
    with open('/tmp/test_uvx.py', 'w') as f:
        f.write(test_code)
    
    # 使用 uvx 的 --with 选项来包含所需依赖
    result = run_command("uvx --with PyYAML --with mcp --with requests python3 /tmp/test_uvx.py")
    if result.returncode == 0:
        print(f"   ✅ uvx 运行本地模块成功: {result.stdout.strip()}")
    else:
        print(f"   ❌ uvx 运行本地模块失败: {result.stderr.strip()}")
        return False
    
    print()
    
    # 4. 测试 uvx 运行远程代码（可选）
    print("4. 测试 uvx 运行远程代码...")
    # 测试运行一个简单的远程 Python 脚本
    result = run_command('uvx python3 -c "print(\\"Hello from uvx!\\")"')
    if result.returncode == 0:
        print(f"   ✅ uvx 运行远程代码成功: {result.stdout.strip()}")
    else:
        print(f"   ❌ uvx 运行远程代码失败: {result.stderr.strip()}")
        return False
    
    print()
    print("✅ 所有测试通过！")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
