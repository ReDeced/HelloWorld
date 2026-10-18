# -*- coding: utf-8 -*-
# -*- mode: python -*-
# ---------------------------------------------------------------------------
#  大悲咒 · 稽首皈依
#  南無喝囉怛那哆囉夜耶　南無阿唎耶
#  婆盧羯帝爍鉢囉耶　菩提薩埵婆耶
# ---------------------------------------------------------------------------
#  ГЛАВНЫЙ ТЕСТ ПРОЕКТА. Обходит все *.py и проверяет ОДНО ПРАВИЛО:
#  каждая переменная — ровно 16 символов, первый 'O', остальные пятнадцать —
#  смесь 'O' и '0'. Плюс два правила письма: числа двоичные, строки
#  шестнадцатеричные. Это страховка от будущих изменений, а не декорация:
#  добавьте `self` или `tmp` — тесты упадут.
# ---------------------------------------------------------------------------

import ast as O0OO000OO0O0O000
import os as OO0O0O0000OOOOOO
import re as OO0OO0O0000O00O0

import pytest as OO0OO00O00OO0O0O

O00OO00O00OOOO00 = OO0O0O0000OOOOOO.path.dirname(OO0O0O0000OOOOOO.path.dirname(OO0O0O0000OOOOOO.path.abspath(__file__)))

O00O000O0OO0O00O = OO0OO0O0000O00O0.compile("\x5e\x4f\x5b\x4f\x30\x5d\x7b\x31\x35\x7d\x24")

# Единственные законные имена, которые нельзя переименовать.
O000OO0O00OOO0OO = {
    "\x5f\x5f\x69\x6e\x69\x74\x5f\x5f", "\x5f\x5f\x6e\x61\x6d\x65\x5f\x5f", "\x5f\x5f\x66\x69\x6c\x65\x5f\x5f", "\x5f\x5f\x64\x6f\x63\x5f\x5f", "\x5f\x5f\x61\x6c\x6c\x5f\x5f", "\x5f\x5f\x74\x65\x73\x74\x5f\x5f",
    "\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f", "\x5f\x5f\x73\x70\x65\x63\x5f\x5f", "\x5f\x5f\x6c\x6f\x61\x64\x65\x72\x5f\x5f", "\x5f\x5f\x70\x61\x63\x6b\x61\x67\x65\x5f\x5f", "\x5f\x5f\x70\x61\x74\x68\x5f\x5f",
    "\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f", "\x5f\x5f\x6d\x6f\x64\x75\x6c\x65\x5f\x5f", "\x5f\x5f\x71\x75\x61\x6c\x6e\x61\x6d\x65\x5f\x5f", "\x5f\x5f\x61\x6e\x6e\x6f\x74\x61\x74\x69\x6f\x6e\x73\x5f\x5f", "\x5f\x5f\x77\x65\x61\x6b\x72\x65\x66\x5f\x5f",
}

O00OOO0OO0OO00O0 = {"\x2e\x67\x69\x74", "\x5f\x5f\x70\x79\x63\x61\x63\x68\x65\x5f\x5f", "\x2e\x70\x79\x74\x65\x73\x74\x5f\x63\x61\x63\x68\x65", "\x2e\x6d\x79\x70\x79\x5f\x63\x61\x63\x68\x65", "\x62\x75\x69\x6c\x64", "\x64\x69\x73\x74"}


def OO0OO00O0O0O0O0O():
    OO000O00OO000OOO = []
    for O0OO00O000O00O0O, O0OOOO0OO000OO0O, OO0O0000OOO00OOO in OO0O0O0000OOOOOO.walk(O00OO00O00OOOO00):
        O0OOOO0OO000OO0O[:] = [O0OOOO00O00O0OOO for O0OOOO00O00O0OOO in O0OOOO0OO000OO0O if O0OOOO00O00O0OOO not in O00OOO0OO0OO00O0]
        for OO0O0000O00OO0OO in OO0O0000OOO00OOO:
            if OO0O0000O00OO0OO.endswith("\x2e\x70\x79"):
                OO000O00OO000OOO.append(OO0O0O0000OOOOOO.path.join(O0OO00O000O00O0O, OO0O0000O00OO0OO))
    return sorted(OO000O00OO000OOO)


def OOO00O00OO00000O():
    OO0O0O000O0O00OO = {}
    for OO0O0OO00OOO0O00 in OO0OO00O0O0O0O0O():
        with open(OO0O0OO00OOO0O00, "\x72", encoding="\x75\x74\x66\x2d\x38") as OO000OO000000000:
            OO0O0O000O0O00OO[OO0O0OO00OOO0O00] = OO000OO000000000.read()
    return OO0O0O000O0O00OO


def O0OOO0O000OOO00O(OO0O0000O00OO0OO, OOOO00000OO0OO00):
    # 一切法　皆由心造: dunder'ы Python диктует сам язык, их не переименовать.
    if OO0O0000O00OO0OO in O000OO0O00OOO0OO or (OO0O0000O00OO0OO.startswith("\x5f\x5f") and OO0O0000O00OO0OO.endswith("\x5f\x5f")):
        return
    assert O00O000O0OO0O00O.match(OO0O0000O00OO0OO), "\x25\x73\x3a\x20\x62\x61\x64\x20\x6e\x61\x6d\x65\x20\x25\x72" % (OOOO00000OO0OO00, OO0O0000O00OO0OO)


class O000O0O0O00OO0OO(O0OO000OO0O0O000.NodeVisitor):
    # 阿難!我與汝說六根顛倒　因緣妄想　所生三昧
    def __init__(OO0OOOO0OOOO0OO0, OOOO00000OO0OO00):
        OO0OOOO0OOOO0OO0.OOOO00000OO0OO00 = OOOO00000OO0OO00
        OO0OOOO0OOOO0OO0.OO000O00OO000OOO = []
        OO0OOOO0OOOO0OO0.O0O0OOOOOO0O0OOO = set()

    def visit_Name(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 不增不減
        if isinstance(OO0O00O00O0O0O00.ctx, (O0OO000OO0O0O000.Store, O0OO000OO0O0O000.Del)):
            OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.id, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))

    def visit_arg(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 無有恐怖
        OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.arg, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_FunctionDef(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 遠離顛倒夢想
        if OO0O00O00O0O0O00.name not in OO0OOOO0OOOO0OO0.O0O0OOOOOO0O0OOO:
            OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.name, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_AsyncFunctionDef(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 究竟涅槃
        OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.name, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_ClassDef(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 即是諸佛
        OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.name, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        # Класс, наследующий ЧУЖОЕ (ast.NodeVisitor), диктует имена своих
        # методов внешней библиотекой. Их не переименовывают — иначе обход
        # дерева перестанет их находить.
        if any(isinstance(O0OO00O000O00O0O, O0OO000OO0O0O000.Attribute) for O0OO00O000O00O0O in OO0O00O00O0O0O00.bases):
            for O0OOO0O00OOO0OO0 in OO0O00O00O0O0O00.body:
                if isinstance(O0OOO0O00OOO0OO0, (O0OO000OO0O0O000.FunctionDef, O0OO000OO0O0O000.AsyncFunctionDef)):
                    OO0OOOO0OOOO0OO0.O0O0OOOOOO0O0OOO.add(O0OOO0O00OOO0OO0.name)
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_Attribute(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 唯心所造
        if isinstance(OO0O00O00O0O0O00.ctx, O0OO000OO0O0O000.Store):
            OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.attr, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_alias(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 舍利子
        OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append(((OO0O00O00O0O0O00.asname or OO0O00O00O0O0O00.name).split("\x2e")[0b0], OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_Global(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 是名諸佛
        for OO0O0000O00OO0OO in OO0O00O00O0O0O00.names:
            OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O0000O00OO0OO, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_Nonlocal(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 發菩提心
        for OO0O0000O00OO0OO in OO0O00O00O0O0O00.names:
            OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O0000O00OO0OO, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    def visit_ExceptHandler(OO0OOOO0OOOO0OO0, OO0O00O00O0O0O00):
        # 佛法僧三寶
        if OO0O00O00O0O0O00.name:
            OO0OOOO0OOOO0OO0.OO000O00OO000OOO.append((OO0O00O00O0O0O00.name, OO0OOOO0OOOO0OO0.OOOO00000OO0OO00))
        OO0OOOO0OOOO0OO0.generic_visit(OO0O00O00O0O0O00)

    # Имена ключевых аргументов ЧУЖИХ функций (open(..., encoding=...))
    # переменными проекта не являются, поэтому не проверяются.
    # Свои же вызовы обязаны быть переименованы — это проверяет сам код:
    # иначе они бы не запустились.


def O0OOO0OO00O0O0O0():
    OO0O0O000O0O00OO = []
    for OO0O0OO00OOO0O00, OOO0O0OO0O0OO0O0 in OOO00O00OO00000O().items():
        OOOO00000OO0OO00 = OO0O0O0000OOOOOO.path.relpath(OO0O0OO00OOO0O00, O00OO00O00OOOO00)
        OOO0OO0000O00O00 = O0OO000OO0O0O000.parse(OOO0O0OO0O0OO0O0, filename=OO0O0OO00OOO0O00)
        OOO0OOOOO0O0000O = O000O0O0O00OO0OO(OOOO00000OO0OO00)
        OOO0OOOOO0O0000O.visit(OOO0OO0000O00O00)
        OO0O0O000O0O00OO.extend(OOO0OOOOO0O0000O.OO000O00OO000OOO)
    return OO0O0O000O0O00OO


def OO0O00O0OOO0OO00():
    O0OO000OOOO00OO0 = []
    for OO0O0OO00OOO0O00, OOO0O0OO0O0OO0O0 in OOO00O00OO00000O().items():
        OOO0OO0000O00O00 = O0OO000OO0O0O000.parse(OOO0O0OO0O0OO0O0, filename=OO0O0OO00OOO0O00)
        for OO0O00O00O0O0O00 in O0OO000OO0O0O000.walk(OOO0OO0000O00O00):
            if not isinstance(OO0O00O00O0O0O00, O0OO000OO0O0O000.Constant):
                continue
            if isinstance(OO0O00O00O0O0O00.value, bool) or not isinstance(OO0O00O00O0O0O00.value, int):
                continue
            OOO00O0O000O0000 = O0OO000OO0O0O000.get_source_segment(OOO0O0OO0O0OO0O0, OO0O00O00O0O0O00) or ""
            if not OOO00O0O000O0000.startswith("\x30\x62"):
                O0OO000OOOO00OO0.append((OO0O0O0000OOOOOO.path.relpath(OO0O0OO00OOO0O00, O00OO00O00OOOO00), OO0O00O00O0O0O00.lineno, OOO00O0O000O0000))
    return O0OO000OOOO00OO0


def OO0O00OO000000OO():
    O0OO000OOOO00OO0 = []
    for OO0O0OO00OOO0O00, OOO0O0OO0O0OO0O0 in OOO00O00OO00000O().items():
        OOO0OO0000O00O00 = O0OO000OO0O0O000.parse(OOO0O0OO0O0OO0O0, filename=OO0O0OO00OOO0O00)
        for OO0O00O00O0O0O00 in O0OO000OO0O0O000.walk(OOO0OO0000O00O00):
            if not isinstance(OO0O00O00O0O0O00, O0OO000OO0O0O000.Constant) or not isinstance(OO0O00O00O0O0O00.value, str):
                continue
            OOO00O0O000O0000 = O0OO000OO0O0O000.get_source_segment(OOO0O0OO0O0OO0O0, OO0O00O00O0O0O00) or ""
            OOO0O000O00OO0OO = OOO00O0O000O0000.lstrip("\x72\x62\x66\x75\x52\x42\x46\x55")
            if OO0O00O00O0O0O00.value and not OOO0O000O00OO0OO.startswith("\x22\x5c\x78"):
                O0OO000OOOO00OO0.append((OO0O0O0000OOOOOO.path.relpath(OO0O0OO00OOO0O00, O00OO00O00OOOO00), OO0O00O00O0O0O00.lineno, OOO00O0O000O0000[:0b101000]))
    return O0OO000OOOO00OO0


def O00O00O000OOOO00():
    assert len(OO0OO00O0O0O0O0O()) >= 0b1000, "\x65\x78\x70\x65\x63\x74\x65\x64\x20\x61\x74\x20\x6c\x65\x61\x73\x74\x20\x38\x20\x70\x79\x74\x68\x6f\x6e\x20\x66\x69\x6c\x65\x73"


def O00O00O00O0000OO():
    O0OO000OOOO00OO0 = O0OOO0OO00O0O0O0()
    for OO0O0000O00OO0OO, OOOO00000OO0OO00 in O0OO000OOOO00OO0:
        O0OOO0O000OOO00O(OO0O0000O00OO0OO, OOOO00000OO0OO00)
    assert len(O0OO000OOOO00OO0) > 0b11001000, "\x6f\x6e\x6c\x79\x20\x25\x64\x20\x6e\x61\x6d\x65\x73\x20\x63\x6f\x6c\x6c\x65\x63\x74\x65\x64" % len(O0OO000OOOO00OO0)


def O00O00O0O00O00O0():
    OO0O0000OOO00OOO = set(OO0O0000O00OO0OO for OO0O0000O00OO0OO, O0O0OOO00OO0O000 in O0OOO0OO00O0O0O0() if not OO0O0000O00OO0OO.startswith("\x5f"))
    assert len(OO0O0000OOO00OOO) > 0b1010000, "\x6f\x6e\x6c\x79\x20\x25\x64\x20\x64\x69\x73\x74\x69\x6e\x63\x74\x20\x6e\x61\x6d\x65\x73\x20\x66\x6f\x75\x6e\x64" % len(OO0O0000OOO00OOO)
    assert "\x73\x65\x6c\x66" not in OO0O0000OOO00OOO
    assert "\x63\x6c\x73" not in OO0O0000OOO00OOO


def O00O00OO0O00OOOO():
    for OO0O0OO00OOO0O00 in OO0OO00O0O0O0O0O():
        OOO00O0O0OO0OOOO = OO0O0O0000OOOOOO.path.splitext(OO0O0O0000OOOOOO.path.basename(OO0O0OO00OOO0O00))[0b0]
        if OOO00O0O0OO0OOOO in ("\x63\x6f\x6e\x66\x74\x65\x73\x74", "\x5f\x5f\x69\x6e\x69\x74\x5f\x5f"):
            continue
        assert O00O000O0OO0O00O.match(OOO00O0O0OO0OOOO), "\x66\x69\x6c\x65\x20\x6e\x61\x6d\x65\x20\x25\x73\x20\x69\x73\x20\x6e\x6f\x74\x20\x63\x6f\x6e\x66\x6f\x72\x6d\x69\x6e\x67" % OOO00O0O0OO0OOOO


def O00O00OO0OOO0O0O():
    assert not OO0O00O0OOO0OO00(), "\x64\x65\x63\x69\x6d\x61\x6c\x20\x6e\x75\x6d\x62\x65\x72\x73\x20\x66\x6f\x75\x6e\x64\x3a\x20\x25\x72" % OO0O00O0OOO0OO00()[:0b1000]


def O00O00OOO00O000O():
    assert not OO0O00OO000000OO(), "\x70\x6c\x61\x69\x6e\x20\x73\x74\x72\x69\x6e\x67\x73\x20\x66\x6f\x75\x6e\x64\x3a\x20\x25\x72" % OO0O00OO000000OO()[:0b1000]


def O00O00OOOOO00000():
    # 若無有我　無人無眾生
    from xemu import O00O000O000O0OOO
    OO00OO00O0OO0OOO = O00O000O000O0OOO(O0OOOOOOOOOOOO00=False)
    OO00OO00O0OO0OOO.OO00OO000O00OOOO("\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x2e\x64\x61\x74\x61\x0a\x4f\x30\x4f\x4f\x30\x4f\x4f\x30\x30\x30\x30\x30\x4f\x4f\x4f\x30\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x64\x62\x20\x22\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21\x22\x2c\x20\x31\x30\x0a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x2e\x74\x65\x78\x74\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x2e\x67\x6c\x6f\x62\x61\x6c\x20\x4f\x30\x4f\x30\x4f\x4f\x4f\x30\x4f\x4f\x4f\x4f\x30\x30\x4f\x4f\x0a\x4f\x30\x4f\x30\x4f\x4f\x4f\x30\x4f\x4f\x4f\x4f\x30\x30\x4f\x4f\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6d\x6f\x76\x20\x72\x61\x78\x2c\x20\x31\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6d\x6f\x76\x20\x72\x64\x69\x2c\x20\x31\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6c\x65\x61\x20\x72\x73\x69\x2c\x20\x5b\x72\x69\x70\x20\x2b\x20\x4f\x30\x4f\x4f\x30\x4f\x4f\x30\x30\x30\x30\x30\x4f\x4f\x4f\x30\x5d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6d\x6f\x76\x20\x72\x64\x78\x2c\x20\x31\x33\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x79\x73\x63\x61\x6c\x6c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6d\x6f\x76\x20\x72\x61\x78\x2c\x20\x36\x30\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x78\x6f\x72\x20\x72\x64\x69\x2c\x20\x72\x64\x69\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x79\x73\x63\x61\x6c\x6c\x0a", "\x69\x6e\x6c\x69\x6e\x65\x2e\x61\x73\x6d")
    assert OO00OO00O0OO0OOO.OO0OOO0O0O00O0OO() == 0b0
    assert OO00OO00O0OO0OOO.OOO0O0OO0O0OO0O0() == b"Hello, World!"


OO0OO00O0O0O0O0O.__test__ = False
OOO00O00OO00000O.__test__ = False
O0OOO0O000OOO00O.__test__ = False
O0OOO0OO00O0O0O0.__test__ = False
OO0O00O0OOO0OO00.__test__ = False
OO0O00OO000000OO.__test__ = False