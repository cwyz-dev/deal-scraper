class Product:
    def __init__(self, name, sale_price, normal_price, link):
        self.name = name
        self.sale_price = sale_price
        self.normal_price = normal_price
        self.link = link

    def serialize(self):
        return  {
                    "name": self.name,
                    "sale_price": self.sale_price,
                    "normal_price": self.normal_price,
                    "link": self.link
                }

    def from_json(self, json):
        self.name = json_["name"]
        self.sale_price = json_["sale_price"]
        self.normal_price = json_["normal_price"]
        self.link = json_["link"]
