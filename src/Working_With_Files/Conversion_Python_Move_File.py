# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities

class Conversion_Python_Move_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_conversion_cloud.MoveFileRequest("conversions\\one-page.docx", "conversions1\\one-page.docx", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.move_file(request)
            
            print("Expected response type is Void: 'conversions/one-page.docx' file moved to 'conversions1/one-page.docx'.")
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))