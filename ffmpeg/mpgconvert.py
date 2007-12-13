#!/usr/bin/python
#./mpgconvert.py
#A script which uses ffmpeg binary, which might help one convert .mpg files to .wmv 
#Copyright (C) 2008 Wayde Milas (bronto@noip.sk)
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; Version 3 of the License.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

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



