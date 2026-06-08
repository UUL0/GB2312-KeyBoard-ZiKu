@echo off
echo 正在处理：%1

py 违禁词编号-还原.py 【2编】字库编码.txt %1 -o %~n1_编还原.txt

pause