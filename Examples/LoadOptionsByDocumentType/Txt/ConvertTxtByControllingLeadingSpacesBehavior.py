# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert a txt document to pdf with advanced options
class ConvertTxtByControllingLeadingSpacesBehavior:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Text/sample.txt"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.TxtLoadOptions()
        loadOptions.leading_spaces_sptions = "ConvertToIndent"
        loadOptions.detect_numbering_with_whitespaces = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        
