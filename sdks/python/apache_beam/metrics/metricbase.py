#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
The classes in this file are interfaces for metrics. They are not intended
to be subclassed or created directly by users. To work with and access metrics,
users should use the classes and methods exposed in metric.py.

Available classes:

- Metric - Base interface of a metrics object.
- Counter - Counter metric interface. Allows a count to be incremented or
    decremented during pipeline execution.
- Distribution - Distribution Metric interface. Allows statistics about the
    distribution of a variable to be collected during pipeline execution.
- MetricName - Namespace and name used to refer to a Metric.
"""

__all__ = ['Metric', 'Counter', 'Distribution', 'MetricName']


class MetricName(object):
  """The name of a metric.

  The name of a metric consists of a namespace and a name. The namespace
  allows grouping related metrics together and also prevents collisions
  between multiple metrics of the same name.
  """
  def __init__(self, namespace, name):
    """Initializes ``MetricName``.

    Args:
      namespace: A string with the namespace of a metric.
      name: A string with the name of a metric.
    """
    self.namespace = namespace
    self.name = name

  def __eq__(self, other):
    return (self.namespace == other.namespace and
            self.name == other.name)

  def __str__(self):
    return 'MetricName(namespace={}, name={})'.format(
        self.namespace, self.name)

  def __hash__(self):
    return hash((self.namespace, self.name))


class Metric(object):
  """Base interface of a metric object."""
  pass


class Counter(Metric):
  """Counter metric interface. Allows a count to be incremented/decremented
  during pipeline execution."""
  def inc(self, n=1):
    raise NotImplementedError

  def dec(self, n=1):
    self.inc(-n)


class Distribution(Metric):
  """Distribution Metric interface. Allows statistics about the
    distribution of a variable to be collected during pipeline execution."""
  def update(self, value):
    raise NotImplementedError
