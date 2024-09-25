from jikanpy import Jikan, AioJikan


async def search_anime_by_jikan(anime_name: str, page: int):
    async with AioJikan() as jikan:
        result = await jikan.search(
            'anime',
            anime_name,
            page=page,
            parameters={"limit": 10, "order_by": "score"}
        )

    return result


async def get_random_anime_by_jikan():
    async with AioJikan() as jikan:
        result = await jikan.random(type='anime')

    return result
