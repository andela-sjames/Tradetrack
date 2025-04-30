# Run tests
test:
	pytest tests

# View test coverage in the terminal
coverage:
	pytest --cov=app --cov-report=term-missing tests

# Generate a full HTML coverage report
htmlcov:
	pytest --cov=app --cov-report=html tests
	python -m webbrowser -t htmlcov/index.html
