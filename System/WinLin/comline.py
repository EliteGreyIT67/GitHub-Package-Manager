import datetime
global os
import sys
import time
import User.UserProfile

global cwd

cwd = User.UserProfile.SourceDirectory


def checkpoint():
    import os
    import time
    os.chdir(User.UserProfile.SourceDirectory)
    time.sleep(0)
    print('\n' * 100)
    import importlib
    import System.WinLin.Banner

    importlib.reload(System.WinLin.Banner)

    try:
        with open(
                f'{User.UserProfile.SourceDirectory}System/.Cache/System/Version.py',
                'r',
        ) as ver:
            version = ver.read()
    except:
        version = 'Version Cannot Be Read'

    import datetime

    print(
        f"""
\033[1m ______                ______             
    |          |   |      |   |      |\ /| 
    | +-       |-+-|      |-+-       | + | 
    |   |      |   |      |          |   | 
     ---  \033[0m                                                                                                                                                                                                                                                                                                                    
==========================================
What's up \033[1m\033[1m{User.UserProfile.Username}!\033[0m      
Today: {datetime.datetime.today()}
From The Devs! {version}Check out the GUI it's option 9!
==========================================="""
    )

    print(System.WinLin.Banner.FunctionList)
    Value = input('Enter a value to continue: ')

    try:
        Value = int(Value)
    except:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest input error', Pol=1)
        checkpoint()

    if Value == 1:  # System info
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information', Pol=1)

            import System.WinLin

            print(System.WinLin.Information.SwAT)
            t = input('\n\nHit enter to continue: ')
            print('\n\n')
            import System.WinLin

            print(System.WinLin.FTD.dev_message)
            t = input('\n\nHit enter to continue: ')

        except:


            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information * Failed', Pol=0)

            os.chdir(User.UserProfile.SourceDirectory)

        time.sleep(0)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 2:  # mcm
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache', Pol=1)

            import System.WinLin.Functions.Cache

            exec('System.WinLin.Functions.Cache')

        except:

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache * Failed', Pol=0)


            os.chdir(User.UserProfile.SourceDirectory)
            checkpoint()

    elif Value == 3:  # settings
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Settings', Pol=1)

            import System.WinLin

            print(System.WinLin.Banner.Function_Settings)
            import System.WinLin.Functions.Settings

            System.WinLin.Functions.Settings.main()

        except:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Settings * Failed', Pol=0)


        time.sleep(3)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 4:
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageInstaller', Pol=1)

            import System.WinLin.Functions.PackageInstaller

            System.WinLin.Functions.PackageInstaller.main()

        except:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'FunctionRequest = PackageInstaller * Failed', Pol=0
            )


        time.sleep(3)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 5:
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageActivator', Pol=1)
            import System.WinLin.Functions.PackageActivator

            System.WinLin.Functions.PackageActivator.All()

        except:

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'FunctionRequest = PackageActivator * Failed', Pol=0
            )

        time.sleep(3)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 6:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = PackageUninstaller', Pol=1)

        import System.WinLin.Functions.Uninstall

        Input = input('Enter Password To Use Uninstaller: ')
        try:
            import System.WinLin.Password as PS

            PS.Password(Event='Uninstall', Input=Input)

            print('Launching Uninstaller')
            time.sleep(1.54)
            print('\n' * 100)
            EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
            System.WinLin.Functions.Uninstall.All()
        except:
            Input = input('Enter Password To Use Uninstaller: ')
            try:
                import System.WinLin.Password as PS

                PS.Password(Event='Uninstall', Input=Input)

                print('Launching Uninstaller')
                time.sleep(1.54)
                print('\n' * 100)
                EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
                System.WinLin.Functions.Uninstall.All()
            except:
                print('Final Attempt')
                Input = input('Enter Password To Use Uninstaller: ')
                try:
                    import System.WinLin.Password as PS

                    PS.Password(Event='Uninstall', Input=Input)

                    print('Launching Uninstaller')
                    time.sleep(1.54)
                    print('\n' * 100)
                    EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
                    System.WinLin.Functions.Uninstall.All()

                except:
                    EV.NewEvent(event=f'Password Failed Multiple Times', Pol=1)

        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 8:
        print(f'Peace Out {User.UserProfile.Username}!')
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'User Logged Out', Pol=0)
        exit(0)

    elif Value == 7:
        print(
            """
    |=#BRICK=|
    |0 > LOCK|
    |++++++++|
    |1 > READ|
    |++++++++|
    |2 > LIST|
    |++++++++|
    |3 > FILE|
    |++++++++|
    |4 > DELL|
    |++++++++|"""
        )
        try:
            f = int(input('Enter Function: '))
        except:
            pass
        try:
            import test
            import System.WinLin.Password as ps

            try:
                ps.Password(
                    Event='FILE',
                    Input=input('Enter password to use FileCache: '),
                )
            except:
                print('password incorrect')
                sys.exit(0)
            if f == 2:
                import Password

                print(
                    Password.main(
                        message=None,
                        password=User.UserProfile.Password,
                        f=f,
                        address=None,
                    )
                )
                time.sleep(4)
            if f == 0:
                message = input('Enter The Data You Would Like To Lock: ')
                time.sleep(0.5)
                input()
                address = input('Name Of Storage: ')
                Input = input('Enter FileLock Password: ')
                key = input('Enter Key: ').encode()
                import hashlib
                import uuid

                UUID = uuid.uuid1()

                UserID = os.getlogin()

                salt = '103lk423'

                UUID = str(f'{UUID}')

                uuidToken = UUID[30:]
                DefaultTkn = User.UserProfile.uuid1

                Password = f'{Input}{uuidToken}{UserID}{key}'

                password = Password + salt
                hashed = hashlib.md5(password.encode())
                Password = hashed.hexdigest()

                print(Password)

                print(
                    Password.main(
                        message, password=Password, f=f, address=address
                    )
                )
            if f == 3:
                File = input('FilePath To Encrypt: ')
                FileName = input('Name to save to: ')
                address = f'{FileName}'
                Fe = open(File, 'r')
                message = Fe.read()
                Input = input('Enter FileLock Password: ')
                key = input('Enter Key: ').encode()
                import hashlib
                import uuid

                UUID = uuid.uuid1()

                UserID = os.getlogin()

                salt = '103lk423'

                UUID = str(f'{UUID}')

                uuidToken = UUID[30:]
                DefaultTkn = User.UserProfile.uuid1

                Password = f'{Input}{uuidToken}{UserID}{key}'

                password = Password + salt
                hashed = hashlib.md5(password.encode())
                Password = hashed.hexdigest()

                import Password

                Password.main(message, password=Password, f=0, address=address)
            if f == 4:
                address = input('Storage To Wipe: ')
                open(
                    f'{User.UserProfile.SourceDirectory}System/.Cache/User/{address}',
                    'w',
                )
            elif f == 1:
                address = input('Name Of Storage: ')
                Input = input('Enter FileLock Password: ')
                key = input('Enter Key: ').encode()
                import hashlib
                import uuid

                UUID = uuid.uuid1()

                UserID = os.getlogin()

                salt = '103lk423'

                UUID = str(f'{UUID}')

                uuidToken = UUID[30:]
                DefaultTkn = User.UserProfile.uuid1

                Password = f'{Input}{uuidToken}{UserID}{key}'

                password = Password + salt
                hashed = hashlib.md5(password.encode())
                Password = hashed.hexdigest()
                import Password

                print(
                    Password.main(
                        message=None, password=Password, f=f, address=address
                    )
                )
                input('enter to continue')

        except:
            pass

        checkpoint()

    elif Value == 0:
        pass
    else:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = InvalidEntry', Pol=1)




checkpoint()
