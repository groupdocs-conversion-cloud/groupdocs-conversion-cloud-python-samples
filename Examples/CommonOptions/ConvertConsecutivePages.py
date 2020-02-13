# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert consecutive pages from word processing document into pdf document
class ConvertConsecutivePages:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "WordProcessing/four-pages.docx"
        settings.format = "pdf"
        convertOptions = groupdocs_conversion_cloud.PdfConvertOptions()
        convertOptions.from_page = 2
        convertOptions.pages_count = 2
        settings.convert_options = convertOptions
        settings.output_path = "converted/two-pages.pdf"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        