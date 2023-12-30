.PHONY: activate deps dev

activate:
	pyenv activate

deps:
	pip install -r requirements.txt

dev:
	python -m codecopilot

