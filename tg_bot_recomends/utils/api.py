import aiohttp
import json
import logging
from .constants import API_KEY, API_BASE_URL, LANGUAGE

async def get_trending(media_type="all", time_window="week", page=1):
    """Отримати популярні фільми/серіали"""
    url = f"{API_BASE_URL}/trending/{media_type}/{time_window}"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE,
        "page": page
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при отриманні трендів: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (trending): {e}")
        return None

async def get_genres(media_type="movie"):
    """Отримати список жанрів"""
    url = f"{API_BASE_URL}/genre/{media_type}/list"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при отриманні жанрів: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (genres): {e}")
        return None

async def search_movie(query, page=1):
    """Пошук фільмів за запитом"""
    url = f"{API_BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE,
        "query": query,
        "page": page,
        "include_adult": "false"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при пошуку фільмів: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (search_movie): {e}")
        return None

async def search_tv(query, page=1):
    """Пошук серіалів за запитом"""
    url = f"{API_BASE_URL}/search/tv"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE,
        "query": query,
        "page": page,
        "include_adult": "false"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при пошуку серіалів: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (search_tv): {e}")
        return None

async def get_movie_details(movie_id):
    """Отримати деталі фільму"""
    url = f"{API_BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при отриманні деталей фільму: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (movie_details): {e}")
        return None

async def get_tv_details(tv_id):
    """Отримати деталі серіалу"""
    url = f"{API_BASE_URL}/tv/{tv_id}"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при отриманні деталей серіалу: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (tv_details): {e}")
        return None

async def discover_by_genre(media_type="movie", genre_id=None, page=1):
    """Знайти фільми/серіали за жанром"""
    url = f"{API_BASE_URL}/discover/{media_type}"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE,
        "sort_by": "popularity.desc",
        "page": page,
        "include_adult": "false"
    }
    
    if genre_id:
        params["with_genres"] = genre_id
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f"Помилка API при пошуку за жанром: {response.status}")
                    return None
    except Exception as e:
        logging.error(f"Помилка при запиті до API (discover): {e}")
        return None 