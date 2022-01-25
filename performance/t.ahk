^!z::  ; Control+Alt+Z hotkey.
MouseGetPos, MouseX, MouseY
PixelGetColor, color, %MouseX%, %MouseY%
test := color == 0x5054c7
MsgBox The color at the current cursor position is %color% == 0x5054c7 -> %test%.
return