from tiny_data_generator import format_csv, generate_rows


def test_generate_rows_count():
    rows = generate_rows(5)
    assert len(rows) == 5


def test_generate_rows_has_expected_columns():
    rows = generate_rows(1)
    assert set(rows[0]) == {"id", "name", "score"}


def test_generate_rows_has_known_first_row():
    rows = generate_rows(1)
    assert rows[0] == {"id": "1", "name": "user_1", "score": "71"}


def test_format_csv_includes_header_and_rows():
    csv_text = format_csv(generate_rows(2))
    assert csv_text.startswith("id,name,score")
    assert "1,user_1,71" in csv_text
    assert "2,user_2,72" in csv_text
