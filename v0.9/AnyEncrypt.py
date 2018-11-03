#!/usr/bin/python3
import os
import platform
import hashlib

def PrintLogo():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

	print()
	print(" *_______________________________________________________________* ")
	print("||      Welcome to                                               ||")
	print("||      _                _____                             _     ||")
	print("||     / \   _ __  _   _| ____|_ __   ___ _ __ _   _ _ __ | |_   ||")
	print("||    / _ \ | '_ \| | | |  _| | '_ \ / __| '__| | | | '_ \| __|  ||")
	print("||   / ___ \| | | | |_| | |___| | | | (__| |  | |_| | |_) | |_   ||")
	print("||  /_/   \_\_| |_|\__, |_____|_| |_|\___|_|   \__, | .__/ \__|  ||")
	print("||                 |___/                       |___/|_|          ||")
	print("||  							 v0.9	 ||")
	print("||  Script for encrypt text with any algorithms                  ||")
	print("||  Author: Temuri Takalandze (ABGEO)                            ||")
	print("||          www.ABGEO.ga                                         ||")
	print("||          abgeo@abgeo.ga                                       ||")
	print("||          (+995) 579 19-47-27                                  ||")
	print("||_______________________________________________________________||")
	print()
#End PrintLogo

def GetHelp():
	PrintLogo()
	print("...Help Text...")
#End GetHelp

def Encrypt(Algorythm, Text = ''):
	if Text != '':
		_result = ''
		if Algorythm == 'MD5':
			md5 = hashlib.md5()
			md5.update(Text.encode('utf-8'))
			_result = md5.hexdigest()
		elif Algorythm == 'SHA256':
			sha256 = hashlib.sha256()
			sha256.update(Text.encode('utf-8'))
			_result = sha256.hexdigest()

		print('"' + Text + '" in ' + Algorythm + ' is ' + _result)
	else:
		_TryAgain = str(input ("Cannot encrypt empty string. Try Again? [Y/n] "))
		if _TryAgain == 'Y' or _TryAgain == 'y':
			SelectAction()
		else:
			return
#End Encrypt

def SelectAction():
	PrintLogo()
	print('Actions\n' +
	'[h] or [Help] - For more information\n' +
	'[q] - For Exit\n\n' +
	'Encryption Algorithms\n' +
	'[1] - MD5\n' +
	'[2] - SHA256\n' +
	'')

	_Action = str(input ("Select Action: "))

	_EncAlgh = ""
	if _Action == 'help' or _Action == 'h':
		GetHelp()
	elif _Action == '1':
		_EncAlgh = 'MD5'
	elif _Action == 'q' or _Action == 'Q':
		return
	elif _Action == '2':
		_EncAlgh = 'SHA256'
	else:
		SelectAction()

	if _Action != "help" or _Action != "h":
		_Text = str(input ("Enter Text: "))
		Encrypt(_EncAlgh, _Text)

	_TryAgain = str(input ("Encrypt New Text? [Y/n] "))
	if _TryAgain == 'Y' or _TryAgain == 'y':
		SelectAction()
#End SelectAction

SelectAction()
