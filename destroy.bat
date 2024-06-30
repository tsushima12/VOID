@echo off 

color a 
echo Hello, start the destroyer?(Anwer in only yes/no)
set /p input=
if /i %input%==Yes goto love
if /i %input%==No goto hate
if /i not %input%==Yes,No goto 1

:love
echo hahaha
echo See You Later
timeout 3
shutdown -s -t 100

:hate
echo Get destroyed
echo nigga you deserve it!
timeout 3
shutdown -s -t 100