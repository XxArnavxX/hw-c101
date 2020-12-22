import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def fileUpload(self, file_from, file_to):
        db = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        db.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.AnwwtCZ7lww80RueHkxI6IL1s98_YjkeJ-HpyWJN7vU9zu8y4lwgwEKVcreHjDCHIRJm8pAQfLeHZgVi4FBo3S2CwtnQH71pJBDnP88VJR35zb6c8aqr0FsmlWZPI2-cAM8KyXk'
    transfer1 = TransferData(access_token)
    file_from = input("type file you want to upload: ")
    file_to = input("enter path where you want to upload to dropbox: ")
    transfer1.fileUpload(file_from, file_to)


main()