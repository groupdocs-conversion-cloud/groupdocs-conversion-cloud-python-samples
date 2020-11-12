# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert word processing document into html document
class ConvertToHtml:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "WordProcessing/four-pages.docx"
        settings.format = "html"
        convertOptions = groupdocs_conversion_cloud.HtmlConvertOptions() 
        convertOptions.from_page = 1
        convertOptions.pages_count = 1
        convertOptions.fixed_layout = True
        convertOptions.fixed_layout_show_borders = True
        settings.convert_options = convertOptions       
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        