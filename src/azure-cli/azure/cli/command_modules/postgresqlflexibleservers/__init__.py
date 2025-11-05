# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType
from azure.cli.core.profiles import ResourceType
import azure.cli.command_modules.postgresqlflexibleservers._help  # pylint: disable=unused-import


# pylint: disable=import-outside-toplevel
class PostgresqlFlexibleServersCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):

        postgres_flexible_custom = CliCommandType(
            operations_tmpl='azure.cli.command_modules.postgresqlflexibleservers.flexible_server_custom_postgres#{}')
        super().__init__(
            cli_ctx=cli_ctx,
            resource_type=ResourceType.MGMT_RDBMS,
            custom_command_type=postgres_flexible_custom)

    def load_command_table(self, args):
        from azure.cli.core.aaz import load_aaz_command_table
        try:
            from . import aaz
        except ImportError:
            aaz = None
        if aaz:
            load_aaz_command_table(
                loader=self,
                aaz_pkg_name=aaz.__name__,
                args=args
            )

        from azure.cli.command_modules.postgresqlflexibleservers.flexible_server_commands import load_flexibleserver_command_table
        load_flexibleserver_command_table(self, args)

        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.postgresqlflexibleservers._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = PostgresqlFlexibleServersCommandsLoader
