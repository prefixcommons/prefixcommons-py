test:
	pytest tests/*.py

# TODO: manually increment version in prefixcommons/__init__.sh, run . bump.sh, then this
release: cleandist
	python setup.py sdist bdist_wheel bdist_egg
	twine upload dist/*
