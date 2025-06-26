import pytest
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from app.models import Base, Product, Transaction, TransactionType
from datetime import datetime

# Setup in-memory SQLite for testing
test_engine = create_engine("sqlite:///:memory:", echo=False)
TestSession = sessionmaker(bind=test_engine)
Base.metadata.create_all(bind=test_engine)

@pytest.fixture
def db_session():
    session = TestSession()
    yield session
    session.close()

def test_inventory_calculation(db_session):
    product = Product(name="Inventory Item", sku="INV-001", category="Stock", purchase_price=5.0)
    db_session.add(product)
    db_session.commit()

    db_session.add(Transaction(product_id=product.id, type=TransactionType.PURCHASE, quantity=10, unit_price=5.0))
    db_session.add(Transaction(product_id=product.id, type=TransactionType.SALE, quantity=4, unit_price=8.0))
    db_session.commit()

    purchases = db_session.query(func.sum(Transaction.quantity)).filter_by(product_id=product.id, type=TransactionType.PURCHASE).scalar() or 0
    sales = db_session.query(func.sum(Transaction.quantity)).filter_by(product_id=product.id, type=TransactionType.SALE).scalar() or 0
    in_stock = purchases - sales

    assert in_stock == 6
