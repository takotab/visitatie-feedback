from visitatie.form import Form


def make_message(name, email, file):
    return {
        "send_from": "visitatiecommissiealkmaar@gmail.com",
        "send_to": [email],
        "subject": "Feedback Visitatie 2018",
        "text": "Beste "
        + name
        + "\n\nIn de bijlage vindt u de resultaten van de afgelopen visitatie ronden.\n\n"
        + "Vriendelijke groeten,\n\nDivera Twisk\n"
        + "Voorzitter Commissie Visitatie Rug-netwerk",
        "files": [file],
    }

