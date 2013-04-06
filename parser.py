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
	device = plistlib.Plist.fromFile(infile)

	writer.writerow(( 
		(device.get("ownerName")), 
		(device.get("ownerEmail")), 
		(device.get("deviceWiFiMACAddress")), 
		(device.get("deviceSerialNumber")), 
		(device.get("deviceIMEI")), 
		(device.get("deviceName")), 
		(device.get("deviceProductVersion")), 
		(device.get("deviceClass")) 
		))
finally:
    f.close()
