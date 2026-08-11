def program_start():
    while True:
        confirmation = input('TYPE "START" TO BEGIN OR "STOP" TO END: ')

        if confirmation.lower() == "start":
            print('STARTING PROGRAM')
            print('DO NOT LAUNCH')
            print('CONFIGURING SETTINGS')
            return True
        elif confirmation.lower() == "stop":
            print('STOPPING PROGRAM')
        else: 
            print('WRONG INPUT ')
            continue

