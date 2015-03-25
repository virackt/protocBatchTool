#!/usr/bin/env python
#coding:utf-8
import os
print "输入proto文件绝对目录:"
inputPath= raw_input()
print "输入proto文件输出目录:"
outputPath=raw_input()
for x in os.listdir(inputPath):
	if os.path.splitext(x)[1]=='.proto':
		path = os.path.join(inputPath, x)   
		os.system('protoc -I=' + inputPath + ' --java_out=' + outputPath+ ' ' + path)
		print "处理完：" + x

print("=====end=======")
