from assets import (
    entities, roles
)

class Lynn(
    entities.Human,
):
    name = 'lynn cyrin'
    role = roles.SoftwareEngineer
    sexuality = 'queer'
    race = 'diasporic african'
    gender_prefix = 'trans'
    gender = 'femme'

    def work_output(self):
        return super()\
            .work_output() * 2

    @property
    def jobs(self):
        return [
            'NASA',
            'Bundler',
            'Callisto',
