from services.messageService import MessageService
from services.searchService import SearchService


def init_routes(app):

    if app:

        msg_service = MessageService()
        app.add_url_rule('/messages', 'get_all_messages', msg_service.get_all_messages, methods=["GET"])

        search_service = SearchService()
        app.add_url_rule("/search", 'search', search_service.search, methods=["POST"])
