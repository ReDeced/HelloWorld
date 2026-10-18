; ===========================================================================
;  般若波羅蜜多心經
;  觀自在菩薩　行深般若波羅蜜多時　照見五蘊皆空
;  度一切苦厄　舍利子　色不異空　空不異色
; ===========================================================================
;  The only program that matters. It writes to STDOUT and then dies politely.
;  Labels are sixteen characters long, begin with O and mix O with zero,
;  exactly like the Python variables that assembled it.
; ===========================================================================

        .data

O0OO0OO00000OOO0:
        db      "\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21", 0b1010

O0O0000OO00OOOOO0 equ  0b1101
OO0O0O0O0O0O0OO0 equ  O0OO0OO00000OOO0 + O0O0000OO00OOOOO0

        .text
        .global O0O0OOO0OOOO00OO

; ---------------------------------------------------------------------------
;  揭諦揭諦　波羅揭諦　波羅僧揭諦　菩提薩婆訶
; ---------------------------------------------------------------------------
O0O0OOO0OOOO00OO:
        lea     rdi, [rip + O0OO0OO00000OOO0]
        mov     rsi, OO0O0O0O0O0O0OO0
        call    O0OOO0O00OOO000O
        mov     rdx, rax

        mov     rax, 0b1
        mov     rdi, 0b1
        lea     rsi, [rip + O0OO0OO00000OOO0]
        syscall

        mov     rax, 0b111100
        xor     rdi, rdi
        syscall

; ---------------------------------------------------------------------------
;  rdi = first byte, rsi = one past the last -> rax = count of bytes
;  是無等等咒　能除一切苦　真實不虛
; ---------------------------------------------------------------------------
O0OOO0O00OOO000O:
        mov     rbx, rdi
        xor     rax, rax

O0OO000O00OOOOOO0:
        cmp     rbx, rsi
        jae     O00O00OOO0000000O
        inc     rbx
        inc     rax
        jmp     O0OO000O00OOOOOO0

O00O00OOO0000000O:
        ret