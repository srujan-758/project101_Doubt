import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
 def __init__(self,access_token):
   self.access_token=access_token

 def upload_file(self,file_from,file_to):  
  dbx=dropbox.Dropbox(self.access_token)  

  print("filesUploaded") 
  for root, files in os.walk(file_from):
   print("filesUploaded") 
   for filename in files:
    local_path= os.path.join(root, filename)
    print("filesUploaded") 
    relative_path= os.path.relpath(local_path, file_from)
    print("filesUploaded") 
    dropbox_path= os.path.join(file_to, relative_path) 
    print("filesUploaded")    

    with open(local_path, 'rb') as f:
     print("filesUploaded")   
     dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))   


def main():
 access_token='sl.A52Ly3S9M0h3tNmbkfwbq_kjnSmRtosDBReF81Ts9qDB6pas3FpxmoU2t9MAZfxVs72hLAa03nQ2haGuaEmCeMgl52FZHFZZsQ_U_aiRLEKLq0W4vou8j4l1mj0PidZitFFTbqisAzYY'
 transferData= TransferData(access_token)

 file_from= input("Enter the file path to transfer:")
 file_to=input("Enter the path to Dropbox to upload the file:")

 transferData.upload_file(file_from,file_to)
 print("File has been moved")


main()
