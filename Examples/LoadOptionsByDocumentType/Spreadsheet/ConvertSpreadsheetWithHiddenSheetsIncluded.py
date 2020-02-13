# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert spreadsheet document into pdf with advanced options
class ConvertSpreadsheetWithHiddenSheetsIncluded:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Spreadsheet/with_hidden_sheet.xlsx"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.SpreadsheetLoadOptions()
        loadOptions.show_hidden_sheets = True
        loadOptions.one_page_per_sheet = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        