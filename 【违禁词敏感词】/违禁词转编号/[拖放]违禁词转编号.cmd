@echo off
echo 正在处理：%1

py 违禁词转编号.py 【2编】字库编码.txt %1 %~n1_转编.txt

pause