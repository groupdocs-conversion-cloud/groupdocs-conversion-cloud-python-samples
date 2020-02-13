# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert pdf document to word processing with advanced options
class ConvertPdfAndFlattenAllFields:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Pdf/sample.pdf"
        settings.format = "docx"

        loadOptions = groupdocs_conversion_cloud.PdfLoadOptions()
        loadOptions.flatten_all_fields = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        
