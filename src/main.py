from textnode import TextNode
from htmlnode import HTMLNode

def main():
    print("hello world")
    textnode1 = TextNode("This is 1", "bold", "https://www.youtube.com")
    print(textnode1)
    htmlnode1 = HTMLNode("div", "hello world", None, {"class": "greeting", "href": "https://boot.dev"})
    print(htmlnode1.props_to_html())



main()