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


def test_profit_calculation(db_session):
    product = Product(name="Profit Item", sku="PROF-001", category="Business", purchase_price=15.0)
    db_session.add(product)
    db_session.commit()

    db_session.add(Transaction(product_id=product.id, type=TransactionType.PURCHASE, quantity=3, unit_price=15.0))
    db_session.add(Transaction(product_id=product.id, type=TransactionType.SALE, quantity=3, unit_price=25.0))
    db_session.commit()

    total_sales = db_session.query(func.sum(Transaction.quantity * Transaction.unit_price)).filter_by(product_id=product.id, type=TransactionType.SALE).scalar() or 0
    total_cost = db_session.query(func.sum(Transaction.quantity * Transaction.unit_price)).filter_by(product_id=product.id, type=TransactionType.PURCHASE).scalar() or 0

    profit = total_sales - total_cost
    assert profit == 30.0
