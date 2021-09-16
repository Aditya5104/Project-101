import dropbox
import os
from dropbox import files
from dropbox.files import WriteMode

class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for fileName in files:
                localPath=os.path.join(root,fileName)
                relativePath=os.path.relpath(localPath,file_from)
                dropboxpath=os.path.join(file_to,relativePath)
                with open(localPath,"rb") as f:
                    dbx.files_upload(f.read(),dropboxpath,mode=WriteMode("overwrite"))

def main():
    access_token="sl.A4lAhjsGyNOSLPLJVQhieCAxOLF7ulph4XEQ0ZsDxPnETgmPCk-Gc3ntACp-o55dWFAvuKpri1E1lnmsZrpfVM6Ya11s_jlL3zlDm-YUczDfP4N35seFK9YlVc1rjsgK6ry3-wE" 
    transferData=TransferData(access_token) 
    file_from=str(input("enter The Folder path to transfer: "))
    file_to=input("Enter The Folder Path To Uplaod To Dropbox")

    transferData.upload_file(file_from,file_to)
    print("File Has Been Moved")         
    
main()