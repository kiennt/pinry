#!/usr/bin/env sh
. venv/bin/activate

runserver() {
    python manage.py runserver
}

dumpdata() {
    python manage.py dumpdata auth.user --indent=4 > pinry/pins/fixtures/user.json
    python manage.py dumpdata social_auth --indent=4 > pinry/pins/fixtures/social_auth.json
    python manage.py dumpdata core --indent=4 > pinry/pins/fixtures/member.json
    python manage.py dumpdata pins --indent=4 > pinry/pins/fixtures/pins.json
}

case "$1" in
    runserver)
        runserver
        ;;
    dumpdata)
        dumpdata
        ;;
    *)
        echo "USAGE ./pinry {runserver|dumpdata}"
esac
