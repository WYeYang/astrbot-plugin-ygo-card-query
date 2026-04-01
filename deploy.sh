#!/bin/bash
# 游戏王查卡 MCP 服务器 - Linux 部署脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_error "未找到 Python，请先安装 Python 3.8 或更高版本"
        exit 1
    fi
    
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
    print_info "检测到 Python 版本: $PYTHON_VERSION"
}

check_git() {
    if ! command -v git &> /dev/null; then
        print_error "未找到 Git，请先安装 Git"
        exit 1
    fi
    print_info "Git 已安装"
}

create_venv() {
    if [ -d "venv" ]; then
        print_info "虚拟环境已存在"
    else
        print_info "创建 Python 虚拟环境..."
        $PYTHON_CMD -m venv venv
        print_success "虚拟环境创建成功"
    fi
}

activate_venv() {
    print_info "激活虚拟环境..."
    source venv/bin/activate
    print_success "虚拟环境已激活"
}

install_dependencies() {
    print_info "安装依赖..."
    pip install --upgrade pip
    pip install -r requirements.txt
    print_success "依赖安装完成"
}

init_database() {
    if [ -d "ygopro_database" ]; then
        print_info "数据库目录已存在"
    else
        print_info "初始化游戏王卡片数据库..."
        print_warning "首次下载可能需要较长时间，请耐心等待..."
        
        git clone --depth 1 https://github.com/moecube/ygopro-database.git ygopro_database_temp
        
        if [ -d "ygopro_database_temp/locales/zh-CN" ]; then
            mkdir -p ygopro_database
            cp ygopro_database_temp/locales/zh-CN/cards.cdb ygopro_database/
            if [ -f "ygopro_database_temp/locales/zh-CN/card_extra.db" ]; then
                cp ygopro_database_temp/locales/zh-CN/card_extra.db ygopro_database/
            fi
            rm -rf ygopro_database_temp
            print_success "数据库初始化完成"
        else
            print_error "数据库文件下载失败"
            rm -rf ygopro_database_temp
            exit 1
        fi
    fi
}

update_database() {
    print_info "更新游戏王卡片数据库..."
    if [ -d "ygopro_database_temp" ]; then
        rm -rf ygopro_database_temp
    fi
    
    git clone --depth 1 https://github.com/moecube/ygopro-database.git ygopro_database_temp
    
    if [ -d "ygopro_database_temp/locales/zh-CN" ]; then
        mkdir -p ygopro_database
        cp -f ygopro_database_temp/locales/zh-CN/cards.cdb ygopro_database/
        if [ -f "ygopro_database_temp/locales/zh-CN/card_extra.db" ]; then
            cp -f ygopro_database_temp/locales/zh-CN/card_extra.db ygopro_database/
        fi
        rm -rf ygopro_database_temp
        print_success "数据库更新完成"
    else
        print_error "数据库更新失败"
        rm -rf ygopro_database_temp
        exit 1
    fi
}

run_server() {
    print_info "启动 MCP 服务器..."
    $PYTHON_CMD mcp_server.py
}

show_help() {
    echo "游戏王查卡 MCP 服务器 - 部署运行脚本"
    echo ""
    echo "用法: $0 [命令]"
    echo ""
    echo "命令:"
    echo "  install     安装依赖并初始化数据库（首次部署）"
    echo "  run         运行 MCP 服务器"
    echo "  update      更新卡片数据库"
    echo "  help        显示帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 install    # 首次部署"
    echo "  $0 run        # 运行服务器"
    echo "  $0 update     # 更新数据库"
}

case "${1:-}" in
    install)
        print_info "开始部署..."
        check_python
        check_git
        create_venv
        activate_venv
        install_dependencies
        init_database
        print_success "部署完成！"
        echo ""
        echo "运行以下命令启动服务器:"
        echo "  ./deploy.sh run"
        ;;
    run)
        check_python
        if [ ! -d "venv" ]; then
            print_error "虚拟环境不存在，请先运行: $0 install"
            exit 1
        fi
        activate_venv
        run_server
        ;;
    update)
        check_git
        if [ ! -d "venv" ]; then
            print_error "虚拟环境不存在，请先运行: $0 install"
            exit 1
        fi
        activate_venv
        update_database
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        show_help
        exit 1
        ;;
esac
