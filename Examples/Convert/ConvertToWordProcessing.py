# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert pdf document into word processing document
class ConvertToWordProcessing:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Pdf/sample.pdf"
        settings.format = "docx"

        loadOptions = groupdocs_conversion_cloud.PdfLoadOptions()
        loadOptions.password = ""
        loadOptions.hide_pdf_annotations = True
        loadOptions.remove_embedded_files = False
        loadOptions.flatten_all_fields = True

        settings.load_options = loadOptions
        settings.convert_options = groupdocs_conversion_cloud.DocxConvertOptions()
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        