import groupdocs_conversion_cloud
import glob
import os

class Common:

    # This properties are set from main class
    app_sid = None
    app_key = None
    myStorage = None
    
    @classmethod  
    def UploadSampleFiles(cls):
        
        # api initialization
        storageApi = groupdocs_conversion_cloud.StorageApi.from_keys(cls.app_sid, cls.app_key)
        fileApi = groupdocs_conversion_cloud.FileApi.from_keys(cls.app_sid, cls.app_key)

        # upload sample files
        for filename in glob.iglob("Resources/**/*.*", recursive=True):
            destFile = filename.replace("Resources\\", "", 1)            
            fileExistsResponse = storageApi.object_exists(groupdocs_conversion_cloud.ObjectExistsRequest(destFile))
            if not fileExistsResponse.exists:                                
                fileApi.upload_file(groupdocs_conversion_cloud.UploadFileRequest(destFile, filename))
                print("Uploaded file: "+ destFile)
