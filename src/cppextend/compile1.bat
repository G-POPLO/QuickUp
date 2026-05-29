@REM 编译 QUmodule.cpp 为 Python 扩展模块
@REM 需要在 Visual Studio x64 Native Tools Command Prompt 中运行

set PYTHON_INCLUDE="C:\Program Files\Python314\include"
set PYTHON_LIB="C:\Program Files\Python314\libs\python314.lib"

cl /utf-8 /LD /I%PYTHON_INCLUDE% QUmodule.cpp %PYTHON_LIB% advapi32.lib Ole32.lib user32.lib Shell32.lib Comctl32.lib dwmapi.lib /std:c++20 /O2 /DNDEBUG /Fe:QUmodule.pyd
cl /utf-8 /LD /I%PYTHON_INCLUDE% hotkeymodule.cpp %PYTHON_LIB% user32.lib /std:c++20 /O2 /DNDEBUG /Fe:hotkeymodule.pyd
