from bolinette import blnt
from bolinette.decorators import seeder


@seeder
async def role_seeder(context: 'blnt.BolinetteContext'):
    role_service = context.service('role')
    async with blnt.Transaction(context):
        await role_service.create({'name': 'root'})
        await role_service.create({'name': 'admin'})
        await role_service.create({'name': 'creator'})


@seeder
async def dev_user_seeder(context: 'blnt.BolinetteContext'):
    role_service = context.service('role')
    user_service = context.service('user')
    if context.env['PROFILE'] == 'development':
        async with blnt.Transaction(context):
            root = await role_service.get_by_name('root')
            admin = await role_service.get_by_name('admin')
            creator = await role_service.get_by_name('creator')
            root_usr = await user_service.create({
                'username': 'root',
                'password': 'root',
                'email': f'root@localhost'
            })
            root_usr.roles.append(root)
            root_usr.roles.append(admin)
            root_usr.roles.append(creator)


@seeder
async def dev_register_seeder(context: 'blnt.BolinetteContext'):
    language_service = context.service('language')
    if context.env['PROFILE'] == 'development':
        async with blnt.Transaction(context):
            await language_service.create({'name': 'fr', 'default': True})
            await language_service.create({'name': 'en', 'default': False})
            await language_service.create({'name': 'es', 'default': False})
            await language_service.create({'name': 'it', 'default': False})
