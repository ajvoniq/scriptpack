#!/usr/bin/python

import os;
import subprocess;

def getff():
	if not os.path.exists("ffmpeg.exe"):
		return False;
	else:
		pr, ps = os.pipe();
		p=subprocess.Popen(["./ffmpeg.exe","-version"], 0, None,
			None,ps,ps,
			None,None, False,
 			".",None, False);
		result=p.wait();
		if result==0:
			return os.path.abspath("ffmpeg.exe");
		else:
			print "'ffmpeg.exe -version' returns error!";
			return false;


def convert( orig, audio, new):
	if orig == "" or audio=="" or new=="":
		print "Bad parameters passed!";
		return 1;
	
	


files = os.listdir(".");

ffmpeg=getff();
if ffmpeg==False:
	raise Exception("Cannot find or run ffmpeg!");

for  file in files:
	if file.endswith(".mpg"):
		audio=file.replace(".mpg", ".wav")
		recoded="R"+file;
		print file+" "+audio+" "+recoded;
		ret=subprocess.call([ffmpeg, "-i", file,
			"-vn", "-ac", "2", audio]);
		if ret!=0:
			raise Exception("ffmpeg returned error");
		ret=subprocess.call([ffmpeg,
			"-i", file,
			"-i", audio,
			"-sameq",
			recoded]);
		if ret!=0:
			raise Exception("ffmpeg returned error");



