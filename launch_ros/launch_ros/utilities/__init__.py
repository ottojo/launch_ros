# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module for descriptions of launchable entities.

Descriptions are not executable and are immutable so they can be reused by launch entities.
"""

from ._evaluate_parameters import evaluate_parameters
from ._evaluate_parameters import evaluate_parameter_dict
from ._lifecycle_event_manager import LifecycleEventManager
from ._namespace_utils import is_namespace_absolute
from ._namespace_utils import is_root_namespace
from ._namespace_utils import make_namespace_absolute
from ._namespace_utils import prefix_namespace
from ._normalize_parameters import normalize_parameters
from ._normalize_parameters import normalize_parameter_dict
from ._normalize_remap_rule import normalize_remap_rule
from ._normalize_remap_rule import normalize_remap_rules
from ._to_parameters_list import to_parameters_list
from ._track_node_names import add_node_name
from ._track_node_names import get_node_name_count

__all__ = [
    'add_node_name',
    'evaluate_parameters',
    'evaluate_parameter_dict',
    'get_node_name_count',
    'is_namespace_absolute',
    'is_root_namespace',
    'LifecycleEventManager',
    'make_namespace_absolute',
    'normalize_parameters',
    'normalize_parameter_dict',
    'normalize_remap_rule',
    'normalize_remap_rules',
    'prefix_namespace',
    'to_parameters_list',
]
