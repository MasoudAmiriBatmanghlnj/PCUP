from art import*
print("======================================================\nWelcome to Program for creating usernames and passwords.\n======================================================")
tprint('PCUP')
print('full Name:Program for creating usernames and passwords.')
print('Trial Version')
print('++++++++++OnSet++++++++++')
class PCUP:
    def __init__(self,username,password):
        self.u=username
        self.p=password
    def Username_Password(path):
        username=input("Pick a username:")
        password=input("Pick a password:")
        username_confirm=input('Please confrim your username:')
        password_confirm=input("Please confrim your password:")
        while True:
            if username==username_confirm:
                print('Username confirmed ^U^.')
                if  password==password_confirm:
                    print('Password confirmed ^U^.')
                    Save=input('Please enter the file storage along with the file name:')
                    #Try: To check if this file already exists👇👇👇
                    try:
                        import os.path
                        filepath=Save
                        if os.path.isfile(filepath):
                            print("The item file already exists.",filepath)
                            continue
                        else:
                            print('This is a new file')
                            text_file=open(Save,"a")
                            text_file.write("\n"),text_file.write(username),text_file.write("\n"),text_file.write(password),
                            text_file.close()
                            print('The file you requested was saved here:',Save)
                            print("Your Account has deen setup^_^")
                            break
                    except:
                        pass
                    #+++++++++++++++++++++++Finish Trying+++++++++++++++++++++++
            else:
                print("Your username and password don,t match.Please try again(._.`)")
                username_confirm=input('Please confrim your username:')
                password_confirm=input("Please confrim your password:")
UP=PCUP
UP.Username_Password('path')