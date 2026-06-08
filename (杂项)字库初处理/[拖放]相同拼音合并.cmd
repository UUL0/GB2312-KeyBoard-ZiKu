@echo off
echo 正在处理：%1

py 相同拼音合并.py %1 %~n1_拼音合并.txt

pause