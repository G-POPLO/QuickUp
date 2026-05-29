# ./config.py
"""
QuickUp configuration file.
"""
import os
import json

from cppextend.QUmodule import detect_app_theme

# 默认设置
settings = {
    'general': {
        'theme': 'light',# light dark system
        'patternRank': 75,
        'maxSearchCount': 5,
        'showHidden': False,
        'topMost': False,
        'checkUpdate': True,
        'closeToTray': True,
    },
    'advanced': {
        'runWhenStart': False,
        'disAdmin': False,
        'autoSave': False,
        'enableHotkey': True,
        'callUp': [0x0001, 0x51],
        'zoneRetryTimes': 20,
    },
    'storage': {}
}

theme_original = 'light'

def init_config():
    """
    初始化配置文件
    """
    global theme_original
    config_dir = os.path.join(os.path.expanduser('~'), '.QuickUp')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    general_path = os.path.join(config_dir, 'config-general.json')
    if not os.path.exists(general_path):
        with open(general_path, 'w', encoding='utf-8') as f:
            json.dump(settings['general'], f, indent=4)
    else:
        with open(general_path, 'r', encoding='utf-8') as f:
            settings['general'].update(json.load(f))
            theme_original = settings['general']['theme']
            if theme_original == 'system':
                settings['general']['theme'] = detect_app_theme()

    advanced_path = os.path.join(config_dir, 'config-advanced.json')
    if not os.path.exists(advanced_path):
        with open(advanced_path, 'w', encoding='utf-8') as f:
            json.dump(settings['advanced'], f, indent=4)
    else:
        with open(advanced_path, 'r', encoding='utf-8') as f:
            settings['advanced'].update(json.load(f))

    storage_path = os.path.join(config_dir, 'config-storage.json')
    if not os.path.exists(storage_path):
        with open(storage_path, 'w', encoding='utf-8') as f:
            json.dump(settings['storage'], f, indent=4)
    else:
        with open(storage_path, 'r', encoding='utf-8') as f:
            settings['storage'].update(json.load(f))

def save_config():
    """
    保存配置文件
    """
    with open(os.path.join(os.path.expanduser('~'), '.QuickUp', 'config-general.json'), 'w', encoding='utf-8') as f:
        settings['general']['theme'] = theme_original
        json.dump(settings['general'], f, indent=4)
        if theme_original == 'system':
            settings['general']['theme'] = detect_app_theme()
    with open(os.path.join(os.path.expanduser('~'), '.QuickUp', 'config-advanced.json'), 'w', encoding='utf-8') as f:
        json.dump(settings['advanced'], f, indent=4)
    with open(os.path.join(os.path.expanduser('~'), '.QuickUp', 'config-storage.json'), 'w', encoding='utf-8') as f:
        json.dump(settings['storage'], f, indent=4)
