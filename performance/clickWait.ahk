#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

ResizeWin(Width = 500,Height = 0)
{
  If %Width% = 0
    Width := W
  If %Height% = 0
    Height := H
  WinMove,A,,%X%,%Y%,%Width%,%Height%
}


^!y::  ; Control+Alt+Z hotkey.
;CoordMode, Mouse, Screen
;CoordMode, Pixel, Screen

Loop, 2
{
	yoffset := 45

	Loop
	{
		sleep, 4000
		WinActivate, blocklib
 	  WinGetPos,X,Y,W,H,A
		x := W - 310
		;MsgBox, 0, ,%x%, 
		Click, %x%, %yoffset%, 0
		sleep, 10
		Click, %x%, 50, 0
		sleep, 10
		Click, %x%, 55, 0
		sleep, 10
		Click, %x%, 60, 0

		MouseGetPos, xpos, ypos 
		;MsgBox, The cursor is at X%xpos% Y%ypos%. Should be at %x%, %y%.
		PixelGetColor, color, %x% , %yoffset%
		;MsgBox, 0, ,%color%, 0.5
		;WinGetTitle, title, blocklib
		;MsgBox, 0, ,%title%, 0
		if(color == 0x595959){
			x := W - 425
			;Click, %x%, %yoffset%, 0
			Click, %x%, %yoffset%
			sleep, 60000
			break
		}
	}
}
return

^!x::
ResizeWin()
return

