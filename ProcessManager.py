"""
ProcessManager.py
* Window Application의 목록 탐색
* 특정 Window Application을 선택하면, Application의 Processid 반환
"""
import win32gui
import win32process


def getActiveWindow():
    activeWindowName = None

    window = win32gui.GetForegroundWindow()
    activeWindowList = win32gui.GetWindow()
    print(activeWindowList)


def winEnumHandelr(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        windowName = win32gui.GetWindowText(hwnd)
        processId = win32process.GetWindowThreadProcessId(hwnd)

        if windowName:
            print(processId, windowName)


if __name__ == "__main__":
    win32gui.EnumWindows(winEnumHandelr, None)
