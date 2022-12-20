# Banner File
import datetime
import time

import System.Requirements.FTD

Launcher = '''
  _                            _               
| |                          | |              
| |     __ _ _   _ _ __   ___| |__   ___ _ __ 
| |    / _` | | | | '_ \ / __| '_ \ / _ \| __|
| |___| (_| | |_| | | | | (__| | | |  __/ |   
\_____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|    
================================================
'''
try:
    import User.UserProfile

    User = User.UserProfile.Username
except:
    pass
FunctionList =f'''
|  |   SSSSSSSSSSSSSSS                                        AAA         TTTTTTTTTTTTTTTTTTTTTTT
|  | SS:::::::::::::::S                                      A:::A        T:::::::::::::::::::::T
|  |S:::::SSSSSS::::::S                                     A:::::A       T:::::::::::::::::::::T
|  |S:::::S     SSSSSSS                                    A:::::::A      T:::::TT:::::::TT:::::T
|  |S:::::S      wwwwwww           wwwww           wwwwwwwA:::::::::A     TTTTTT  T:::::T  TTTTTT
|  |S:::::S       w:::::w         w:::::w         w:::::wA:::::A:::::A            T:::::T        
|  | S::::SSSS     w:::::w       w:::::::w       w:::::wA:::::A A:::::A           T:::::T        
|  |  SS::::::SSSSS w:::::w     w:::::::::w     w:::::wA:::::A   A:::::A          T:::::T        
|  |    SSS::::::::SSw:::::w   w:::::w:::::w   w:::::wA:::::A     A:::::A         T:::::T        
|  |       SSSSSS::::Sw:::::w w:::::w w:::::w w:::::wA:::::AAAAAAAAA:::::A        T:::::T        
|  |            S:::::Sw:::::w:::::w   w:::::w:::::wA:::::::::::::::::::::A       T:::::T        
|  |            S:::::S w:::::::::w     w:::::::::wA:::::AAAAAAAAAAAAA:::::A      T:::::T        
|  |SSSSSSS     S:::::S  w:::::::w       w:::::::wA:::::A             A:::::A   TT:::::::TT      
|  |S::::::SSSSSS:::::S   w:::::w         w:::::wA:::::A               A:::::A  T:::::::::T      
|  |S:::::::::::::::SS     w:::w           w:::wA:::::A                 A:::::A T:::::::::T      
|  | SSSSSSSSSSSSSSS        www             wwwAAAAAAA                   AAAAAAATTTTTTTTTTT
===============================================================================================
|/|             What's up {User}!       
|/|             Today: {datetime.datetime.today()}
|/|             From The Devs! {System.Requirements.FTD.Version}
===============================================================================================
|/|             |-------------------------------|-------------------------------| 
|/|             | 1:: SwAT Information          | 5:: Package Launcher          |
|/|             |-------------------------------|-------------------------------|
|/|             | 2:: Manual Cache management   | 6:: Package Uninstaller       |
|/|             |-------------------------------|-------------------------------|
|/|             | 3:: Package Settings          | 7:: DEV                       |
|/|             |-------------------------------|-------------------------------|
|/|             | 4:: Package Compiler          | 8:: Exit                      |
|/|             |-------------------------------|-------------------------------|
'''
Function_Settings = '''        
|  |                        Settings
======================================================
|  |                |1 | Info
|  |                |==================================
|  |                |2 | User Specific Settings
|  |                |===================================
|  |                |3 | System Settings
|  |                |===================================
'''

