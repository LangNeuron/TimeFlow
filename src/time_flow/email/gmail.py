"""Gmail sender."""


import smtplib
from email.message import EmailMessage

from time_flow.utils import get_logger, get_settings

settings = get_settings()
log = get_logger(name=__name__, settings=settings.LOGGING)


def send_email(
    recipient_email: str,
    subject: str,
    body: str | None = None,
    html: str | None = None,
) -> None:
    """Send email to user via SMTP GMAIL.

    Parameters
    ----------
    recipient_email : str
        Where send message
    subject : str
        The subject of the email.
    body : str | None, optional
        string message, by default None
    html : str | None, optional
        html message, high priority, by default None

    Raises
    ------
    ValueError
        when html and body is None
    """
    message = EmailMessage()
    message["From"] = f"{settings.GMAIL.DEFAULT_SENDER_NAME} \
        <{settings.GMAIL.DEFAULT_SENDER_EMAIL}>"
    message["To"] = recipient_email
    message["Subject"] = subject

    if html:
        message.add_alternative(html, subtype="html",
                                charset=settings.GMAIL.CHARSET)
    elif body:
        message.set_content(body, charset=settings.GMAIL.CHARSET)
    else:
        msg = "html and body is None"
        log.warning(msg)
        raise ValueError(msg)

    with smtplib.SMTP(settings.GMAIL.SMTP_HOST,
                      settings.GMAIL.SMTP_PORT) as server:
        if settings.GMAIL.USE_TLS:
            server.starttls()

        server.login(settings.GMAIL.SMTP_USERNAME,
                     settings.GMAIL.SMTP_PASSWORD)
        server.send_message(message)

    log.debug("Sent email to user, from %s",
              settings.GMAIL.DEFAULT_SENDER_NAME)
