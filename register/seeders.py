from bolinette import env, transaction, db
from bolinette.services import role_service, user_service

from register.services import language_service


@db.engine.seeder
async def role_seeder():
    with transaction:
        await role_service.create({'name': 'root'})
        await role_service.create({'name': 'admin'})
        await role_service.create({'name': 'creator'})


@db.engine.seeder
async def dev_user_seeder():
    if env['PROFILE'] == 'development':
        with transaction:
            root = await role_service.get_by_name('root')
            admin = await role_service.get_by_name('admin')
            root_usr = await user_service.create({
                'username': 'root',
                'password': 'root',
                'email': f'root@localhost'
            })
            root_usr.roles.append(root)
            root_usr.roles.append(admin)

            dev0 = await role_service.create({'name': 'dev0'})
            dev1 = await role_service.create({'name': 'dev1'})
            dev2 = await role_service.create({'name': 'dev2'})
            roles = [dev0, dev1, dev2]

            for i in range(10):
                user = await user_service.create({
                    'username': f'user_{i}',
                    'password': 'test',
                    'email': f'user{i}@test.com'
                })
                user.roles.append(roles[i % 3])
                user.roles.append(roles[(i + 1) % 3])


@db.engine.seeder
async def dev_register_seeder():
    if env['PROFILE'] == 'development':
        with transaction:
            await language_service.create({'name': 'fr'})
            await language_service.create({'name': 'en'})
