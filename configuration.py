#!/usr/bin/env python

# genKeyLine code by Hordur Heidarsson
# rest Oliver Matthews

import base64
import sys

secrets = []
labels = []
lengths = []
time_zone = "+0"

def genKeyLine( code ):
  secret_key = code.replace(' ','').upper()
  if len(secret_key) <= 32:
    key_b32 = secret_key+'='*(32%len(secret_key))
    key = base64.b32decode(key_b32)
  else:
    key_b64 = secret_key+'='*(64%len(secret_key))
    key = base64.b32decode(key_b64)
  key_bytes = map(ord,key)
  lengths.append( len(key_bytes) )
  key_hex = ["0x%02X" % x for x in key_bytes]
  return "{ " + ', '.join(key_hex) + " },"

def genAppId(key):
  # Start with 8 bytes of a static UUID
  ar = [ "0xA4", "0xA6", "0x13", "0xB5", "0x8A", "0x6B", "0x4F", "0xF0"]
  # Append 8 more bytes of the given key
  for i in xrange(2, 45, 6):
    ar.append( key[ i : i+4] )
  return ", ".join(ar)

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
    labels.append( key )
    secrets.append( genKeyLine(value) )
f.close()

f = open( "src/configuration.h","w" )
#f = sys.stderr
f.write( "#ifndef _CONFIGURATION_H_\n#define _CONFIGURATION_H_\n" )
f.write( "#define NUM_SECRETS %i\n" % len(labels) )
f.write( "#define DEFAULT_TIME_ZONE %s\n" % time_zone )
f.write( "#define APP_NAME \"Authenticator %s\"\n" % labels[0])
f.write( "#define MY_UUID { %s }\n" % genAppId( secrets[0]) )
f.write( "char otplabels[NUM_SECRETS][10] = {\n    " )
for label in labels:
  f.write( "\"%s\"," % label )
f.write( "\n};\n" )
f.write( "unsigned char otpkeys[NUM_SECRETS][%s] = {\n    " % max(lengths) )
for secret in secrets:
  f.write( "%s\n" % secret )
f.write( "};\n" )
f.write ("int otpsizes[NUM_SECRETS] = { ")
for length in lengths:
  f.write( "%s," % length )
f.write( "};\n#endif\n" )

f.close()
