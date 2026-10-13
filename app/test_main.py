from app.main import get_human_age


def test_get_human_age_14() -> None:
    assert get_human_age(14, 14) == [0, 0], (
        "14 cat/dog years should convert into 0 human age."
    )


def test_get_human_age_23() -> None:
    assert get_human_age(23, 23) == [1, 1], (
        "23 cat/dog years should convert into 1 human age."
    )


def test_get_human_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2], (
        "24 cat/dog years should convert into 2 human age."
    )


def test_get_human_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1], (
        "15 cat/dog years should convert into 1 human age."
    )


def test_get_human_age_28() -> None:
    assert get_human_age(28, 29) == [3, 3], (
        "28/29 cat/dog years should convert into 3 human age."
    )


def test_get_human_age_27() -> None:
    assert get_human_age(27, 28) == [2, 2], (
        "27/28 cat/dog years should convert into 2 human age."
    )
