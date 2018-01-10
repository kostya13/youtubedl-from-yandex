import getpass
import imaplib
import email
import email.message
import re
import subprocess

command = 'youtube-dl -f 43 https://www.youtube.com/watch?v={}'

user = 'kx13@ya.ru'
M = imaplib.IMAP4_SSL('imap.yandex.ru')
M.login(user, getpass.getpass())
M.select('Youtube')
mails = M.search(None, 'ALL')[1]
for m in mails[0].split(b' '):
    status, data = M.fetch(m, '(RFC822)')
    msg = email.message_from_bytes(data[0][1],
                                   _class=email.message.EmailMessage)
    payload = msg.get_payload()[1]
    html = payload.get_payload(decode=True).decode('utf-8')
    match = re.search('watch%3Fv%3D(.+?)%26feature%3Dem-uploademail', html)
    if match:
        video = match.group(1)
        subprocess.run(command.format(video), shell=True)
