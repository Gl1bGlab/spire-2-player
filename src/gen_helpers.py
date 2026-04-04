from win32 import win32gui

def game_window_foreground_check(game_window) -> None:
    msg_printed = False
    while win32gui.GetForegroundWindow() != game_window:
        if not msg_printed:
            print("Waiting for Slay the Spire 2 to be the foreground window")
            msg_printed = True
        pass