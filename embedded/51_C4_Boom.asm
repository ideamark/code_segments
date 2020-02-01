;*********************************************************
;程序名：C4炸弹定时控制器
;程序类型：51汇编
;硬件平台：STC89C52RC
;作者：YangTing
;日期：2011/5/18
;已通过Keil uVision4编译通过
;--------------------------------------------------------
;工作过程：
;定时器通电后，先设定初始时间，再按启动键启动计时，
;计时过程中有嘀嘀声和指示灯闪烁，并在计时快结束时
;蜂鸣器有段渐加速鸣叫过程，完全模仿CS中的C4效果
;计时结束时自动开启继电器引爆雷管
;特别说明：本装置仅供娱乐，不得用于非法用途！
;--------------------------------------------------------
;定时器参数：
;工作电压：DC5V
;最大计时范围：1小时
;--------------------------------------------------------
;单片机资源使用情况：
;寄存器：R0,R1,R2,R3,R4,R5,R6,R7
;定时中断：T0
;外部中断：INT0,INT1
;--------------------------------------------------------
;单片机管脚说明：
;数码管扫描：P1.0~P1.3
;数码管显示：P0.0~P0.7
;计时指示灯：P2.0,P2.1
;蜂鸣器：     P1.5
;雷管继电器：P1.4
;*********************************************************

FLAG BIT P2.0         ;1秒时基标志位
FLAG2 BIT P1.6        ;0.5秒时基标志位
FLAG3 BIT P2.1          ;加速鸣叫标志位
R41 DATA 20H          ;中间变量寄存单元

ORG 0000H
AJMP START
ORG 000BH
AJMP TIME0
ORG 0003H
AJMP P32
ORG 0013H
AJMP P33
ORG 30H

START:                ;初始化
MOV SP,#5FH
MOV R41,#10
MOV R0,#0
MOV R1,#0
MOV R2,#0
MOV R3,#0            ;秒数初始值
MOV R4,#0
MOV R5,#0
MOV R6,#0            ;分数初始值
MOV R7,#0
SETB FLAG
SETB FLAG2
SETB FLAG3
MOV A,#0
MOV B,#0
MOV DPTR,#CODETAB
MOV P1,#0FFH
MOV P3,#0FFH
MOV TMOD,#01H
MOV TH0,#3CH
MOV TL0,#0B0H
SETB EA
SETB EX0
SETB EX1
SETB ET0

SETNUM:                ;初始时间设置子程序
MOV A,R6
MOV B,#10
DIV AB
MOV B,A
MOVC A,@A+DPTR
MOV P0,A
CLR P1.0
MOV R1,#0FFH
D41:DJNZ R1,D41
SETB P1.0
;--------
MOV A,#10
MUL AB
MOV B,A
MOV A,R6
CLR C
SUBB A,B
MOVC A,@A+DPTR
MOV P0,A
CLR P1.1
MOV R1,#0FFH
D51:DJNZ R1,D51
SETB P1.1
;--------
MOV A,R3
MOV B,#10
DIV AB
MOV B,A
MOVC A,@A+DPTR
MOV P0,A
CLR P1.2
MOV R1,#0FFH
D61:DJNZ R1,D61
SETB P1.2
;--------
MOV A,#10
MUL AB
MOV B,A
MOV A,R3
CLR C
SUBB A,B
MOVC A,@A+DPTR
MOV P0,A
CLR P1.3
MOV R1,#0FFH
D71:DJNZ R1,D71
SETB P1.3
;--------
JB P3.4,OUT2
MOV R4,#050H
M16:MOV R5,#0FFH
M17:DJNZ R5,M17
M18:DJNZ R4,M16
JB P3.4,OUT2
CLR P1.5
MOV R4,#0FFH
M13:MOV R5,#0FFH
M14:DJNZ R5,M14
M15:DJNZ R4,M13
SETB P1.5
MOV R4,#0
MOV R5,#0
CLR EX0
CLR EX1
SETB TR0
AJMP LOOP
OUT2:
AJMP SETNUM

P32:             ;外部中断INT0服务程序，用于设置初始秒数
PUSH ACC
PUSH PSW
JB P3.2,OUT0
MOV R4,#050H
M4:MOV R5,#0FFH
M5:DJNZ R5,M5
M6:DJNZ R4,M4
JB P3.2,OUT0
CLR P1.5
INC R3
CJNE R3,#60,OUT0
MOV R3,#0

OUT0:
MOV R4,#080H
M1:MOV R5,#0FFH
M2:DJNZ R5,M2
M3:DJNZ R4,M1
SETB P1.5
AJMP RETI1
 
P33:             ;外部中断INT1服务程序，用于设置初始分数
PUSH ACC
PUSH PSW
JB P3.3,OUT1
MOV R4,#050H
M7:MOV R5,#0FFH
M8:DJNZ R5,M8
M9:DJNZ R4,M7
JB P3.3,OUT1
CLR P1.5
INC R6
CJNE R6,#60,OUT1
MOV R6,#0

OUT1:
MOV R4,#080H
M10:MOV R5,#0FFH
M11:DJNZ R5,M11
M12:DJNZ R4,M10
SETB P1.5
AJMP RETI1

RETI1:
POP PSW
POP ACC
RETI

LOOP:                     ;主程序
JNB FLAG2,NEXT1
CLR P1.5
AJMP NEXT2

NEXT1:
SETB P1.5

NEXT2:
MOV A,R6
MOV B,#10
DIV AB
MOV B,A
MOVC A,@A+DPTR
MOV P0,A
CLR P1.0
MOV R1,#0FFH
D01:DJNZ R1,D01
SETB P1.0
;--------
MOV A,#10
MUL AB
MOV B,A
MOV A,R6
CLR C
SUBB A,B
MOVC A,@A+DPTR
MOV P0,A
CLR P1.1
MOV R1,#0FFH
D11:DJNZ R1,D11
SETB P1.1
;--------
MOV A,R3
MOV B,#10
DIV AB
MOV B,A
MOVC A,@A+DPTR
MOV P0,A
CLR P1.2
MOV R1,#0FFH
D21:DJNZ R1,D21
SETB P1.2
;--------
MOV A,#10
MUL AB
MOV B,A
MOV A,R3
CLR C
SUBB A,B
MOVC A,@A+DPTR
MOV P0,A
CLR P1.3
MOV R1,#0FFH
D31:DJNZ R1,D31
SETB P1.3
AJMP LOOP

TIME0:                    ;定时器0（时基）中断服务程序
PUSH ACC
PUSH PSW
MOV TH0,#3CH
MOV TL0,#0B0H
INC R4
CJNE R4,#10,NEXT0
JB FLAG3,NEXT4
MOV R41,R5
MOV R4,R41
CPL FLAG2
AJMP NEXT0

NEXT4:
MOV R4,#0      
CPL FLAG2

NEXT0:
INC R0
CJNE R0,#20,RETI0
MOV R0,#0
CPL FLAG
MOV A,R6
JZ NEXT8
MOV A,R3
JNZ NEXT8
MOV R3,#60

NEXT8:
CJNE R3,#60,NEXT6
DEC R6

NEXT6:
CJNE R3,#10,NEXT3
CJNE R6,#00,NEXT3
CLR FLAG3

NEXT3:
JB FLAG3,NEXT5
INC R5

NEXT5:
MOV A,R6
JNZ NEXT7
MOV A,R3
JNZ NEXT7
AJMP BANG

NEXT7:
DEC R3
AJMP RETI0

RETI0:                         ;与TIME0子程序配套
POP PSW
POP ACC
RETI

BANG:                          ;爆炸子程序
CLR EA
CLR ET0
CLR ET1
CLR TR0                           
CLR TR1
CLR P1.4
AJMP $

CODETAB:DB 0C0H,0F9H,0A4H,0B0H,99H,92H,82H,0F8H,80H,90H

END
