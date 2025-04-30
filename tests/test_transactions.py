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

def test_add_product_and_purchase(db_session):
    # Add product
    product = Product(name="Test Widget", sku="TW-001", category="Gadgets", purchase_price=10.0)
    db_session.add(product)
    db_session.commit()

    # Ensure product added
    added = db_session.query(Product).filter_by(sku="TW-001").first()
    assert added is not None
    assert added.name == "Test Widget"

    # Add purchase
    txn = Transaction(
        product_id=added.id,
        type=TransactionType.PURCHASE,
        quantity=5,
        unit_price=10.0,
        date=datetime.utcnow()
    )
    db_session.add(txn)
    db_session.commit()

    # Check transaction
    purchases = db_session.query(Transaction).filter_by(product_id=added.id, type=TransactionType.PURCHASE).all()
    assert len(purchases) == 1
    assert purchases[0].quantity == 5

def test_record_sale_transaction(db_session):
    product = Product(name="Sale Widget", sku="SW-001", category="Gadgets", purchase_price=12.0)
    db_session.add(product)
    db_session.commit()

    txn = Transaction(
        product_id=product.id,
        type=TransactionType.SALE,
        quantity=3,
        unit_price=20.0,
        date=datetime.utcnow()
    )
    db_session.add(txn)
    db_session.commit()

    sales = db_session.query(Transaction).filter_by(product_id=product.id, type=TransactionType.SALE).all()
    assert len(sales) == 1
    assert sales[0].quantity == 3
    assert sales[0].unit_price == 20.0
