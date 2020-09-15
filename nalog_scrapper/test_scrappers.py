from nalog_scrapper.scrappers import get_org_n_from_nalog_ru

def test_get_org_n_from_nalog_ru():
    assert get_org_n_from_nalog_ru(['7706107510', '5321029508', '6704000505']) == [{'name': 'ПАО "АКРОН"', 'inn': '5321029508', 'id': '2347012'}, {'name': 'ПАО "ДОРОГОБУЖ"', 'inn': '6704000505', 'id': '3356745'}]
