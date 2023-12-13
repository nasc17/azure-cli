# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network public-ip prefix list",
)
class List(AAZCommand):
    """List public IP prefix resources.

    :example: List public IP prefix resource.
        az network public-ip prefix list --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.network/publicipprefixes", "2022-09-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/publicipprefixes", "2022-09-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.PublicIPPrefixesList(ctx=self.ctx)()
        if condition_1:
            self.PublicIPPrefixesListAll(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class PublicIPPrefixesList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _element.id = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )
            _element.zones = AAZListType()

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.custom_ip_prefix = AAZObjectType(
                serialized_name="customIPPrefix",
            )
            _ListHelper._build_schema_sub_resource_read(properties.custom_ip_prefix)
            properties.ip_prefix = AAZStrType(
                serialized_name="ipPrefix",
                flags={"read_only": True},
            )
            properties.ip_tags = AAZListType(
                serialized_name="ipTags",
            )
            properties.load_balancer_frontend_ip_configuration = AAZObjectType(
                serialized_name="loadBalancerFrontendIpConfiguration",
            )
            _ListHelper._build_schema_sub_resource_read(properties.load_balancer_frontend_ip_configuration)
            properties.nat_gateway = AAZObjectType(
                serialized_name="natGateway",
            )
            properties.prefix_length = AAZIntType(
                serialized_name="prefixLength",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address_version = AAZStrType(
                serialized_name="publicIPAddressVersion",
            )
            properties.public_ip_addresses = AAZListType(
                serialized_name="publicIPAddresses",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )

            ip_tags = cls._schema_on_200.value.Element.properties.ip_tags
            ip_tags.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ip_tags.Element
            _element.ip_tag_type = AAZStrType(
                serialized_name="ipTagType",
            )
            _element.tag = AAZStrType()

            nat_gateway = cls._schema_on_200.value.Element.properties.nat_gateway
            nat_gateway.etag = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.id = AAZStrType()
            nat_gateway.location = AAZStrType()
            nat_gateway.name = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            nat_gateway.sku = AAZObjectType()
            nat_gateway.tags = AAZDictType()
            nat_gateway.type = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.zones = AAZListType()

            properties = cls._schema_on_200.value.Element.properties.nat_gateway.properties
            properties.idle_timeout_in_minutes = AAZIntType(
                serialized_name="idleTimeoutInMinutes",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_addresses = AAZListType(
                serialized_name="publicIpAddresses",
            )
            properties.public_ip_prefixes = AAZListType(
                serialized_name="publicIpPrefixes",
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.subnets = AAZListType(
                flags={"read_only": True},
            )

            public_ip_addresses = cls._schema_on_200.value.Element.properties.nat_gateway.properties.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(public_ip_addresses.Element)

            public_ip_prefixes = cls._schema_on_200.value.Element.properties.nat_gateway.properties.public_ip_prefixes
            public_ip_prefixes.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(public_ip_prefixes.Element)

            subnets = cls._schema_on_200.value.Element.properties.nat_gateway.properties.subnets
            subnets.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(subnets.Element)

            sku = cls._schema_on_200.value.Element.properties.nat_gateway.sku
            sku.name = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.nat_gateway.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.properties.nat_gateway.zones
            zones.Element = AAZStrType()

            public_ip_addresses = cls._schema_on_200.value.Element.properties.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.public_ip_addresses.Element
            _element.id = AAZStrType()

            sku = cls._schema_on_200.value.Element.sku
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200

    class PublicIPPrefixesListAll(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Network/publicIPPrefixes",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _element.id = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )
            _element.zones = AAZListType()

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.custom_ip_prefix = AAZObjectType(
                serialized_name="customIPPrefix",
            )
            _ListHelper._build_schema_sub_resource_read(properties.custom_ip_prefix)
            properties.ip_prefix = AAZStrType(
                serialized_name="ipPrefix",
                flags={"read_only": True},
            )
            properties.ip_tags = AAZListType(
                serialized_name="ipTags",
            )
            properties.load_balancer_frontend_ip_configuration = AAZObjectType(
                serialized_name="loadBalancerFrontendIpConfiguration",
            )
            _ListHelper._build_schema_sub_resource_read(properties.load_balancer_frontend_ip_configuration)
            properties.nat_gateway = AAZObjectType(
                serialized_name="natGateway",
            )
            properties.prefix_length = AAZIntType(
                serialized_name="prefixLength",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address_version = AAZStrType(
                serialized_name="publicIPAddressVersion",
            )
            properties.public_ip_addresses = AAZListType(
                serialized_name="publicIPAddresses",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )

            ip_tags = cls._schema_on_200.value.Element.properties.ip_tags
            ip_tags.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ip_tags.Element
            _element.ip_tag_type = AAZStrType(
                serialized_name="ipTagType",
            )
            _element.tag = AAZStrType()

            nat_gateway = cls._schema_on_200.value.Element.properties.nat_gateway
            nat_gateway.etag = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.id = AAZStrType()
            nat_gateway.location = AAZStrType()
            nat_gateway.name = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            nat_gateway.sku = AAZObjectType()
            nat_gateway.tags = AAZDictType()
            nat_gateway.type = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.zones = AAZListType()

            properties = cls._schema_on_200.value.Element.properties.nat_gateway.properties
            properties.idle_timeout_in_minutes = AAZIntType(
                serialized_name="idleTimeoutInMinutes",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_addresses = AAZListType(
                serialized_name="publicIpAddresses",
            )
            properties.public_ip_prefixes = AAZListType(
                serialized_name="publicIpPrefixes",
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.subnets = AAZListType(
                flags={"read_only": True},
            )

            public_ip_addresses = cls._schema_on_200.value.Element.properties.nat_gateway.properties.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(public_ip_addresses.Element)

            public_ip_prefixes = cls._schema_on_200.value.Element.properties.nat_gateway.properties.public_ip_prefixes
            public_ip_prefixes.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(public_ip_prefixes.Element)

            subnets = cls._schema_on_200.value.Element.properties.nat_gateway.properties.subnets
            subnets.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(subnets.Element)

            sku = cls._schema_on_200.value.Element.properties.nat_gateway.sku
            sku.name = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.nat_gateway.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.properties.nat_gateway.zones
            zones.Element = AAZStrType()

            public_ip_addresses = cls._schema_on_200.value.Element.properties.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.public_ip_addresses.Element
            _element.id = AAZStrType()

            sku = cls._schema_on_200.value.Element.sku
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.value.Element.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["List"]
