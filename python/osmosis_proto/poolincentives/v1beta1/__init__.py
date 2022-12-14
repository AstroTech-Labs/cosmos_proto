# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: genesis.proto, gov.proto, incentives.proto, query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ... import incentives as __incentives__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    minted_denom: str = betterproto.string_field(1)
    """
    minted_denom is the denomination of the coin expected to be minted by the
    minting module. Pool-incentives module doesn’t actually mint the coin
    itself, but rather manages the distribution of coins that matches the
    defined minted_denom.
    """


@dataclass(eq=False, repr=False)
class LockableDurationsInfo(betterproto.Message):
    lockable_durations: List[timedelta] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DistrInfo(betterproto.Message):
    total_weight: str = betterproto.string_field(1)
    records: List["DistrRecord"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class DistrRecord(betterproto.Message):
    gauge_id: int = betterproto.uint64_field(1)
    weight: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class QueryGaugeIdsRequest(betterproto.Message):
    pool_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryGaugeIdsResponse(betterproto.Message):
    gauge_ids_with_duration: List[
        "QueryGaugeIdsResponseGaugeIdWithDuration"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryGaugeIdsResponseGaugeIdWithDuration(betterproto.Message):
    gauge_id: int = betterproto.uint64_field(1)
    duration: timedelta = betterproto.message_field(2)
    gauge_incentive_percentage: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class QueryDistrInfoRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryDistrInfoResponse(betterproto.Message):
    distr_info: "DistrInfo" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryLockableDurationsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryLockableDurationsResponse(betterproto.Message):
    lockable_durations: List[timedelta] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryIncentivizedPoolsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class IncentivizedPool(betterproto.Message):
    pool_id: int = betterproto.uint64_field(1)
    lockable_duration: timedelta = betterproto.message_field(2)
    gauge_id: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class QueryIncentivizedPoolsResponse(betterproto.Message):
    incentivized_pools: List["IncentivizedPool"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryExternalIncentiveGaugesRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryExternalIncentiveGaugesResponse(betterproto.Message):
    data: List["__incentives__.Gauge"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the pool incentives module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the paramaters of the module."""

    lockable_durations: List[timedelta] = betterproto.message_field(2)
    distr_info: "DistrInfo" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class ReplacePoolIncentivesProposal(betterproto.Message):
    """
    ReplacePoolIncentivesProposal is a gov Content type for updating the pool
    incentives. If a ReplacePoolIncentivesProposal passes, the proposal’s
    records override the existing DistrRecords set in the module. Each record
    has a specified gauge id and weight, and the incentives are distributed to
    each gauge according to weight/total_weight. The incentives are put in the
    fee pool and it is allocated to gauges and community pool by the
    DistrRecords configuration. Note that gaugeId=0 represents the community
    pool.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    records: List["DistrRecord"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class UpdatePoolIncentivesProposal(betterproto.Message):
    """
    For example: if the existing DistrRecords were: [(Gauge 0, 5), (Gauge 1,
    6), (Gauge 2, 6)] An UpdatePoolIncentivesProposal includes [(Gauge 1, 0),
    (Gauge 2, 4), (Gauge 3, 10)] This would delete Gauge 1, Edit Gauge 2, and
    Add Gauge 3 The result DistrRecords in state would be: [(Gauge 0, 5),
    (Gauge 2, 4), (Gauge 3, 10)]
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    records: List["DistrRecord"] = betterproto.message_field(3)


class QueryStub(betterproto.ServiceStub):
    async def gauge_ids(
        self,
        query_gauge_ids_request: "QueryGaugeIdsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryGaugeIdsResponse":
        return await self._unary_unary(
            "/osmosis.poolincentives.v1beta1.Query/GaugeIds",
            query_gauge_ids_request,
            QueryGaugeIdsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def distr_info(
        self,
        query_distr_info_request: "QueryDistrInfoRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryDistrInfoResponse":
        return await self._unary_unary(
            "/osmosis.poolincentives.v1beta1.Query/DistrInfo",
            query_distr_info_request,
            QueryDistrInfoResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/osmosis.poolincentives.v1beta1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def lockable_durations(
        self,
        query_lockable_durations_request: "QueryLockableDurationsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryLockableDurationsResponse":
        return await self._unary_unary(
            "/osmosis.poolincentives.v1beta1.Query/LockableDurations",
            query_lockable_durations_request,
            QueryLockableDurationsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def incentivized_pools(
        self,
        query_incentivized_pools_request: "QueryIncentivizedPoolsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryIncentivizedPoolsResponse":
        return await self._unary_unary(
            "/osmosis.poolincentives.v1beta1.Query/IncentivizedPools",
            query_incentivized_pools_request,
            QueryIncentivizedPoolsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def external_incentive_gauges(
        self,
        query_external_incentive_gauges_request: "QueryExternalIncentiveGaugesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryExternalIncentiveGaugesResponse":
        return await self._unary_unary(
            "/osmosis.poolincentives.v1beta1.Query/ExternalIncentiveGauges",
            query_external_incentive_gauges_request,
            QueryExternalIncentiveGaugesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def gauge_ids(
        self, query_gauge_ids_request: "QueryGaugeIdsRequest"
    ) -> "QueryGaugeIdsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def distr_info(
        self, query_distr_info_request: "QueryDistrInfoRequest"
    ) -> "QueryDistrInfoResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def lockable_durations(
        self, query_lockable_durations_request: "QueryLockableDurationsRequest"
    ) -> "QueryLockableDurationsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def incentivized_pools(
        self, query_incentivized_pools_request: "QueryIncentivizedPoolsRequest"
    ) -> "QueryIncentivizedPoolsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def external_incentive_gauges(
        self,
        query_external_incentive_gauges_request: "QueryExternalIncentiveGaugesRequest",
    ) -> "QueryExternalIncentiveGaugesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_gauge_ids(
        self,
        stream: "grpclib.server.Stream[QueryGaugeIdsRequest, QueryGaugeIdsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.gauge_ids(request)
        await stream.send_message(response)

    async def __rpc_distr_info(
        self,
        stream: "grpclib.server.Stream[QueryDistrInfoRequest, QueryDistrInfoResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.distr_info(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_lockable_durations(
        self,
        stream: "grpclib.server.Stream[QueryLockableDurationsRequest, QueryLockableDurationsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.lockable_durations(request)
        await stream.send_message(response)

    async def __rpc_incentivized_pools(
        self,
        stream: "grpclib.server.Stream[QueryIncentivizedPoolsRequest, QueryIncentivizedPoolsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.incentivized_pools(request)
        await stream.send_message(response)

    async def __rpc_external_incentive_gauges(
        self,
        stream: "grpclib.server.Stream[QueryExternalIncentiveGaugesRequest, QueryExternalIncentiveGaugesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.external_incentive_gauges(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.poolincentives.v1beta1.Query/GaugeIds": grpclib.const.Handler(
                self.__rpc_gauge_ids,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryGaugeIdsRequest,
                QueryGaugeIdsResponse,
            ),
            "/osmosis.poolincentives.v1beta1.Query/DistrInfo": grpclib.const.Handler(
                self.__rpc_distr_info,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDistrInfoRequest,
                QueryDistrInfoResponse,
            ),
            "/osmosis.poolincentives.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/osmosis.poolincentives.v1beta1.Query/LockableDurations": grpclib.const.Handler(
                self.__rpc_lockable_durations,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryLockableDurationsRequest,
                QueryLockableDurationsResponse,
            ),
            "/osmosis.poolincentives.v1beta1.Query/IncentivizedPools": grpclib.const.Handler(
                self.__rpc_incentivized_pools,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryIncentivizedPoolsRequest,
                QueryIncentivizedPoolsResponse,
            ),
            "/osmosis.poolincentives.v1beta1.Query/ExternalIncentiveGauges": grpclib.const.Handler(
                self.__rpc_external_incentive_gauges,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryExternalIncentiveGaugesRequest,
                QueryExternalIncentiveGaugesResponse,
            ),
        }
