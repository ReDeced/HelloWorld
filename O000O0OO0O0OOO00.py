# -*- coding: utf-8 -*-
# -*- mode: python -*-
# ---------------------------------------------------------------------------
#  藥師十二願王
#  第一大願　願我來時　得阿耨多羅三藐三菩提
#  自身光明熾然照耀無量無數無邊世界
# ---------------------------------------------------------------------------
#  主程序。 Запускает prog/hello.asm и печатает Hello, World!
#  Ничего больше. Ни аргументов, ни подсказок, ни спасения.
# ---------------------------------------------------------------------------

import os as OO0O0O0000OOOOOO
import sys as OOO0O00OOO00O0O0

from xemu import O00O000O000O0OOO

O000O0OOO0OOO0OO = OO0O0O0000OOOOOO.path.join(OO0O0O0000OOOOOO.path.dirname(OO0O0O0000OOOOOO.path.abspath(__file__)),
                               "\x70\x72\x6f\x67", "\x68\x65\x6c\x6c\x6f\x2e\x61\x73\x6d")
O000O0OOO0O00O0O = 0b11110100001001000000


def OO0OO0O00O0O000O(OO0O0OO00OOO0O00):
    with open(OO0O0OO00OOO0O00, "\x72", encoding="\x75\x74\x66\x2d\x38") as OO000OO000000000:
        return OO000OO000000000.read()


def OO00OO0O0O00O000(O0OO0000OO00OO00=None):
    O0OO0000OO00OO00 = list(OOO0O00OOO00O0O0.argv[0b1:] if O0OO0000OO00OO00 is None else O0OO0000OO00OO00)
    OO0O0OO00OOO0O00 = O0OO0000OO00OO00[0b0] if O0OO0000OO00OO00 else O000O0OOO0OOO0OO
    O0OO0O000OOO000O = int(O0OO0000OO00OO00[0b1], 0b0) if len(O0OO0000OO00OO00) > 0b1 else O000O0OOO0O00O0O
    OO00OO00O0OO0OOO = O00O000O000O0OOO(O0OOOOOOOOOOOO00=True)
    OO00OO00O0OO0OOO.OO00OO000O00OOOO(OO0OO0O00O0O000O(OO0O0OO00OOO0O00), OO0O0O0000OOOOOO.path.basename(OO0O0OO00OOO0O00))
    O0OOO0OO000OOO0O = OO00OO00O0OO0OOO.OO0OOO0O0O00O0OO(OO00O0OOOO0OO0OO=O0OO0O000OOO000O)
    OOO0O00OOO00O0O0.stderr.write("\x0a\x25\x73\x3a\x20\x65\x78\x69\x74\x3d\x25\x64\x20\x73\x74\x65\x70\x73\x3d\x25\x64\x20\x74\x65\x78\x74\x3d\x25\x64\x0a"
                     % (OO0O0O0000OOOOOO.path.basename(OO0O0OO00OOO0O00), O0OOO0OO000OOO0O, OO00OO00O0OO0OOO.O0OOOO000000O00O.OOO00OO00OOO0000,
                        len(OO00OO00O0OO0OOO.OOO0O0OO0O0OO0O0())))
    return O0OOO0OO000OOO0O


if __name__ == "\x5f\x5f\x6d\x61\x69\x6e\x5f\x5f":
    OOO0O00OOO00O0O0.exit(OO00OO0O0O00O000())