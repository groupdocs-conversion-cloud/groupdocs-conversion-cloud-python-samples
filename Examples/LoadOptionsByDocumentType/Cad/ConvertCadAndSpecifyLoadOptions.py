# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert cad document into pdf document
class ConvertCadAndSpecifyLoadOptions:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Cad/Sample.dwg"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.CadLoadOptions()
        loadOptions.width = 1920
        loadOptions.height = 1080

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        