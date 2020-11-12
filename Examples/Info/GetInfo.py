# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to get document info
class GetInfo:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_conversion_cloud.InfoApi.from_config(Common.GetConfig())
        request = groupdocs_conversion_cloud.GetDocumentMetadataRequest()
        request.file_path = "WordProcessing/four-pages.docx"
        result = infoApi.get_document_metadata(request)        
        print("Page count = " + str(result.page_count))