# USB Phantom

USB Phantom is a tool that makes it easier to use the Digispark board. You can choose which script code you want to be displayed to you using the available options and choices.

## install 
```bash
   git clone https://github.com/soheil-vanaee/usb-phantom.git
   cd usb-phantom
   python3 USB-Phantom.py
```

## Usage

```bash
   _   ,--()
  ( )-'-.------|>    [soheil vanaee] - [insta: soheil_vanaee]
    "     `--[]        [twitter: SoehilVanaee] - [hacklido: S0431L] 

              
[1]: Create Account    [2]: DNS Poisoner 
[3]: Keylogger         [4]: Fake update 
[5]: Talker            [6]: Wallpaper Changer 
[7]: Window Jammer     [8]: Silly Mouse 

Choose script => 
```

Feel free to modify the text formatting or add any additional information as needed.


For example, if I choose option 4, it returns the following script:

```bash 

██    ██ ███████ ██████      ██████  ██   ██  █████  ███    ██ ████████  ██████  ███    ███ 
██    ██ ██      ██   ██     ██   ██ ██   ██ ██   ██ ████   ██    ██    ██    ██ ████  ████ 
██    ██ ███████ ██████      ██████  ███████ ███████ ██ ██  ██    ██    ██    ██ ██ ████ ██ 
██    ██      ██ ██   ██     ██      ██   ██ ██   ██ ██  ██ ██    ██    ██    ██ ██  ██  ██ 
 ██████  ███████ ██████      ██      ██   ██ ██   ██ ██   ████    ██     ██████  ██      ██ 


#include "DigiKeyboard.h"
void setup() {
    // Empty
}

void loop() {
    DigiKeyboard.delay(2000);
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
    DigiKeyboard.delay(3000);
    DigiKeyboard.print("http://fakeupdate.net/win10ue");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(2000);
    DigiKeyboard.sendKeyStroke(KEY_F11);
    for(;;) { /* Empty */ }
}
```
