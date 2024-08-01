# Import modules
import groupdocs_conversion_cloud
import time
from Common import Common

# This example demonstrates how to convert document without using cloud storage asyncronously
class ConvertToPdfDirectAsync:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.AsyncApi.from_config(Common.GetConfig())
        
        # Prepare request
        request = groupdocs_conversion_cloud.StartConvertRequest("pdf", "Resources\\WordProcessing\\four-pages.docx")

        # Convert
        operation_id = apiInstance.start_convert(request)
        print("Operaion ID: " + operation_id)

        while (True):
            time.sleep(1)
            result = apiInstance.get_operation_status(groupdocs_conversion_cloud.GetOperationStatusRequest(operation_id))
            if (result.status == "Finished"):
                response = apiInstance.get_operation_result(groupdocs_conversion_cloud.GetOperationResultRequest(operation_id))
                print("Document converted: " + response)
                break
            elif (result.status == "Failed"):
                print("Operation failed: " + result.error)
                break
            else:
                print("Operation status: " + result.status)
        