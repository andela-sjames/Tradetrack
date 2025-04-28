# CLI commands go here

import typer
from sqlalchemy.sql import func
from app.db import SessionLocal, init_db
from app.models import Product, Transaction, TransactionType
from datetime import datetime

app = typer.Typer()

@app.command()
def add_product(
    name: str = typer.Option(..., prompt=True, help="Name of the product"),
    sku: str = typer.Option(..., prompt=True, help="Stock Keeping Unit"),
    category: str = typer.Option("Uncategorized", help="Product category"),
    purchase_price: float = typer.Option(..., prompt=True, help="Purchase price per unit")
):
    """Add a new product to the inventory."""
    init_db()
    db = SessionLocal()
    try:
        product = Product(name=name, sku=sku, category=category, purchase_price=purchase_price)
        db.add(product)
        db.commit()
        typer.echo(f"✅ Product '{name}' added with SKU '{sku}'")
    except Exception as e:
        db.rollback()
        typer.echo(f"❌ Error: {e}")
    finally:
        db.close()


@app.command()
def record_purchase(
    sku: str = typer.Option(..., prompt=True, help="Product SKU to record purchase for"),
    quantity: int = typer.Option(..., prompt=True, help="Number of units purchased"),
    unit_price: float = typer.Option(..., prompt=True, help="Price per unit at purchase")
):
    """Record a product purchase transaction."""
    init_db()
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.sku == sku).first()
        if not product:
            typer.echo(f"❌ No product found with SKU '{sku}'")
            return
        txn = Transaction(
            product_id=product.id,
            type=TransactionType.PURCHASE,
            date=datetime.utcnow(),
            quantity=quantity,
            unit_price=unit_price
        )
        db.add(txn)
        db.commit()
        typer.echo(f"✅ Recorded purchase...")
    except Exception as e:
        db.rollback()
        typer.echo(f"❌ Error: {e}")
    finally:
        db.close()


@app.command()
def record_sale(
    sku: str = typer.Option(..., prompt=True, help="Product SKU to record sale for"),
    quantity: int = typer.Option(..., prompt=True, help="Number of units sold"),
    unit_price: float = typer.Option(..., prompt=True, help="Selling price per unit")
):
    """Record a product sale transaction."""
    init_db()
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.sku == sku).first()
        if not product:
            typer.echo(f"❌ No product found with SKU '{sku}'")
            return
        txn = Transaction(
            product_id=product.id,
            type=TransactionType.SALE,
            date=datetime.utcnow(),
            quantity=quantity,
            unit_price=unit_price
        )
        db.add(txn)
        db.commit()
        typer.echo(f"✅ Recorded sale of {quantity} units at ${unit_price} each for '{product.name}'")
    except Exception as e:
        db.rollback()
        typer.echo(f"❌ Error: {e}")
    finally:
        db.close()

@app.command()
def inventory_status():
    """Display current inventory status for all products."""
    init_db()
    db = SessionLocal()
    try:
        products = db.query(Product).all()
        if not products:
            typer.echo("No products found.")
            return

        for product in products:
            purchases = db.query(func.sum(Transaction.quantity)).filter_by(
                product_id=product.id, type=TransactionType.PURCHASE).scalar() or 0
            sales = db.query(func.sum(Transaction.quantity)).filter_by(
                product_id=product.id, type=TransactionType.SALE).scalar() or 0
            in_stock = purchases - sales
            typer.echo(f"\n📦 {product.name} (SKU: {product.sku})")
            typer.echo(f"Category: {product.category}")
            typer.echo(f"In Stock: {in_stock} units")
            typer.echo(f"Avg Purchase Price: ${product.purchase_price:.2f}")
            typer.echo(f"Estimated Inventory Value: ${in_stock * product.purchase_price:.2f}")
    except Exception as e:
        typer.echo(f"❌ Error: {e}")
    finally:
        db.close()

@app.command()
def profit_report(
    sku: str = typer.Option(None, help="Optional: Product SKU to generate report for"),
):
    """Display profit report for one or all products."""
    init_db()
    db = SessionLocal()
    try:
        if sku:
            product = db.query(Product).filter(Product.sku == sku).first()
            if not product:
                typer.echo(f"❌ No product found with SKU '{sku}'")
                return
            products = [product]
        else:
            products = db.query(Product).all()
            if not products:
                typer.echo("No products found.")
                return

        for product in products:
            sales_qty = db.query(func.sum(Transaction.quantity)).filter_by(
                product_id=product.id, type=TransactionType.SALE
            ).scalar() or 0

            sales_total = db.query(func.sum(Transaction.quantity * Transaction.unit_price)).filter_by(
                product_id=product.id, type=TransactionType.SALE
            ).scalar() or 0.0

            cost_total = db.query(func.sum(Transaction.quantity * Transaction.unit_price)).filter_by(
                product_id=product.id, type=TransactionType.PURCHASE
            ).scalar() or 0.0

            profit = sales_total - cost_total

            typer.echo(f"\n📊 {product.name} (SKU: {product.sku})")
            typer.echo(f"Total Units Sold: {sales_qty}")
            typer.echo(f"Total Revenue: ${sales_total:.2f}")
            typer.echo(f"Total Cost:    ${cost_total:.2f}")
            typer.echo(f"Net Profit:    ${profit:.2f}")

    except Exception as e:
        typer.echo(f"❌ Error generating report: {e}")
    finally:
        db.close()
