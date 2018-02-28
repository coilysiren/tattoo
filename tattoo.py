#!/usr/bin/env python

from assets import (
    entities, roles, majors
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
    education = [
        majors.MechanicalEngineering,
        majors.MaterialScience,
        majors.AstronauticalEngineering,
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
