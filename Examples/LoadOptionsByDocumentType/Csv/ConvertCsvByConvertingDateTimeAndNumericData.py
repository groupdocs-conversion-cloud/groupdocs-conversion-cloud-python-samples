# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert csv document into pdf document
class ConvertCsvByConvertingDateTimeAndNumericData:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_config(Common.GetConfig())
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Spreadsheet/sample.csv"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.CsvLoadOptions()
        loadOptions.convert_date_time_data = True
        loadOptions.convert_numeric_data = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        
