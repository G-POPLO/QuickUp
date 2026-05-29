def start_hotkey(fsmodifier:int, fskey:int, callback:function) -> None:
    """
    fsmodifier: the modifier key for the hotkey (e.g. MOD_ALT)
    fskey: the key code for the hotkey (e.g. ord('Q'))
    callback: the function to be called when the hotkey is pressed
    """
    ...
def stop_hotkey() -> None:
    # stop the hotkey.
    ...
