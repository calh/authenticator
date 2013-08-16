Authenticator Watch Face
=============

This is a Google Authenticator (Time-Based One-Time Password generator) **watch face app** for the Pebble.

Forked off 'authenticator' by IEF, which was forked off 'twostep' by pokey9000, with patches from rigel314 

This is slightly different from the IEF version, which is a standard watch app.  A watch app 
must be accessed from the main menu.  Viewing a two-factor auth code then requires at least 
6 button presses, along with scrolling through multiple accounts if they are defined.

A watch face app installs the Authenticator screen along side your other watch faces.  A 
minimum of 1 button press is needed to view a two-factor auth code.

The caveat to this convenience is that you can only display one code per watch app.  The
configureation.py script creates a new UUID for each app based on the secret key defined
in configuration.txt.

To configure the application you need to create a configuration.txt file.

1. Copy configuration-sample.txt to configuration.txt

2. Set your timezone in configuration.txt - it's near the top, labelled 'tz'

3. Let's say you have secret key AXIMZYJXITSIOIJVNXOE76PEJQ 
On most sites, when setting up choose 'show key' when presented with the QR code.

4. add it to the end of configuration.txt, following the example in the format 
label:secret
(You may add only **one** key)

6. Generate the config by running ./configuration.py

7. Create the waf symlinks using the PebbleSDK:

* cd /path/to/PebbleSDK/Pebble/tools
* ./create\_pebble\_project.py --symlink-only ../sdk /path/to/authenticator

8. Run ./waf configure 

9. Build the .pbw file with ./waf build  (copy build/authenticator.pbw to your phone and install)

8. The Pebble phone app should show a watch app called 'Authenticator [label]'

10. You should be able to scroll through watch faces and see the code displayed

11.  To install MORE codes, remove / comment out the first one, and replace it with a new label and secret key

12.  Re-run ./waf build  and install the new .pbw file with your phone.  It should show up as
a new watch face with a different name.

The above is assuming you have the Pebble SDK installed and configured to compile watch apps.
If not, review: http://developer.getpebble.com/1/01_GetStarted/01_Step_2
