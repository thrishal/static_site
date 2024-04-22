class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode1: object, TextNode2: object) -> bool:
        if (TextNode1.text == TextNode2.text) and (TextNode1.text_type == TextNode2.text_type) and (TextNode1.url == TextNode2.url):
            return True
        
    def __repr__(self) -> str:
        TEXT = self.text.upper()
        TEXT_TYPE = self.text_type.upper()
        URL = self.url.upper()
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"
