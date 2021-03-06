#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from functional.common import test


class AvailabilityZoneTests(test.TestCase):
    """Functional tests for availability zone. """
    HEADERS = ["'Zone Name'"]
    # So far, all components have the same default availability zone name.
    DEFAULT_AZ_NAME = 'nova'

    def test_availability_zone_list(self):
        opts = self.get_opts(self.HEADERS)
        raw_output = self.openstack('availability zone list' + opts)
        self.assertIn(self.DEFAULT_AZ_NAME, raw_output)
