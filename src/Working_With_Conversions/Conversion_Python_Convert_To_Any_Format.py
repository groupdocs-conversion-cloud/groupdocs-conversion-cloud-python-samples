# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities


class Conversion_Python_Convert_To_Any_Format:
    
    @classmethod
    def Run(self, strformat, convertOptions):
        # Create instance of the API
        api = Common_Utilities.Get_ConversionApi_Instance()
        
        try:
            settings = groupdocs_conversion_cloud.ConvertSettings()
            settings.storage_name = Common_Utilities.myStorage;
            settings.file_path = "conversions\\sample.docx"
            settings.format = strformat
            settings.convert_options = convertOptions
            settings.output_path = "converted\\" + strformat
        
            request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
            response = api.convert_document(request)

            print("Document converted successfully: " + str(response))
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
