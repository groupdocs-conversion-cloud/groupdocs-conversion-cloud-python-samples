# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert word processing document into pdf document
class ConvertToPdf:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "WordProcessing/password-protected.docx"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.WordProcessingLoadOptions()
        loadOptions.password = "password"
        convertOptions = groupdocs_conversion_cloud.PdfConvertOptions()
        convertOptions.center_window = True
        convertOptions.compress_images = False
        convertOptions.display_doc_title = True
        convertOptions.dpi = 1024
        convertOptions.fit_window = False
        convertOptions.from_page = 1
        convertOptions.grayscale = False
        convertOptions.image_quality = 100
        convertOptions.linearize = False
        convertOptions.margin_top = 5
        convertOptions.margin_left = 5
        convertOptions.password = "password"
        convertOptions.unembed_fonts = True
        convertOptions.remove_unused_streams = True
        convertOptions.remove_unused_objects = True
        convertOptions.remove_pdfa_compliance = False

        settings.load_options = loadOptions
        settings.convert_options = convertOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        