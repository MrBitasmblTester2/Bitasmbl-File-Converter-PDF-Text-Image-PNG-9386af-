from .conversion_service import ConversionService
class PdfImageAdapter:
    def __init__(self):
        self.svc = ConversionService()
    def handle(self, src_path: str, mime: str) -> str:
        raise NotImplementedError