text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode2: object) -> bool:
        if (self.text == TextNode2.text) and (self.text_type == TextNode2.text_type) and (self.url == TextNode2.url):
            return True
        
    def __repr__(self) -> str:
        TEXT = self.text
        TEXT_TYPE = self.text_type
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"
