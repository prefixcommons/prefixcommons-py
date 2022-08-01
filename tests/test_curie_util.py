from prefixcommons import NoPrefix, contract_uri, expand_uri
from prefixcommons.curie_util import read_biocontext

bp_id = "GO:0008150"
obo_bp_id = "OBO:GO_0008150"
bp_iri = "http://purl.obolibrary.org/obo/GO_0008150"

CASES = [
    # semweb context is a default so should work for both
    ("owl:Class", "http://www.w3.org/2002/07/owl#Class", [None, ["semweb_context"]]),
    # obo context is a default so should work for both
    (bp_id, bp_iri, [None, ["obo_context"]]),
    # monarch context is a default so should work for both
    (
        "biolink:Gene",
        "https://w3id.org/biolink/vocab/Gene",
        [None, ["monarch_context"]],
    ),
    # identifier.org test
    ("BIOSAMPLE:SAM001", "http://identifiers.org/biosample/SAM001", [["idot_context"]]),
    # ensure that if identifiers.org is explicitly passed this has precedence
    ("CL:0000001", "http://identifiers.org/cl/0000001", [["idot_context"]]),
    # ensure that if obo is explicitly passed this has precedence; also obo is a default
    (
        "CL:0000001",
        "http://purl.obolibrary.org/obo/CL_0000001",
        [None, ["obo_context"]],
    ),
    # conflict test: first has priority
    (
        "CL:0000001",
        "http://identifiers.org/cl/0000001",
        [["idot_context", "obo_context"]],
    ),
    # conflict test: first has priority
    (
        "CL:0000001",
        "http://purl.obolibrary.org/obo/CL_0000001",
        [["obo_context", "idot_context"]],
    ),
]


def test_cases():
    for curie, uri, prefixmap_sets in CASES:
        for prefixmap_set in prefixmap_sets:
            if prefixmap_set is not None:
                prefixmap_set = [read_biocontext(n) for n in prefixmap_set]
            assert contract_uri(uri, cmaps=prefixmap_set) == [curie]
            assert expand_uri(curie, cmaps=prefixmap_set) == uri


def test_prefixes():
    assert contract_uri(bp_iri) == [bp_id]
    assert expand_uri(bp_id) == bp_iri
    assert contract_uri("FAKE", strict=False) == []
    try:
        contract_uri("FAKE", strict=True)
    except NoPrefix:
        pass
    else:
        assert False


def test_prefixes_cmaps():
    cmaps = [
        {"GO": "http://purl.obolibrary.org/obo/GO_"},
        {"OBO": "http://purl.obolibrary.org/obo/"},
    ]
    assert contract_uri(bp_iri, cmaps) == [bp_id]
    all_curies = contract_uri(bp_iri, cmaps, shortest=False)
    assert len(all_curies) == 2
    assert obo_bp_id in all_curies
    assert bp_id in all_curies
    assert expand_uri(bp_id, cmaps) == bp_iri
    assert expand_uri(obo_bp_id, cmaps) == bp_iri
    assert contract_uri("FAKE", cmaps, strict=False) == []
    try:
        contract_uri("FAKE", cmaps, strict=True)
    except NoPrefix:
        pass
    else:
        assert False
