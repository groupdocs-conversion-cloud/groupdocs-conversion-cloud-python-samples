# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities


class Conversion_Python_Convert_To_Pdf_Stream:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ConversionApi_Instance()
        
        try:
            settings = groupdocs_conversion_cloud.ConvertSettings()
            settings.storage_name = Common_Utilities.myStorage;
            settings.file_path = "conversions\\password-protected.docx"
            settings.format = "jpeg"
            
            loadOptions = groupdocs_conversion_cloud.DocxLoadOptions()
            loadOptions.password = "password"
            
            settings.load_options = loadOptions;
            
            convertOptions = groupdocs_conversion_cloud.PdfConvertOptions()
            convertOptions.bookmarks_outline_level = 1;
            convertOptions.center_window = True
            convertOptions.compress_images = False;
            convertOptions.display_doc_title = True
            convertOptions.dpi = 1024
            convertOptions.expanded_outline_levels = 1
            convertOptions.fit_window = False
            convertOptions.from_page = 1
            convertOptions.pages_count = 1
            convertOptions.grayscale = True
            convertOptions.headings_outline_levels = 1
            convertOptions.image_quality = 100
            convertOptions.linearize = False
            convertOptions.margin_top = 5
            convertOptions.margin_left = 5
            convertOptions.password = "password"
            convertOptions.unembed_fonts = True
            convertOptions.remove_unused_streams = True
            convertOptions.remove_unused_objects = True
            convertOptions.remove_pdfa_compliance = False
            convertOptions.height = 1024
            
            settings.convert_options = convertOptions
            settings.output_path = None  # leave OutputPath will result the output as document IOStream
            
            request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
            response = api.convert_document_download(request)

            print("Document converted successfully: " + str(len(response)))
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
