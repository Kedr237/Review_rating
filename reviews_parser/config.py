from typing import Callable
from typing import Final


TOP_500: Final[str] = 'https://www.kinopoisk.ru/lists/movies/top500/'
COUNT_PAGES: Final[int] = 10

FILES_DIRECTORY: Final[str] = 'generated/'
PAGES_FILE: Final[str] = FILES_DIRECTORY + 'pages.txt'
IDS_FILE: Final[str] = FILES_DIRECTORY + 'ids.txt'
REVIEW_FILES: Final[str] = FILES_DIRECTORY + 'all_reviews/reviews'


get_reviews_page: Callable[[str], str] = lambda film_id: f'https://www.kinopoisk.ru/film/{film_id}/reviews/ord/date/status/all/perpage/200/'
