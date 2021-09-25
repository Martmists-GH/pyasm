import dis

from asm.ops.abc import *
from asm.ops.py30 import *

if sys.version_info >= (3, 1, 0):
    from asm.ops.py31 import *

if sys.version_info >= (3, 2, 0):
    from asm.ops.py32 import *

if sys.version_info >= (3, 3, 0):
    from asm.ops.py33 import *

if sys.version_info >= (3, 4, 0):
    from asm.ops.py34 import *

if sys.version_info >= (3, 5, 0):
    from asm.ops.py35 import *

if sys.version_info >= (3, 6, 0):
    from asm.ops.py36 import *

if sys.version_info >= (3, 7, 0):
    from asm.ops.py37 import *

if sys.version_info >= (3, 8, 0):
    from asm.ops.py38 import *

if sys.version_info >= (3, 9, 0):
    from asm.ops.py39 import *

if sys.version_info >= (3, 10, 0):
    from asm.ops.py310 import *

ALL_OPS = {v: eval(k) for k, v in opmap.items()}

__all__ = tuple(dis.opmap.keys()) + (
    "Opcode", "JumpOp", "RelJumpOp", "AbsJumpOp",
    "NameOp", "VarOp", "ConstOp", "CellOp"
)
