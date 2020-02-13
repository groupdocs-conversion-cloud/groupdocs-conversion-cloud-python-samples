# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert word processing document into pdf document with adding watermark
class AddWatermark:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "WordProcessing/four-pages.docx"
        settings.format = "pdf"
        settings.convert_options = groupdocs_conversion_cloud.PdfConvertOptions()

        watermark = groupdocs_conversion_cloud.WatermarkOptions()                
        watermark.text = "Sample watermark"
        watermark.color = "Red"
        watermark.width = 100
        watermark.height = 100
        watermark.background = True
        
        settings.watermark_options = watermark
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        