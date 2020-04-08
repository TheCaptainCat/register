from bolinette import response
from bolinette.exceptions import NotFoundError
from bolinette.routing import Namespace, Method, AccessType
from register.services import page_service, language_service, article_service

ns = Namespace('/page', page_service)


@ns.route('/{lang}', method=Method.GET, access=AccessType.Required)
async def get_by_language(match, **_):
    lang = await language_service.get_by_name(match['lang'])
    return response.ok('OK', await page_service.get_by_language(lang))


@ns.route('/{lang}', method=Method.POST, access=AccessType.Required, roles=['creator'],
          expects=ns.route.expects('page', 'new'), returns=ns.route.returns('page', 'complete'))
@ns.route(r'/{lang}/{article:\d+}', method=Method.POST, access=AccessType.Required, roles=['creator'],
          expects=ns.route.expects('page', 'version'), returns=ns.route.returns('page', 'complete'))
async def create_page(payload, match, current_user, **_):
    language = await language_service.get_by_name(match['lang'])
    article_id = match.get('article')
    article = None
    if article_id:
        article = await article_service.get(article_id)
    return response.created(
        'page.created', await page_service.add_version(
            payload.get('name'), payload['content'], article, language, current_user
        )
    )


@ns.route(r'/{lang}/{article:\d+}', method=Method.GET, access=AccessType.Required,
          returns=ns.route.returns('page', 'complete'))
async def get_page(match, **_):
    language = await language_service.get_by_name(match['lang'])
    article = await article_service.get(match['article'])
    return response.ok('OK', await page_service.get_one_by_article_language(article, language))


@ns.route(r'/{lang}/{article:\d+}/content', method=Method.GET, access=AccessType.Required)
async def get_page_content(match, **_):
    language = await language_service.get_by_name(match['lang'])
    article = await article_service.get(match['article'])
    page = await page_service.get_one_by_article_language(article, language)
    return response.ok('OK', await page_service.get_parsed_content(page))


@ns.route(r'/{lang}/{article:\d+}/versions', method=Method.GET, access=AccessType.Required,
          returns=ns.route.returns('version', as_list=True))
async def get_page_versions(match, **_):
    language = await language_service.get_by_name(match['lang'])
    article = await article_service.get(match['article'])
    page = await page_service.get_one_by_article_language(article, language)
    return response.ok('OK', sorted(page.versions, key=lambda v: v.created_on))


@ns.route(r'/{lang}/{article:\d+}/versions/{version:\d+}', method=Method.GET, access=AccessType.Required,
          returns=ns.route.returns('version'))
async def get_page_version(match, **_):
    language = await language_service.get_by_name(match['lang'])
    article = await article_service.get(match['article'])
    version_index = int(match['version'])
    page = await page_service.get_one_by_article_language(article, language)
    versions = sorted(page.versions, key=lambda v: v.created_on)
    if version_index >= len(versions):
        raise NotFoundError(f'page.version.not_found:lang,page,version:{language.name},{page.id},{version_index}')
    return response.ok('OK', versions[version_index])
