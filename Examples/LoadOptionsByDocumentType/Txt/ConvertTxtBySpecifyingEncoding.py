# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert a txt document to pdf with advanced options
class ConvertTxtBySpecifyingEncoding:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Text/sample.txt"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.TxtLoadOptions()
        loadOptions.encoding = "shift_jis"        

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        