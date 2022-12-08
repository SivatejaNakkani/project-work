import sys

class Main:
    def run_db(self):
        import DB_implementation
    
    def run_ping_device(self):
        import ping_device
        
    def run_ServerARP1(self):
        import ServerARP1
        
    def run_ClientARP1(self):
        import ClientARP1
        
def exitprogram():
    sys.exit("system exiting")
    
def printerror():
    print("Invalid option entered")
    
main = Main()
def run():
    menu={
    1:main.run_db,
    2:main.run_ping_device,
    3:main.run_ServerARP1,
    4:main.run_ClientARP1,
    5:exitprogram
    }
    while True:
        print("\n 1:Establish DataBase connection\n2:ping a device\n3:run ARP server\n4:run ARP client\n5:Exit Program\nEnter your choice?",end='')
        try :
            choice = int(input())
        except ValueError:
            print("Please enter a valid input!")
        menu.get(choice,printerror)()
run()