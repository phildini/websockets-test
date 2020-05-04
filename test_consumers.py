import pytest
from channels.testing import HttpCommunicator, WebsocketCommunicator
from django.test import Client
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async

from websocketstest.routing import application
from model_mommy import mommy


TEST_CHANNEL_LAYERS = {
    "default": {"BACKEND": "channels.layers.InMemoryChannelLayer",},
}


@pytest.mark.asyncio
class TestWebsockets:
    async def test_user_can_connect(self, settings):

        communicator = WebsocketCommunicator(
            application=application, path="/ws/notifications/"
        )
        connected, _ = await communicator.connect()
        assert connected
        await communicator.disconnect()

    async def test_receives_data(self, settings):

        communicator = WebsocketCommunicator(
            application=application, path="/ws/notifications/"
        )
        connected, _ = await communicator.connect()
        assert connected
        await communicator.send_json_to({"type": "notify", "data": "who knows"})
        response = await communicator.receive_json_from()
        await communicator.disconnect()


@pytest.mark.asyncio
async def test_receives_data(settings):
    communicator = WebsocketCommunicator(
        application=application, path="/ws/notifications/"
    )
    connected, _ = await communicator.connect()
    assert connected
    await communicator.send_json_to({"type": "notify", "data": "who knows"})
    response = await communicator.receive_json_from()
    await communicator.disconnect()
