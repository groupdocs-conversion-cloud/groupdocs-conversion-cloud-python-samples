# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert msg document into pdf document
# and replace field labels to custom values
class ConvertEmailWithFieldLabels:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Email/sample.msg"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.EmailLoadOptions()
        fieldLabel = groupdocs_conversion_cloud.FieldLabel()
        fieldLabel.field = "From"
        fieldLabel.label = "Sender"
        loadOptions.field_labels = [fieldLabel]

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
   