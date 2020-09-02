from flask import Flask
from service.messageService import MessageService
# from service.searchService import SearchService

def init_routes(app):

    if app:

        msgService = MessageService()
        app.add_url_rule('/messages', 'get_all_messages', msgService.get_all_messages, methods=["GET"])

        searcService = SearchService()
        app.add_url_rule("/search", 'search', searchService.search, methods=["POST"])
