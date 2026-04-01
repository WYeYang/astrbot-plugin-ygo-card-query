@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM 游戏王查卡 MCP 服务器 - Windows 部署脚本

set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

:main
if "%1"=="" goto :help
if "%1"=="install" goto :install
if "%1"=="run" goto :run
if "%1"=="update" goto :update
if "%1"=="help" goto :help
if "%1"=="--help" goto :help
if "%1"=="-h" goto :help
goto :help

:check_python
echo [INFO] 检查 Python...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] 未找到 Python，请先安装 Python 3.8 或更高版本
    echo         下载地址: https://www.python.org/downloads/
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [INFO] 检测到 Python 版本: %PYTHON_VERSION%
exit /b 0

:check_git
echo [INFO] 检查 Git...
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] 未找到 Git，请先安装 Git
    echo         下载地址: https://git-scm.com/download/win
    exit /b 1
)
echo [INFO] Git 已安装
exit /b 0

:create_venv
if exist "venv" (
    echo [INFO] 虚拟环境已存在
) else (
    echo [INFO] 创建 Python 虚拟环境...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] 创建虚拟环境失败
        exit /b 1
    )
    echo [SUCCESS] 虚拟环境创建成功
)
exit /b 0

:activate_venv
echo [INFO] 激活虚拟环境...
call venv\Scripts\activate.bat
echo [SUCCESS] 虚拟环境已激活
exit /b 0

:install_dependencies
echo [INFO] 安装依赖...
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] 依赖安装失败
    exit /b 1
)
echo [SUCCESS] 依赖安装完成
exit /b 0

:init_database
if exist "ygopro_database" (
    echo [INFO] 数据库目录已存在
    exit /b 0
)

echo [INFO] 初始化游戏王卡片数据库...
echo [WARNING] 首次下载可能需要较长时间，请耐心等待...

git clone --depth 1 https://github.com/moecube/ygopro-database.git ygopro_database_temp
if %errorlevel% neq 0 (
    echo [ERROR] 数据库下载失败
    if exist "ygopro_database_temp" rd /s /q "ygopro_database_temp"
    exit /b 1
)

if exist "ygopro_database_temp\locales\zh-CN" (
    if not exist "ygopro_database" mkdir "ygopro_database"
    copy /y "ygopro_database_temp\locales\zh-CN\cards.cdb" "ygopro_database\" >nul
    if exist "ygopro_database_temp\locales\zh-CN\card_extra.db" (
        copy /y "ygopro_database_temp\locales\zh-CN\card_extra.db" "ygopro_database\" >nul
    )
    rd /s /q "ygopro_database_temp"
    echo [SUCCESS] 数据库初始化完成
) else (
    echo [ERROR] 数据库文件下载失败
    if exist "ygopro_database_temp" rd /s /q "ygopro_database_temp"
    exit /b 1
)
exit /b 0

:update_database
echo [INFO] 更新游戏王卡片数据库...
if exist "ygopro_database_temp" rd /s /q "ygopro_database_temp"

git clone --depth 1 https://github.com/moecube/ygopro-database.git ygopro_database_temp
if %errorlevel% neq 0 (
    echo [ERROR] 数据库更新失败
    if exist "ygopro_database_temp" rd /s /q "ygopro_database_temp"
    exit /b 1
)

if exist "ygopro_database_temp\locales\zh-CN" (
    if not exist "ygopro_database" mkdir "ygopro_database"
    copy /y "ygopro_database_temp\locales\zh-CN\cards.cdb" "ygopro_database\" >nul
    if exist "ygopro_database_temp\locales\zh-CN\card_extra.db" (
        copy /y "ygopro_database_temp\locales\zh-CN\card_extra.db" "ygopro_database\" >nul
    )
    rd /s /q "ygopro_database_temp"
    echo [SUCCESS] 数据库更新完成
) else (
    echo [ERROR] 数据库更新失败
    if exist "ygopro_database_temp" rd /s /q "ygopro_database_temp"
    exit /b 1
)
exit /b 0

:run_server
echo [INFO] 启动 MCP 服务器...
python -m ygo_card_query.mcp.server
exit /b 0

:install
echo [INFO] 开始部署...
call :check_python
if %errorlevel% neq 0 exit /b 1
call :check_git
if %errorlevel% neq 0 exit /b 1
call :create_venv
if %errorlevel% neq 0 exit /b 1
call :activate_venv
if %errorlevel% neq 0 exit /b 1
call :install_dependencies
if %errorlevel% neq 0 exit /b 1
call :init_database
if %errorlevel% neq 0 exit /b 1
echo.
echo [SUCCESS] 部署完成！
echo.
echo 运行以下命令启动服务器:
echo   deploy.bat run
exit /b 0

:run
call :check_python
if %errorlevel% neq 0 exit /b 1
if not exist "venv" (
    echo [ERROR] 虚拟环境不存在，请先运行: deploy.bat install
    exit /b 1
)
call :activate_venv
if %errorlevel% neq 0 exit /b 1
call :run_server
exit /b 0

:update
call :check_git
if %errorlevel% neq 0 exit /b 1
if not exist "venv" (
    echo [ERROR] 虚拟环境不存在，请先运行: deploy.bat install
    exit /b 1
)
call :activate_venv
if %errorlevel% neq 0 exit /b 1
call :update_database
exit /b 0

:help
echo 游戏王查卡 MCP 服务器 - 部署运行脚本
echo.
echo 用法: %~nx0 [命令]
echo.
echo 命令:
echo   install     安装依赖并初始化数据库（首次部署）
echo   run         运行 MCP 服务器
echo   update      更新卡片数据库
echo   help        显示帮助信息
echo.
echo 示例:
echo   %~nx0 install    # 首次部署
echo   %~nx0 run        # 运行服务器
echo   %~nx0 update     # 更新数据库
exit /b 0
