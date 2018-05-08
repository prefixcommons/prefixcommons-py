from prefixcommons import expand_uri, contract_uri, NoPrefix

bp_id = "GO:0008150"
obo_bp_id = "OBO:GO_0008150"
bp_iri = "http://purl.obolibrary.org/obo/GO_0008150"

def test_prefixes():
    assert contract_uri(bp_iri) == [bp_id]
    assert expand_uri(bp_id) == bp_iri
    assert contract_uri("FAKE", strict=False) == []
    try:
        contract_uri("FAKE", strict=True)
    except NoPrefix as e:
        pass
    else:
        assert False
        
def test_prefixes_cmaps():
    cmaps = [ {'GO': 'http://purl.obolibrary.org/obo/GO_'},
              {'OBO': 'http://purl.obolibrary.org/obo/'}
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
    except NoPrefix as e:
        pass
    else:
        assert False
    
        

    
