# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities

class Conversion_Python_Download_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_conversion_cloud.DownloadFileRequest("conversions\\one-page.docx", Common_Utilities.myStorage)
            response = api.download_file(request)
            
            print("Expected response type is Stream: " + str(len(response)))
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))