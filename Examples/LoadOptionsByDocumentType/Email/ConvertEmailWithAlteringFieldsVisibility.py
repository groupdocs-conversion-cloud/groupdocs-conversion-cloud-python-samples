# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert msg document into pdf document
class ConvertEmailWithAlteringFieldsVisibility:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Email/sample.msg"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.EmailLoadOptions()
        loadOptions.display_header = False
        loadOptions.display_from_email_address = False
        loadOptions.display_to_email_address = False
        loadOptions.display_email_address = False
        loadOptions.display_cc_email_address = False
        loadOptions.display_bcc_email_address = False

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        