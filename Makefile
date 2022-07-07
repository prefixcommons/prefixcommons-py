test:
	pytest tests/*.py

# TODO: manually increment version in prefixcommons/__init__.sh, run . bump.sh, then this
release: cleandist
	python setup.py sdist bdist_wheel bdist_egg
	twine upload dist/*

cleandist:
	rm dist/* || true

PREFIXSETS = obo_context semweb_context idot_context monarch_context

all-jsonld: $(patsubst %, prefixcommons/registry/%.jsonld, $(PREFIXSETS))
prefixcommons/registry/%.jsonld:
	curl -L -s https://raw.githubusercontent.com/prefixcommons/biocontext/master/registry/$*.jsonld > $@.tmp && mv $@.tmp $@
