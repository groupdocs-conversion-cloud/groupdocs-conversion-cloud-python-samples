# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert document using custom font
class ConvertUsingCustomFont:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Presentation/uses-custom-font.pptx"
        settings.format = "pdf"        
        settings.output_path = "converted"
        settings.fonts_path = "font/ttf"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        