test:
	uv run python -m pytest -vv tests
	
lint:
	uv run mypy . --ignore-missing-imports --no-strict-optional

release:
	rm dist/*
	uv build
	uv publish

