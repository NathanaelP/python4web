#!/usr/bin/env python3

import ftplib
import sys

filename = sys.argv[1]
onnect = ftplib.FTP("www.ualr.edu")
connect.login("facstaff\mmmcmillan", "meredith26")

connect.retrlines("RETR ", + filename)
connect.quit()