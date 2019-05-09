# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities

class Conversion_Python_Delete_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_conversion_cloud.DeleteFolderRequest("conversions\\conversions1", Common_Utilities.myStorage, True)
            api.delete_folder(request)
            
            print("Expected response type is Void: 'conversions/conversions1' folder deleted recursively.")
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))