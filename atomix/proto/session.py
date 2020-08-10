# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: atomix/session/session.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import Optional

import betterproto

from atomix.proto import headers


@dataclass
class OpenSessionRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    timeout: timedelta = betterproto.message_field(2)


@dataclass
class OpenSessionResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


@dataclass
class KeepAliveRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)


@dataclass
class KeepAliveResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


@dataclass
class CloseSessionRequest(betterproto.Message):
    header: headers.RequestHeader = betterproto.message_field(1)
    delete: bool = betterproto.bool_field(2)


@dataclass
class CloseSessionResponse(betterproto.Message):
    header: headers.ResponseHeader = betterproto.message_field(1)


class SessionServiceStub(betterproto.ServiceStub):
    """Session service"""

    async def open_session(
        self,
        *,
        header: Optional[headers.RequestHeader] = None,
        timeout: Optional[timedelta] = None,
    ) -> OpenSessionResponse:
        """OpenSession opens a new session"""

        request = OpenSessionRequest()
        if header is not None:
            request.header = header
        if timeout is not None:
            request.timeout = timeout

        return await self._unary_unary(
            "/atomix.session.SessionService/OpenSession", request, OpenSessionResponse,
        )

    async def keep_alive(
        self, *, header: Optional[headers.RequestHeader] = None
    ) -> KeepAliveResponse:
        """KeepAlive keeps a session alive"""

        request = KeepAliveRequest()
        if header is not None:
            request.header = header

        return await self._unary_unary(
            "/atomix.session.SessionService/KeepAlive", request, KeepAliveResponse,
        )

    async def close_session(
        self, *, header: Optional[headers.RequestHeader] = None, delete: bool = False
    ) -> CloseSessionResponse:
        """CloseSession closes a session"""

        request = CloseSessionRequest()
        if header is not None:
            request.header = header
        request.delete = delete

        return await self._unary_unary(
            "/atomix.session.SessionService/CloseSession",
            request,
            CloseSessionResponse,
        )