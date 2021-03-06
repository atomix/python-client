# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: atomix/indexedmap/indexedmap.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import AsyncGenerator, Optional

import betterproto

from atomix.proto import headers


class ResponseStatus(betterproto.Enum):
    OK = 0
    NOOP = 1
    WRITE_LOCK = 2
    PRECONDITION_FAILED = 3


class EventResponseType(betterproto.Enum):
    NONE = 0
    INSERTED = 1
    UPDATED = 2
    REMOVED = 3


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
class ExistsRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    key: str = betterproto.string_field(2)


@dataclass
class ExistsResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    contains_key: bool = betterproto.bool_field(2)


@dataclass
class SizeRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class SizeResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    size: int = betterproto.int32_field(2)


@dataclass
class PutRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    ttl: timedelta = betterproto.message_field(6)


@dataclass
class PutResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    status: "ResponseStatus" = betterproto.enum_field(2)
    index: int = betterproto.int64_field(3)
    key: str = betterproto.string_field(4)
    created: datetime = betterproto.message_field(5)
    updated: datetime = betterproto.message_field(6)
    previous_value: bytes = betterproto.bytes_field(7)
    previous_version: int = betterproto.int64_field(8)


@dataclass
class ReplaceRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    previous_value: bytes = betterproto.bytes_field(4)
    previous_version: int = betterproto.int64_field(5)
    new_value: bytes = betterproto.bytes_field(6)
    ttl: timedelta = betterproto.message_field(7)


@dataclass
class ReplaceResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    status: "ResponseStatus" = betterproto.enum_field(2)
    index: int = betterproto.int64_field(3)
    key: str = betterproto.string_field(4)
    created: datetime = betterproto.message_field(5)
    updated: datetime = betterproto.message_field(6)
    previous_value: bytes = betterproto.bytes_field(7)
    previous_version: int = betterproto.int64_field(8)


@dataclass
class GetRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)


@dataclass
class GetResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class FirstEntryRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class FirstEntryResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class LastEntryRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class LastEntryResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class PrevEntryRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)


@dataclass
class PrevEntryResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class NextEntryRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)


@dataclass
class NextEntryResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class RemoveRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    index: int = betterproto.int64_field(2)
    key: str = betterproto.string_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class RemoveResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    status: "ResponseStatus" = betterproto.enum_field(2)
    index: int = betterproto.int64_field(3)
    key: str = betterproto.string_field(4)
    previous_value: bytes = betterproto.bytes_field(5)
    previous_version: int = betterproto.int64_field(6)


@dataclass
class ClearRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class ClearResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


@dataclass
class EntriesRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class EntriesResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    key: str = betterproto.string_field(2)
    index: int = betterproto.int64_field(3)
    value: bytes = betterproto.bytes_field(4)
    version: int = betterproto.int64_field(5)
    created: datetime = betterproto.message_field(6)
    updated: datetime = betterproto.message_field(7)


@dataclass
class EventRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    replay: bool = betterproto.bool_field(2)
    key: str = betterproto.string_field(3)
    index: int = betterproto.int64_field(4)


@dataclass
class EventResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)
    type: "EventResponseType" = betterproto.enum_field(2)
    key: str = betterproto.string_field(3)
    index: int = betterproto.int64_field(4)
    value: bytes = betterproto.bytes_field(5)
    version: int = betterproto.int64_field(6)
    created: datetime = betterproto.message_field(7)
    updated: datetime = betterproto.message_field(8)


class IndexedMapServiceStub(betterproto.ServiceStub):
    """IndexedMap service"""

    async def create(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> CreateResponse:
        """Create creates an indexed map"""

        request = CreateRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Create", request, CreateResponse,
        )

    async def close(
        self, *, header: Optional[headers.RequestHeader] = None, delete: bool = False
    ) -> CloseResponse:
        """Close closes an indexed map"""

        request = CloseRequest()
        if header is not None:
            request.header = header
        request.delete = delete

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Close", request, CloseResponse,
        )

    async def size(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> SizeResponse:
        """Size returns the size of the map"""

        request = SizeRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Size", request, SizeResponse,
        )

    async def exists(
        self, *, header: Optional[headers.RequestHeader] = None, key: str = ""
    ) -> ExistsResponse:
        """Exists checks whether a key exists in the map"""

        request = ExistsRequest()
        if header is not None:
            request.header = header
        request.key = key

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Exists", request, ExistsResponse,
        )

    async def put(
        self,
        *,
        header: Optional[headers.RequestHeader] = None,
        index: int = 0,
        key: str = "",
        value: bytes = b"",
        version: int = 0,
        ttl: Optional[timedelta] = None,
    ) -> PutResponse:
        """Put puts an entry into the map"""

        request = PutRequest()
        if header is not None:
            request.header = header
        request.index = index
        request.key = key
        request.value = value
        request.version = version
        if ttl is not None:
            request.ttl = ttl

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Put", request, PutResponse,
        )

    async def replace(
        self,
        *,
        header: Optional[headers.RequestHeader] = None,
        index: int = 0,
        key: str = "",
        previous_value: bytes = b"",
        previous_version: int = 0,
        new_value: bytes = b"",
        ttl: Optional[timedelta] = None,
    ) -> ReplaceResponse:
        """
        Replace performs a check-and-set operation on an entry in the map
        """

        request = ReplaceRequest()
        if header is not None:
            request.header = header
        request.index = index
        request.key = key
        request.previous_value = previous_value
        request.previous_version = previous_version
        request.new_value = new_value
        if ttl is not None:
            request.ttl = ttl

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Replace", request, ReplaceResponse,
        )

    async def get(
        self,
        *,
        header: Optional[headers.RequestHeader] = None,
        index: int = 0,
        key: str = "",
    ) -> GetResponse:
        """Get gets the entry for a key"""

        request = GetRequest()
        if header is not None:
            request.header = header
        request.index = index
        request.key = key

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Get", request, GetResponse,
        )

    async def first_entry(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> FirstEntryResponse:
        """FirstEntry gets the first entry in the map"""

        request = FirstEntryRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/FirstEntry",
            request,
            FirstEntryResponse,
        )

    async def last_entry(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> LastEntryResponse:
        """LastEntry gets the last entry in the map"""

        request = LastEntryRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/LastEntry",
            request,
            LastEntryResponse,
        )

    async def prev_entry(
        self, *, header: Optional[headers.RequestHeader] = None, index: int = 0
    ) -> PrevEntryResponse:
        """PrevEntry gets the previous entry in the map"""

        request = PrevEntryRequest()
        if header is not None:
            request.header = header
        request.index = index

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/PrevEntry",
            request,
            PrevEntryResponse,
        )

    async def next_entry(
        self, *, header: Optional[headers.RequestHeader] = None, index: int = 0
    ) -> NextEntryResponse:
        """NextEntry gets the next entry in the map"""

        request = NextEntryRequest()
        if header is not None:
            request.header = header
        request.index = index

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/NextEntry",
            request,
            NextEntryResponse,
        )

    async def remove(
        self,
        *,
        header: Optional[headers.RequestHeader] = None,
        index: int = 0,
        key: str = "",
        value: bytes = b"",
        version: int = 0,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> RemoveResponse:
        """Remove removes an entry from the map"""

        request = RemoveRequest()
        if header is not None:
            request.header = header
        request.index = index
        request.key = key
        request.value = value
        request.version = version
        if created is not None:
            request.created = created
        if updated is not None:
            request.updated = updated

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Remove", request, RemoveResponse,
        )

    async def clear(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> ClearResponse:
        """Clear removes all entries from the map"""

        request = ClearRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.indexedmap.IndexedMapService/Clear", request, ClearResponse,
        )

    async def events(
        self,
        *,
        header: Optional[headers.RequestHeader] = None,
        replay: bool = False,
        key: str = "",
        index: int = 0,
    ) -> AsyncGenerator[EventResponse, None]:
        """Events listens for change events"""

        request = EventRequest()
        if header is not None:
            request.header = header
        request.replay = replay
        request.key = key
        request.index = index

        async for response in self._unary_stream(
            "/atomix.indexedmap.IndexedMapService/Events", request, EventResponse,
        ):
            yield response

    async def entries(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> AsyncGenerator[EntriesResponse, None]:
        """Entries lists all entries in the map"""

        request = EntriesRequest()
        if header is not None:
            request.header = header

        async for response in self._unary_stream(
            "/atomix.indexedmap.IndexedMapService/Entries", request, EntriesResponse,
        ):
            yield response
