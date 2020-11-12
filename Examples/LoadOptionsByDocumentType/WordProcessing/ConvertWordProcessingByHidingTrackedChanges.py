# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert a word-processing document to pdf with advanced options
class ConvertWordProcessingByHidingTrackedChanges:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "WordProcessing/with_tracked_changes.docx"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.WordProcessingLoadOptions()
        loadOptions.hide_word_tracked_changes = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        