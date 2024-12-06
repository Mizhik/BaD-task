import pytest
from collections import defaultdict

# Імпорт функцій, які тестуємо
from main import build_graph, assemble_sequence, find_longest_sequence


@pytest.mark.parametrize(
    "fragments, expected_sequence",
    [
        (["248460", "608017", "177092"], "24846080177092"),
        (["123456", "567890", "908123"], "12345678908123"),
        (["111222", "223333", "334444", "445555"], "111222333344445555"),
        (["000111", "222333", "444555"], "000111"),
    ],
)
def test_longest_sequence(fragments, expected_sequence):
    graph = build_graph(fragments)
    longest_path = find_longest_sequence(graph, fragments)
    result_sequence = assemble_sequence(longest_path)
    assert result_sequence == expected_sequence
