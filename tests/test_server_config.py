import os

from arma_server_tools.server_config import Generator


def test_generator_simple_item1():
    gen = Generator()
    result = gen.simple_item("key", "value")
    print(result)
    expected = 'key = "value";'
    assert result == expected


def test_generator_simple_lineitem2():
    gen = Generator()
    result = gen.simple_item("motdInterval", 5)
    expected = 'motdInterval = 5;'
    assert result == expected

def test_generator_simple_lineitem3():
    gen = Generator()
    result = gen.simple_item("motdInterval", 5)
    expected = 'motdInterval = 5;'
    assert result == expected


def test_basic_list():
    gen = Generator()

    expected = """missionWhitelist[] = {
  "direct_action_dev.Altis",
  "otherMission.Tanoa",
};
"""

    result = gen.list_items(
        "missionWhitelist",
        ["direct_action_dev.Altis", "otherMission.Tanoa"],
    )

    print("~~~~~ EXPECTED")
    print(expected)

    print("~~~~~ RESULT")
    print(result)
    assert result == expected

def test_generate_kavala():
    gen = Generator()
    this_dir, this_filename = os.path.split(__file__)
    kavala_file = os.path.join(this_dir, "warlords_kavala.yaml")
    result = gen.generate(kavala_file)
    print("-=-=-=-")
    print(result)