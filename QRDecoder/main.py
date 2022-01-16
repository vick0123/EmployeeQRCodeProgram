import qrcode
import cv2
import employee

def menu():
  f = input("Enter A to Scan QR Code \n"
          "Enter B Create QR code for Employee \n"
          "Enter C to exit: \n")
  f=f.lower()
  return f
def main():
    
    x=menu()
    while True:
            #———————————Scan QR Code———————————
            if x=='a':
                d=cv2.QRCodeDetector()
                val,points,straight_qrcode = d.detectAndDecode(cv2.imread("employee.png"))

                variables=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1','2','3','4','5','6','7','8','9','0']

                print("\nEmployee Information: \n")

                for i in val:
                    if i==",":
                        print("\n")
                    else:
                        for x in variables:
                            if i== x:
                                print(i, end ="")
                print('\n')

            #———————————Create QR Code———————————
            elif x=='b':
                name = input ('\nEnter the name: ')
                department = input('\nEnter the Department: ')
                id = input ('\nEnter the ID number: ')

                worker = employee.Employee(name, id, department)
                
                data = worker.get_name(),worker.get_department(),worker.get_number()
                
                img=qrcode.make(data)
                img.save('/Users/vivekpatel/Desktop/YearUp/QRDecoder/employee.png')


                print("\nQR Code for Employee 1 in QRDecoder Folder.\n")
            
            #———————————End Program———————————
            elif x=='c':
                break
            else:
                print("Try Again")

            x=menu()
    
main()