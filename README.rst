__UPDATE 2022-10-25__

This repository is being replaced by https://github.com/linkml/prefixmaps/issues/6

Newer code should not use the prefixcommons package on PyPI, but instead use [prefixmaps](https://pypi.org/project/prefixmaps) combined with [curies](https://pypi.org/project/curies)

prefixcommons
=============

A python API for working with ID prefixes in the context of
`prefixcommons <http://prefixcommons.org>`__

Current functionality: Uses JSON-LD contexts to expand and contract
CURIEs to URIs

E.g. GO:0008150 <=> http://purl.obolibrary.org/obo/GO\_0008150

Example
=======

::
   
   >>> from prefixcommons import contract_uri
   >>> print(contract_uri('http://purl.obolibrary.org/obo/GO_0008150'))
   ['GO:0008150']
   
   >>> from prefixcommons import expand_uri
   >>> print(expand_uri('GO:000850'))
   http://purl.obolibrary.org/obo/GO_0008150

The above uses standard JSON-LD context files from 
`prefixcommons/biocontext <https://github.com/prefixcommons/biocontext>`__

You can pass your own

::

   >>> cmaps = [{'GO': 'http://purl.obolibrary.org/obo/GO_'}]
   >>> print(contract_uri('http://purl.obolibrary.org/obo/GO_0008150'), cmaps)
   ['GO:0008150']

