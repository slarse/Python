from strings.min_cost_string_conversion import (
    main,
    compute_transform_tables,
    assemble_transformation,
)


def test_min_cost_for_replacing_python_with_algorithms():
    """Testing the cost for replacing string values Python with Algorithms"""
    _, operations = compute_transform_tables("Python", "Algorithms", -1, 1, 2, 2)

    m = len(operations)
    n = len(operations[0])
    sequence = assemble_transformation(operations, m - 1, n - 1)
    string = list("Python")
    assert main(sequence, string) == 10
