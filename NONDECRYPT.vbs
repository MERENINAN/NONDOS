
     set x = WScript.CreateObject("WScript.Shell")
     mySecret = inputbox("Enter the Text to be Encrypted.")
  mySecret = StrReverse(mySecret)
     x.Run "%windir%\notepad"
     wscript.sleep 1000 
     x.sendkeys encode(mySecret)
     function encode(s) 
        For i = 1 To Len(s) 
           newtxt = Mid(s, i, 1)
           newtxt = Chr(Asc(newtxt)-3) 
           coded = coded & newtxt 
        Next 
        encode = coded 
     End Function