import pytest

from algorithms.chapter_01_arrays_and_strings.q04_palindrome_permutation import \
    is_palindrome_permutation
from algorithms.chapter_01_arrays_and_strings.q05_one_edit_away import \
    is_one_edit_away
from algorithms.chapter_01_arrays_and_strings.q06_string_compression import \
    compressed_string
from algorithms.chapter_01_arrays_and_strings.q07_rotate_matrix import \
    rotate_matrix
from algorithms.chapter_01_arrays_and_strings.q08_zero_matrix import zero_matrix
from algorithms.chapter_01_arrays_and_strings.q09_string_rotation import \
    is_rotation
from algorithms.strings import has_unique_chars, is_permutation, urlify


@pytest.mark.parametrize(
    'input_str',
    [
        '',
        'a',
        'ab',
        'abc',
        'hsjdpayb',
    ]
)
def test_has_unique_chars(input_str):
    assert has_unique_chars(input_str)


@pytest.mark.parametrize(
    'input_str',
    [
        'aa',
        'bb',
        'aabc',
        'abbc',
        'abcc',
        'abhjskaer',
        'abhrjskaer',
    ]
)
def test_does_not_have_unique_chars(input_str):
    assert not has_unique_chars(input_str)


@pytest.mark.parametrize(
    'a,b',
    [
        ('', ''),
        ('a', 'a'),
        ('ab', 'ab'),
        ('ab', 'ba'),
        ('abc', 'abc'),
        ('abc', 'cab'),
        ('abc', 'bca'),
        ('abc', 'acb'),
        ('abc', 'bac'),
        ('abc', 'cba'),
        ('hdbcge', 'cebhdg'),
    ]
)
def test_is_permutation(a, b):
    assert is_permutation(a, b)


@pytest.mark.parametrize(
    'a,b',
    [
        ('', 'a'),
        ('a', 'ab'),
        ('abc', 'abd'),
        ('asdv', 'cba'),
    ]
)
def test_is_not_permutation(a, b):
    assert not is_permutation(a, b)


@pytest.mark.parametrize(
    'chars,real_size',
    [
        (list('a b  '), 3),
        (list('Mr John Smith    '), 13),
    ]
)
def test_urlify(chars, real_size):
    assert ''.join(urlify(chars, real_size)) == \
           ''.join(chars).strip().replace(' ', '%20')


@pytest.mark.parametrize(
    'string',
    [
        '',
        'a',
        'aba',
        'baa',
        'hhdgttd',
    ]
)
def test_is_palindrome_permutation(string):
    assert is_palindrome_permutation(string)


@pytest.mark.parametrize(
    'string',
    [
        'ab',
        'ba',
        'abc'
    ]
)
def test_is_not_palindrome_permutation(string):
    assert not is_palindrome_permutation(string)


@pytest.mark.parametrize(
    'a,b',
    [
        ('', ''),
        ('a', ''),
        ('', 'a'),
        ('a', 'a'),
        ('a', 'b'),
        ('ab', 'ab'),
        ('abc', 'ab'),
        ('bc', 'abc'),
        ('abc', 'bc'),
        ('abc', 'adc'),
    ]
)
def test_is_one_edit_away(a, b):
    assert is_one_edit_away(a, b)


@pytest.mark.parametrize(
    'a,b',
    [
        ('', 'ab'),
        ('ab', ''),
        ('aa', 'bb'),
        ('abc', 'acb'),
        ('asdv', 'cba'),
    ]
)
def test_is_not_one_edit_away(a, b):
    assert not is_one_edit_away(a, b)


@pytest.mark.parametrize(
    'input_str,expected',
    [
        ('', ''),
        ('a', 'a'),
        ('abc', 'abc'),
        ('abbc', 'abbc'),
        ('abbbc', 'abbbc'),
        ('aabbbccbb', 'a2b3c2b2'),
        ('abbbbccbb', 'a1b4c2b2'),
    ]
)
def test_is_one_edit_away(input_str, expected):
    assert compressed_string(input_str) == expected


@pytest.mark.parametrize(
    'matrix,expected',
    [
        ('a', 'a'),
        ('aa\nbb', 'ba\nba'),
        ('aaa\nbbb\nccc', 'cba\ncba\ncba'),
        ('abcde\nfghij\nklmno\npqrst\nuvxyz', 'upkfa\nvqlgb\nxrmhc\nysnid\nztoje'),
    ]
)
def test_rotate_matrix(matrix, expected):
    matrix_as_lists = []
    for line in matrix.splitlines():
        matrix_as_lists.append([c for c in line])

    rotate_matrix(matrix_as_lists) == expected

    obtained = []
    for line in matrix_as_lists:
        obtained.append(''.join(line))

    assert '\n'.join(obtained) == expected


@pytest.mark.parametrize(
    'matrix,expected',
    [
        ('0', '0'),
        ('1', '1'),
        ('01\n11', '00\n01'),
        ('11\n10', '10\n00'),
        ('11\n11', '11\n11'),
        ('101\n111\n111', '000\n101\n101'),
    ]
)
def test_zero_matrix(matrix, expected):
    matrix_as_lists = []
    for line in matrix.splitlines():
        matrix_as_lists.append([int(c) for c in line])

    zero_matrix(matrix_as_lists) == expected

    obtained = []
    for line in matrix_as_lists:
        obtained.append(''.join([str(c) for c in line]))

    assert '\n'.join(obtained) == expected


@pytest.mark.parametrize(
    'a,b',
    [
        ('', ''),
        ('a', 'a'),
        ('ab', 'ab'),
        ('ab', 'ba'),
        ('waterbottle', 'erbottlewat'),
    ]
)
def test_is_rotation(a, b):
    assert is_rotation(a, b)


@pytest.mark.parametrize(
    'a,b',
    [
        ('ab', ''),
        ('aa', 'bb'),
        ('abc', 'acb'),
        ('asdv', 'cba'),
        ('waterbottle', 'rbottlewat'),
    ]
)
def test_is_not_rotation(a, b):
    assert not is_rotation(a, b)
