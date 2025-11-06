from faststream.rabbit import RabbitRouter

from src.brokers import notification_stream


def setup_brokers_router() -> RabbitRouter:
    router = RabbitRouter()

    router.include_router(notification_stream.router)

    return router