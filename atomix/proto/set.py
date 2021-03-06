# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: atomix/set/set.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncGenerator, Optional

import betterproto

from atomix.proto import headers


class ResponseStatus(betterproto.Enum):
    OK = 0
    NOOP = 1
    WRITE_LOCK = 2


class EventResponseType(betterproto.Enum):
    NONE = 0
    ADDED = 1
    REMOVED = 2


@dataclass
class CreateRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class CreateResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


@dataclass
class CloseRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    delete: bool = betterproto.bool_field(2)


@dataclass
class CloseResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


@dataclass
class SizeRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class SizeResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    size: int = betterproto.int32_field(2)


@dataclass
class ContainsRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class ContainsResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    contains: bool = betterproto.bool_field(2)


@dataclass
class AddRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class AddResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    status: "ResponseStatus" = betterproto.enum_field(2)
    added: bool = betterproto.bool_field(3)


@dataclass
class RemoveRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class RemoveResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    status: "ResponseStatus" = betterproto.enum_field(2)
    removed: bool = betterproto.bool_field(3)


@dataclass
class ClearRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class ClearResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


@dataclass
class EventRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    replay: bool = betterproto.bool_field(2)


@dataclass
class EventResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    type: "EventResponseType" = betterproto.enum_field(2)
    value: str = betterproto.string_field(3)


@dataclass
class IterateRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class IterateResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    value: str = betterproto.string_field(2)


class SetServiceStub(betterproto.ServiceStub):
    """Set service"""

    async def create(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> CreateResponse:
        """Create creates a set session"""

        request = CreateRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.set.SetService/Create", request, CreateResponse,
        )

    async def close(
        self, *, header: Optional[headers.RequestHeader] = None, delete: bool = False
    ) -> CloseResponse:
        """Close closes a set"""

        request = CloseRequest()
        if header is not None:
            request.header = header
        request.delete = delete

        return await self._unary_unary(
            "/atomix.set.SetService/Close", request, CloseResponse,
        )

    async def size(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> SizeResponse:
        """Size gets the number of elements in the set"""

        request = SizeRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.set.SetService/Size", request, SizeResponse,
        )

    async def contains(
        self, *, header: Optional[headers.RequestHeader] = None, value: str = ""
    ) -> ContainsResponse:
        """Contains returns whether the set contains a value"""

        request = ContainsRequest()
        if header is not None:
            request.header = header
        request.value = value

        return await self._unary_unary(
            "/atomix.set.SetService/Contains", request, ContainsResponse,
        )

    async def add(
        self, *, header: Optional[headers.RequestHeader] = None, value: str = ""
    ) -> AddResponse:
        """Add adds a value to the set"""

        request = AddRequest()
        if header is not None:
            request.header = header
        request.value = value

        return await self._unary_unary(
            "/atomix.set.SetService/Add", request, AddResponse,
        )

    async def remove(
        self, *, header: Optional[headers.RequestHeader] = None, value: str = ""
    ) -> RemoveResponse:
        """Remove removes a value from the set"""

        request = RemoveRequest()
        if header is not None:
            request.header = header
        request.value = value

        return await self._unary_unary(
            "/atomix.set.SetService/Remove", request, RemoveResponse,
        )

    async def clear(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> ClearResponse:
        """Clear removes all values from the set"""

        request = ClearRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.set.SetService/Clear", request, ClearResponse,
        )

    async def events(
        self, *, header: Optional[headers.RequestHeader] = None, replay: bool = False
    ) -> AsyncGenerator[EventResponse, None]:
        """Events listens for set change events"""

        request = EventRequest()
        if header is not None:
            request.header = header
        request.replay = replay

        async for response in self._unary_stream(
            "/atomix.set.SetService/Events", request, EventResponse,
        ):
            yield response

    async def iterate(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> AsyncGenerator[IterateResponse, None]:
        """Iterate iterates through all values in the set"""

        request = IterateRequest()
        if header is not None:
            request.header = header

        async for response in self._unary_stream(
            "/atomix.set.SetService/Iterate", request, IterateResponse,
        ):
            yield response
