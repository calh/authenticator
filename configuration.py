#!/usr/bin/env python

# genKeyLine code by Hordur Heidarsson
# rest Oliver Matthews

import base64
import sys
import hashlib

secret = "" 
label = ""
key_len = ""
time_zone = "+0"

def genKeyLine( code ):
  global key_len
  secret_key = code.replace(' ','').upper()
  if len(secret_key) <= 32:
    key_b32 = secret_key+'='*(32%len(secret_key))
    key = base64.b32decode(key_b32)
  else:
    key_b64 = secret_key+'='*(64%len(secret_key))
    key = base64.b32decode(key_b64)
  key_bytes = map(ord,key)
  key_len = len(key_bytes)
  key_hex = ["0x%02X" % x for x in key_bytes]
  return ', '.join(key_hex) 

# Generate a unique MY_UUID based on the label
def genAppId(str):
  # Salt MD5 with the string for our 16 bytes
  bytes = hashlib.md5(str).digest()
  bytes = map(ord,bytes)
  hex = ["%02X" % x for x in bytes]
  str = "%s-%s-%s-%s-%s" % ("".join(hex[0:4]), 
        "".join(hex[4:6]), "".join(hex[6:8]), "".join(hex[8:10]), "".join(hex[10:]))
  return str.lower()

try:
  f = open( 'configuration.txt','r' )
except:
  print "Unable to open configuration.txt. Cheack README.md for configuration details."
  sys.exit(1)

for line in f:
  line = line.strip()
  if( line.startswith('#') or not ':' in line ): continue
  key,value = line.split(':')
  if( key.lower() == "tz" ):
    time_zone = value
  else:
    label = key[:50]  # Truncate labels at 50 chars
    secret = genKeyLine(value)
f.close()

f = open( "appinfo.json","w" )
#f = sys.stderr
appinfo = """{
  "uuid": "%s",
  "shortName": "%s",
  "longName": "%s",
  "companyName": "pokey9000/IEF/rigel314/FBS",
  "versionCode": 1,
  "versionLabel": "1.0.0",
  "watchapp": {
    "watchface": true
  },
  "appKeys": {
    "dummy": 0
  },
  "resources": {
    "media": []
  }
}\n""" % (genAppId( label ), label, label )
f.write(appinfo)

f = open( "src/configuration.h","w" )
#f = sys.stderr
f.write( "#ifndef _CONFIGURATION_H_\n#define _CONFIGURATION_H_\n" )
f.write( "#define DEFAULT_TIME_ZONE %s\n" % time_zone )
# Truncate app name to 32 bytes
f.write( "char otplabel[50] = {\n    " )
f.write( "\"%s\"," % label )
f.write( "\n};\n" )
f.write( "unsigned char otpkey[%s] = {\n    " % key_len)
f.write( "%s\n" % secret )
f.write( "};\n" )
f.write ("int otpsize = %s;\n" % key_len)
f.write( "\n#endif\n" )

f.close()
