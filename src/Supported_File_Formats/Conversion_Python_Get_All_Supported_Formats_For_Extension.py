# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities

class Conversion_Python_Get_All_Supported_Formats_For_Extension:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ConversionApi_Instance()
        
        try:
            # Retrieve supported conversion types
            request = groupdocs_conversion_cloud.GetSupportedConversionTypesRequest("", Common_Utilities.myStorage, "xlsx")
            response = api.get_supported_conversion_types(request)
            
            # Print out supported conversion types
            print("Supported conversion types:")
            for fileformat in response:
                print('{0} to [{1}]'.format(fileformat.source_format, ', '.join(fileformat.target_formats))) 
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception when calling get_supported_conversion_types: {0}".format(e.message))