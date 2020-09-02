from flask import Flask
from service.messageService import MessageService

def init_routes(app):

    if app:

        msgService = MessageService()
        app.add_url_rule('/messages', 'get_all_messages', msgService.get_all_messages, methods=["GET"])

        """
        Search for answers!
        Accepts a 'query' as JSON post, returns the full answer.
        curl -d '{"query":"Star Trek"}' -H "Content-Type: application/json" -X POST http://localhost:5000/search
        """
        # app.add_url_rule("/search", methods=["POST"])
