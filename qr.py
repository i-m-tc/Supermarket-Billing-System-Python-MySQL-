import cv2
from pyzbar.pyzbar import decode

from warnings import filterwarnings
filterwarnings(action='ignore')

def qr_code_scanner():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Loop until a QR code is detected
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Decode QR codes
        try:
            decoded_objs = decode(frame)
        except Exception as e:
            print("Error decoding QR code:", e)
            continue

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Check for QR codes
        if decoded_objs:
            for obj in decoded_objs:
                # print( obj.data.decode())
                # print(type(obj.data.decode()))
                qr_code_info=obj.data.decode()
                product_id=qr_code_info.split('-')[0]
                #print(product_id)
                return product_id

            break  # Break out of the loop once a QR code is detected

        # Wait for the 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    qr_code_scanner()