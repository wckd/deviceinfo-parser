#!/usr/bin/python
import plistlib, sys, codecs, os, glob, csv

reload(sys)
sys.setdefaultencoding( "latin-1" )
path = ''
f = open(sys.argv[1], 'wt')

try:
    writer = csv.writer(f)
    writer.writerow( ('Owner', 'Email', 'MAC-adress', 'Serialnumber', 'IMEI', 'Devicename', 'Version') )
    for infile in glob.glob( os.path.join(path, '*.deviceinfo') ):
	plist = plistlib.Plist.fromFile(infile)

	writer.writerow( ((plist["ownerName"]), (plist["ownerEmail"]), (plist["deviceWiFiMACAddress"]), (plist["deviceSerialNumber"]), (plist["deviceIMEI"]), (plist["deviceName"]), (plist["deviceProductVersion"])) )
finally:
    f.close()
