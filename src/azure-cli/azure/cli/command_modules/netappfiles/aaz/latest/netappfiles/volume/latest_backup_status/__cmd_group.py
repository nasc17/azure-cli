# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "netappfiles volume latest-backup-status",
)
class __CMDGroup(AAZCommandGroup):
    """Get the latest backup status of a volume
    """
    pass


__all__ = ["__CMDGroup"]
