import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(fileFrom, 'rb')
        dbx.files_upload(f.read(),fileTo)

def main():
    access_token = "sl.BKXsR7WnDesFMn4t4cPC-44oKE2MlDbBCSTXQdX5_bZ5_zyjLhbe1ErCshCuzWvBNvvMnCmdq6yR0r-VtH6UaHxMbhZKurK_2BBZe34K3o3NW3DhmHiPe0d5ymyn9v_sv1V3d_NAdecc"
    transferData=TransferData(access_token)
    fileFrom = input("File path to transfer: ")
    fileTo = input("Full Path to upload to Dropbox: ")
    transferData.upload_file(fileFrom,fileTo)
    print("File Moved")

main()
