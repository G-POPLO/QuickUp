# ./runner/hotkey.py
"""
热键监听模块，当QuickUp主界面位于托盘时启用
"""
import atexit

import config
from cppextend.QUmodule import start_hotkey, stop_hotkey

reg = None
_callback = None
_is_running = False

def start_listen(command=None):
    # 开始监听热键
    global reg, _callback, _is_running
    if command is not None:
        _callback = command
    if not config.settings['advanced'].get('enableHotkey', True):
        if _is_running:
            pause_listen()
        return
    if _is_running:
        return
    fsModifiers = config.settings['advanced']['callUp'][0]
    vk = config.settings['advanced']['callUp'][1]
    start_hotkey(fsModifiers, vk, _callback)
    _is_running = True
    if not reg:
        reg = atexit.register(pause_listen)

def pause_listen():
    # 暂停监听热键
    global _is_running
    if not _is_running:
        return
    stop_hotkey()
    _is_running = False
