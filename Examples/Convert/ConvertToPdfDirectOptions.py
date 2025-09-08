# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert document without using cloud storage
class ConvertToPdfDirectOptions:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare request
        load_options = groupdocs_conversion_cloud.WordProcessingLoadOptions()
        load_options.format = "docx"
        load_options.password = "password"
        request = groupdocs_conversion_cloud.ConvertDocumentDirectRequest("pdf", "Resources\\WordProcessing\\password-protected.docx", None, None, load_options)

        # Convert
        result = apiInstance.convert_document_direct(request)

        print("Document converted: " + result)
        