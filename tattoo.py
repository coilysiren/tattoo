#!/usr/bin/env python

from assets import (
    entities,
    roles,
)

class Lynn(
    entities.Human,
):
    role = roles.Engineer
    name = 'lynn cyrin'
    identities = [
        'african',
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
