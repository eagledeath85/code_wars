class HTMLGen:

    def a(self, element):
        return f"<a>{element}</a>"

    def b(self, element):
        return f"<b>{element}</b>"

    def p(self, element):
        return f"<p>{element}</p>"

    def body(self, element):
        p_part = self.p(element)
        return f"<body>\n\t{p_part}\n</body>"

    def div(self, element):
        p_part = self.p(element)
        return f"<div class='myClass'>\n\t{p_part}\n</div>"

    def span(self, element):
        return f"<span>{element}</span>"

    def title(self, element):
        return f"<title>{element}</title>"

    def comment(self, element):
        return f"<!--{element}-->"


g = HTMLGen()
print(g.a("https://www.w3schools.com"))
print(g.comment('test'))
print()

print(g.body("This is a paragraph."))
print(g.div("This is a paragraph."))
