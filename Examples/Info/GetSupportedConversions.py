# Import modules
import groupdocs_conversion_cloud
from Common import Common

#  This example demonstrates how to obtain all supported document conversions
class GetSupportedConversions:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_conversion_cloud.InfoApi.from_config(Common.GetConfig())
        result = infoApi.get_supported_conversion_types(groupdocs_conversion_cloud.GetSupportedConversionTypesRequest())
        print("Formats count: " + str(len(result)))