Name "ReadMeThe: Bible"
Outfile "readmethebible.exe"

InstallDir "$DESKTOP\RMTBible"

Section
	
	SetOutPath "$INSTDIR"

	File /r "dist\*.*"
	File "bible.txt"

	WriteUninstaller "$INSTDIR\uninstall.exe"

	CreateShortCut "$SMPROGRAMS\RMTBible.lnk" "$INSTDIR\readmethebible\readmethebible.exe"
	CreateShortCut "$DESKTOP\RMTBible.lnk" "$INSTDIR\readmethebible\readmethebible.exe"

SectionEnd

Section "uninstall"

	Delete "$SMPROGRAMS\RMTBible.lnk"
	Delete "$DESKTOP\RMTBible.lnk"
	
	Delete "$INSTDIR\*.*"

	RMDir "$INSTDIR"

SectionEnd
