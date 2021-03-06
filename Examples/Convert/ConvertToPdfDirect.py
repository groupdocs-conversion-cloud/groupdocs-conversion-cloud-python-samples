# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert document without using cloud storage
class ConvertToPdfDirect:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare request
        request = groupdocs_conversion_cloud.ConvertDocumentDirectRequest("pdf", "Resources\\WordProcessing\\four-pages.docx")

        # Convert
        result = apiInstance.convert_document_direct(request)

        print("Document converted: " + result)
        