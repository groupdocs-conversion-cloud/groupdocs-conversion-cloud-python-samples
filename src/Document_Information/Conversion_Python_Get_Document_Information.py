# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities

class Conversion_Python_Get_Document_Information:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_InfoApi_Instance()
        
        try:
            request = groupdocs_conversion_cloud.GetDocumentMetadataRequest()
            request.storage_name = Common_Utilities.myStorage;
            request.file_path = "conversions\\password-protected.docx"
			
            response = api.get_document_metadata(request)

            print("Expected response type is DocumentMetadata: " + str(len(response)))
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))