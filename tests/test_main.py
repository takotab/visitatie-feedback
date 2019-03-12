import visitatie


def test_main():
    a_form = visitatie.get_data(i=0)
    colour = visitatie.get_colour(a_form)
    assert type(colour) == str

