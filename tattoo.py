#!/usr/bin/env python

from assets import (
    entities,
    roles,
)

class Lynn(
    entities.Human,
):
    role = roles.SoftwareEngineer
    name = 'lynn cyrin'
    identities = [
        'diasporic african',
        'woman',
    ]
    interests = [
        'OSS',
        'gaming',
        'crafts',
    ]
    jobs = [
        'NASA',
        'Bundler',
        'Callisto',
