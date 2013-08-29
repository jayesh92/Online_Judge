#! /usr/bin/python
import os
import sys
import cgi
#import cgitb
#cgitb.enable()


def printing(x,nick):
	fpin=open("../status.html",'r')
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	filein=fpin.readlines()
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	fpin.close()
	a="<tr class=\"odd\">\n"
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	if filein[89]==a:
		filein.insert(89,"<tr>\n")
	else:
		filein.insert(89,"<tr class=\"odd\">\n")
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	var_x="<td>" + str(nick)+ "</td>\n"
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	if x==-1:
		v_t="UPLOAD_PROBLEM"
	elif x==0:
		v_t="CORRECT ANSWER"
	elif x==1:
		v_t="WRONG ANSWER"
	elif x==2:
		v_t="TLE"
	elif x==3:
		v_t="RUNTIME ERROR"
	elif x==4:
		v_t="RUNTIME ERROR(NZEC)"
	elif x==5:
		v_t="COMPILATION ERROR"
	var_y="<td>"+v_t+"</td>\n"
	#print "Content-Type: text/html\n\n"
	#print "khuli"
	filein.insert(90,var_x)
	filein.insert(91,var_y)
	filein.insert(92,"</tr>\n")
	#print "Content-Type: text/html\n\n"
	#print "khuli"

	fpin=open("../status.html",'w')
#	print "Content-Type: text/html\n\n"
#	print "khuli"
	for i in filein:
		fpin.write(i)
	fpin.close()
	print "Content-Type: text/html\n\n"
	if x==-1:
		print "<html><head><style type=\"text/css\" >a{outline:0}h1{width:800px;margin:180px 0px 0px 400px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>UPLOAD PROBLEM..plz upload again</h1>"
		print "<img src=\"sad.png\" height=\"200\" width=\"200\" />"
	elif x==0:
		print "<html><head><style type=\"text/css\" >a{outline:0}h1{width:800px;margin:180px 0px 0px 500px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>CORRECT ANSWER </h1>"
		print "<img src=\"happy.jpg\" height=\"200\" width=\"200\" />"
	elif x==1:
		print "<html><head><style type=\"text/css\" >a{outline:0} h1{width:800px;margin:180px 0px 0px 500px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>WRONG ANSWER </h1>"
		print "<img src=\"sad.png\" height=\"200\" width=\"200\" />"
	elif x==2:
		print "<html><head><style type=\"text/css\" >a{outline:0} h1{width:800px;margin:180px 0px 0px 600px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>TLE </h1>"
		print "<img src=\"sad.png\" height=\"200\" width=\"200\" />"
	elif x==3:
		print "<html><head><style type=\"text/css\" > a{outline:0}h1{width:800px;margin:180px 0px 0px 500px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>RUNTIME ERROR </h1>"
		print "<img src=\"sad.png\" height=\"200\" width=\"200\" />"
	elif x==4:
		print "<html><head><style type=\"text/css\" >a{outline:0} h1{width:800px;margin:180px 0px 0px 420px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>RUNTIME ERROR(NZEC) </h1>"
		print "<img src=\"sad.png\" height=\"200\" width=\"200\" />"
	elif x==5:
		print "<html><head><style type=\"text/css\" >a{outline:0} h1{width:800px;margin:180px 0px 0px 500px;}img{margin:0 -400px 0 550px}</style><body>"
		print "<h1>COMPILATION ERROR</h1>"
		print "<img src=\"./sad.png\" height=\"200\" width=\"200\" />"
	print "<br>"
	print "<a href=\"../submit.html\"><img src=\"back.png\" height=\"40\" width=\"40\" /></a><a href=\"../status.html\"><img src=\"Status.png\" height=\"30\" width=\"50\" /></a><body></html>"
	return


form=cgi.FieldStorage()
filedata = form['upload']
nickname=form.getvalue('user')
#print "Content-Type: text/html\n\n"
nickname=cgi.escape(nickname)
#print nickname
#print type(nickname)
#print "Content-Type: text/html\n\n"
#print "Content-Type: text/html\n\n"
#print "in"
#sys.exit()
if filedata.filename:
	to_be_uploaded="../upload_dir/" + filedata.filename
	itr=0
	while(1):
		if os.path.isfile(to_be_uploaded):
			fil_name=str(itr)+os.path.basename(to_be_uploaded)
			to_be_uploaded="../upload_dir/"+fil_name
			itr=itr+1
		else:
			break
	open(to_be_uploaded,'w').write(filedata.file.read())
	fil_name=os.path.basename(to_be_uploaded)
#	print "Content-Type: text/html\n\n"
#	print "files saved successfully\n"
#	print fil_name
	#sys.exit()
else:
	printing(-1,nickname)
	sys.exit()

compile_command="gcc -o "+fil_name+".out "+to_be_uploaded
#print compile_command
#print
#print 
exit_compile=os.system(compile_command)
#print exit_compile

delete_file="rm -rf "+to_be_uploaded
if exit_compile!=0:
	printing(5,nickname)
	#print "COMPILATION ERROR"
	os.system(delete_file)
	sys.exit()
#else:
#	print "COMPILED SUCCESFULLY"

#ch_command="chmod 777 ./"+fil_name+".out"
#os.system(ch_command)
	
run_command= "perl -e \'alarm shift @ARGV; exec @ARGV\' 1 /ug/ug2k11/cse/jayesh.lahori/public_html/cgi-bin/"+fil_name + ".out < ../testcases > ../output"
#print run_command
#print
exit_run=os.system(run_command)
#print exit_run
#print
delete_out="rm -rf "+"./"+fil_name+".out"

if exit_run==36352:
#	print "TIME LIMIT EXCEDED"
	printing(2,nickname)
	os.system(delete_out)
	os.system(delete_file)
	sys.exit()
	
elif exit_run==65280:
#	print "RUN TIME ERROR(SIGSEGV)"
	printing(4,nickname)
	os.system(delete_out)
	os.system(delete_file)
	sys.exit()

elif exit_run!=0:
#	print "RUN TIME ERROR"
	printing(3,nickname)
	os.system(delete_out)
	os.system(delete_file)
	sys.exit()
	
else:
	os.system(delete_out)
	os.system(delete_file)
#	print "RUN SUCCESSFULL"
#	sys.exit()	
#print "jayesh"
fp1=open("../output",'r')
fp2=open("../pre_output",'r')
file1=fp1.readlines()
file2=fp2.readlines()
fp1.close()
fp2.close()
x=0
flag=0
if file1==file2:
#	print "correct answer"
	printing(0,nickname)
	sys.exit()
else:
	#print "wrong answer"
	printing(1,nickname)
	sys.exit()

