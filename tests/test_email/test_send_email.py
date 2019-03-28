from visitatie import email


def test_make_msg():
    email.send_mail(
        **email.make_message(
            "Divera",
            "takotabak+visitatie_test@gmail.com",
            "data_real/result_pdfs/results_Feedback visitatie Oefentherapie Mensendieck Castricum 2018.pdf",
        )
    )
