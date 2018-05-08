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
   GO:0008150
   
   >>> from prefixcommons import expand_uri
   >>> print(expand_uri('GOL0008150'))
   http://purl.obolibrary.org/obo/GO_0008150

The above uses standard JSON-LD context files from 
`prefixcommons/biocontext <https://github.com/prefixcommons/biocontext>`__

You can pass your own

::

   >>> cmaps = [{'GO': 'http://purl.obolibrary.org/obo/GO_'}]
   >>> print(contract_uri('http://purl.obolibrary.org/obo/GO_0008150'), cmaps)
   GO:0008150

