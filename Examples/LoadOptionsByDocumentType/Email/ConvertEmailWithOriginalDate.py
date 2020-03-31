# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert msg document into pdf document with original date
class ConvertEmailWithOriginalDate:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Email/sample.msg"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.EmailLoadOptions()
        loadOptions.preserve_original_date = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
   