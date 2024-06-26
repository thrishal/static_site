from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print("hello world")
    textnode1 = TextNode("This is 1", "bold", "https://www.youtube.com")
    print(textnode1)
    htmlnode1 = HTMLNode("div", "hello world", None, {"class": "greeting", "href": "https://boot.dev"})
    print(htmlnode1.props_to_html())
    leafnode1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leafnode1.to_html())

    parentnode1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

    print(parentnode1.to_html()) 



main()