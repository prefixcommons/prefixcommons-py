from prefixcommons import CsvTransformer


def test_csv():
    t = CsvTransformer()
    t.transform("tests/ids.tsv", "tests/ids-tr.tsv")
    t2 = CsvTransformer(contract=True)
    t2.transform("tests/ids-tr.tsv", "tests/ids-tr2.tsv")


    
