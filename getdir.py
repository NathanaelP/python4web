#!/usr/bin/env python3

import ftplib

connect = ftplib.FTP("www.ualr.edu")
connect.login("facstaff\mmmcmillan", "meredith26")

data = []
connect.dir(data.append)
connect.quit()
for line in data:
	print(line)