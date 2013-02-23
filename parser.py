#!/usr/bin/python
import plistlib, sys, os, glob, csv

reload(sys)
sys.setdefaultencoding( "utf-8" )
path = ''
f = open(sys.argv[1], 'wt')

try:
    writer = csv.writer(f)
    writer.writerow( ('Owner', 'Email', 'MAC-adress', 'Serialnumber', 'IMEI', 'Devicename', 'Version', 'Type') )
    for infile in glob.glob( os.path.join(path, '*.deviceinfo') ):
	plist = plistlib.Plist.fromFile(infile)

	writer.writerow(( 
		(plist.get("ownerName")), 
		(plist.get("ownerEmail")), 
		(plist.get("deviceWiFiMACAddress")), 
		(plist.get("deviceSerialNumber")), 
		(plist.get("deviceIMEI")), 
		(plist.get("deviceName")), 
		(plist.get("deviceProductVersion")), 
		(plist.get("deviceClass")) 
		))
finally:
    f.close()
