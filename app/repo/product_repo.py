from app.models.product import Product
from app.database.database import Session


class ProductRepo:
    def __init__(self):
        self.session = Session()

    def get_product_by_id(self, product_id: int) -> Product | None:
        return self.session.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product: Product) -> Product:
        if self.get_product_by_id(product.id):
            return product
        self.session.add(product)
        self.session.commit()
        return product

    def update_product(self, product: Product) -> None:
        self.session.commit()
        return

    def delete_product(self, product_id: int) -> None:
        product = self.get_product_by_id(product_id)
        if product:
            self.session.delete(product)
            self.session.commit()
            return
        return

    def get_product_by_uuid(self, uuid: str) -> Product | None:
        return self.session.query(Product).filter(Product.uuid == uuid).first()
