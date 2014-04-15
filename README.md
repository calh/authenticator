SDK 2.0 Authenticator Watch Face
=============

This is a Google Authenticator (Time-Based One-Time Password generator) **watch face app** for the Pebble.

**The Pebble [1.0 SDK version is here](https://github.com/calh/authenticator/tree/SDK1)**

Features
--------

A few main features which make my version different from the other [forks of Authenticator](https://github.com/IEF/authenticator/network/members):
* Pebble watch face, not an app
  * Quick to access to two-factor codes
  * One app per code
* Secret key is still compiled into the app
  * Compile and distribute .pbw binaries to end users of a website
  * Easy for novice users that aren't able to set up or configure a Pebble app
* Long labels adjust the position of the token
* Two-factor code uses [NotCourierSans](http://openfontlibrary.org/en/font/notcouriersans) from the Open Font Library
  * Monospaced Courier-copy font is easy to read
  * The code is split into two chunks of 3 digits separated by some space to assist with chunking the information in your noodle.  
  * This helps you quickly retain the full 6 digits in short term memory and regurgitate them in the text input field
* Time zone information is retrieved from the phone and cached in local storage on the Pebble
  * Default time zone is specified as a compile-time option  
  * App startup reads from the local storage cache, or compiled timezone for **quick** startups

<img src="screenshots/short_label_example.png" /> &nbsp;&nbsp;
<img src="screenshots/long_label_example.png" />

This is slightly different from the IEF version, which is a standard watch app.  A watch app 
must be accessed from the main menu.  Viewing a two-factor auth code then requires at least 
6 button presses, along with scrolling through multiple accounts if they are defined.

A watch face app installs the Authenticator screen along side your other watch faces.  A 
minimum of 1 button press is needed to view a two-factor auth code.

The caveat to this convenience is that you can only display one code per watch app.  The
configureation.py script creates a new UUID for each app based on the secret key defined
in configuration.txt.

When the watch face is initialized, the time zone is retrieved via Pebble JS on the phone.  
If the time zone is diferent from the compile-time option, the new timezone is saved in 
a local storage cache on the Pebble.  When the app is initialized again, the local cache is 
used instead of the compile-time option.  This ensures that the correct code is displayed
immediately after switching to the app.  (It takes a few seconds for Pebble JS to start up)

Since this watch face app is meant to be switched to, then switch back to your main watch face,
the time zone should always be correct.  (Re-reading the phone time zone every hour shouldn't be
necessary)

Compile and Installation
------------------------

If you haven't already, install and setup Pebble SDK 2.0: https://developer.getpebble.com/2/getting-started/

To configure the application you need to create a configuration.txt file.

1. Copy configuration-sample.txt to configuration.txt

2. Set your timezone in configuration.txt - it's near the top, labelled 'tz'.  These are
integer offsets from UTC.  (Ex:  Central Daylight Savings is -5)

3. Let's say you have secret key AXIMZYJXITSIOIJVNXOE76PEJQ 
When setting up two-factor auth on most sites, find a 'show key' option when presented with a QR code.

4. add it to the end of configuration.txt, following the example in the format 
label:secret
(You may add only **one** key)  The label is any custom string up to 50 characters to describe this account.

5. Generate the config by running `./configuration.py`  This creates a new appinfo.json file, and src/configuration.h file

6. Build the authenticator.pbw file with `pebble build`

7. Install the authenticator.pbw file using your phone
* Using the Pebble SDK
 * Connect your phone to the same local wifi network that your workstation is on
 * On the phone's Pebbble app, go to Configuration -> Developer Options and check **Enable Developer Connection**
 * On the main screen, your IP address is shown below the **Connected** button.  Use that in the command below
 * Run this command: `pebble install --phone 192.168.x.x` 
* Copying the file manually
 * Attach the build/authenticator.pbw file to an email, send it to your phone, and download the attachment.  
   The Pebble app should pick up the .pbw extension and install it to the watch.
 * Or copy the build/authenticator.pbw file to your phone and open it with a file viewer

8. The Pebble phone app should show a watch app named with the label provided in configuration.txt

10. You should be able to scroll through watch faces and see the code displayed

11.  To install MORE codes, remove / comment out the first code in configuration.txt, 
and replace it with a new label and secret key.

12.  Re-run `./configuration.py`

13.  Re-run `pebble build`  and install the new .pbw file with your phone.  It should show up as
a new watch face with a different name.

**PRO-TIP**: Checkout [PebbleBits](http://pebblebits.com/firmware/) to create a custom firmware for your Pebble that removes the lame default watch faces!  If you install only the faces you actively use, switching to your two-factor code is much quicker.

Credits 
-------

The [Authenticator network](https://github.com/IEF/authenticator/network/members) is growing pretty large, as each developer has their own tweaks and customizations.  Search around for the features you like.  Credits for my version are listed below.  Thanks to everyone for contributing to this amazing Pebble app!

* [IEF](https://github.com/IEF/authenticator)
* [pokey9000](https://github.com/pokey9000/twostep)
* [rigel314](https://github.com/rigel314/pebbleAuthenticator)
* [DidierA](https://github.com/DidierA/authenticator)
* [dmchurch](https://github.com/dmchurch/authenticator)
 


