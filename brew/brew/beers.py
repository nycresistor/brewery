#/usr/bin/env python
from common import db

def create_brew():
    db.mysql_version();
    db.mysql_init();
    return 0

def destroy_brew():
    return 0

def update_brew():
    return 0

def rate_brew():
    return 0
