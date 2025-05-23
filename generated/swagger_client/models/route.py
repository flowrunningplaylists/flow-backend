# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Route(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'athlete': 'SummaryAthlete',
        'description': 'str',
        'distance': 'float',
        'elevation_gain': 'float',
        'id': 'int',
        'id_str': 'str',
        'map': 'PolylineMap',
        'name': 'str',
        'private': 'bool',
        'starred': 'bool',
        'timestamp': 'int',
        'type': 'int',
        'sub_type': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'estimated_moving_time': 'int',
        'segments': 'list[SummarySegment]',
        'waypoints': 'list[Waypoint]'
    }

    attribute_map = {
        'athlete': 'athlete',
        'description': 'description',
        'distance': 'distance',
        'elevation_gain': 'elevation_gain',
        'id': 'id',
        'id_str': 'id_str',
        'map': 'map',
        'name': 'name',
        'private': 'private',
        'starred': 'starred',
        'timestamp': 'timestamp',
        'type': 'type',
        'sub_type': 'sub_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'estimated_moving_time': 'estimated_moving_time',
        'segments': 'segments',
        'waypoints': 'waypoints'
    }

    def __init__(self, athlete=None, description=None, distance=None, elevation_gain=None, id=None, id_str=None, map=None, name=None, private=None, starred=None, timestamp=None, type=None, sub_type=None, created_at=None, updated_at=None, estimated_moving_time=None, segments=None, waypoints=None):  # noqa: E501
        """Route - a model defined in Swagger"""  # noqa: E501

        self._athlete = None
        self._description = None
        self._distance = None
        self._elevation_gain = None
        self._id = None
        self._id_str = None
        self._map = None
        self._name = None
        self._private = None
        self._starred = None
        self._timestamp = None
        self._type = None
        self._sub_type = None
        self._created_at = None
        self._updated_at = None
        self._estimated_moving_time = None
        self._segments = None
        self._waypoints = None
        self.discriminator = None

        if athlete is not None:
            self.athlete = athlete
        if description is not None:
            self.description = description
        if distance is not None:
            self.distance = distance
        if elevation_gain is not None:
            self.elevation_gain = elevation_gain
        if id is not None:
            self.id = id
        if id_str is not None:
            self.id_str = id_str
        if map is not None:
            self.map = map
        if name is not None:
            self.name = name
        if private is not None:
            self.private = private
        if starred is not None:
            self.starred = starred
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if estimated_moving_time is not None:
            self.estimated_moving_time = estimated_moving_time
        if segments is not None:
            self.segments = segments
        if waypoints is not None:
            self.waypoints = waypoints

    @property
    def athlete(self):
        """Gets the athlete of this Route.  # noqa: E501


        :return: The athlete of this Route.  # noqa: E501
        :rtype: SummaryAthlete
        """
        return self._athlete

    @athlete.setter
    def athlete(self, athlete):
        """Sets the athlete of this Route.


        :param athlete: The athlete of this Route.  # noqa: E501
        :type: SummaryAthlete
        """

        self._athlete = athlete

    @property
    def description(self):
        """Gets the description of this Route.  # noqa: E501

        The description of the route  # noqa: E501

        :return: The description of this Route.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Route.

        The description of the route  # noqa: E501

        :param description: The description of this Route.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def distance(self):
        """Gets the distance of this Route.  # noqa: E501

        The route's distance, in meters  # noqa: E501

        :return: The distance of this Route.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Route.

        The route's distance, in meters  # noqa: E501

        :param distance: The distance of this Route.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def elevation_gain(self):
        """Gets the elevation_gain of this Route.  # noqa: E501

        The route's elevation gain.  # noqa: E501

        :return: The elevation_gain of this Route.  # noqa: E501
        :rtype: float
        """
        return self._elevation_gain

    @elevation_gain.setter
    def elevation_gain(self, elevation_gain):
        """Sets the elevation_gain of this Route.

        The route's elevation gain.  # noqa: E501

        :param elevation_gain: The elevation_gain of this Route.  # noqa: E501
        :type: float
        """

        self._elevation_gain = elevation_gain

    @property
    def id(self):
        """Gets the id of this Route.  # noqa: E501

        The unique identifier of this route  # noqa: E501

        :return: The id of this Route.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Route.

        The unique identifier of this route  # noqa: E501

        :param id: The id of this Route.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def id_str(self):
        """Gets the id_str of this Route.  # noqa: E501

        The unique identifier of the route in string format  # noqa: E501

        :return: The id_str of this Route.  # noqa: E501
        :rtype: str
        """
        return self._id_str

    @id_str.setter
    def id_str(self, id_str):
        """Sets the id_str of this Route.

        The unique identifier of the route in string format  # noqa: E501

        :param id_str: The id_str of this Route.  # noqa: E501
        :type: str
        """

        self._id_str = id_str

    @property
    def map(self):
        """Gets the map of this Route.  # noqa: E501


        :return: The map of this Route.  # noqa: E501
        :rtype: PolylineMap
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this Route.


        :param map: The map of this Route.  # noqa: E501
        :type: PolylineMap
        """

        self._map = map

    @property
    def name(self):
        """Gets the name of this Route.  # noqa: E501

        The name of this route  # noqa: E501

        :return: The name of this Route.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Route.

        The name of this route  # noqa: E501

        :param name: The name of this Route.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def private(self):
        """Gets the private of this Route.  # noqa: E501

        Whether this route is private  # noqa: E501

        :return: The private of this Route.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Route.

        Whether this route is private  # noqa: E501

        :param private: The private of this Route.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def starred(self):
        """Gets the starred of this Route.  # noqa: E501

        Whether this route is starred by the logged-in athlete  # noqa: E501

        :return: The starred of this Route.  # noqa: E501
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this Route.

        Whether this route is starred by the logged-in athlete  # noqa: E501

        :param starred: The starred of this Route.  # noqa: E501
        :type: bool
        """

        self._starred = starred

    @property
    def timestamp(self):
        """Gets the timestamp of this Route.  # noqa: E501

        An epoch timestamp of when the route was created  # noqa: E501

        :return: The timestamp of this Route.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Route.

        An epoch timestamp of when the route was created  # noqa: E501

        :param timestamp: The timestamp of this Route.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this Route.  # noqa: E501

        This route's type (1 for ride, 2 for runs)  # noqa: E501

        :return: The type of this Route.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Route.

        This route's type (1 for ride, 2 for runs)  # noqa: E501

        :param type: The type of this Route.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this Route.  # noqa: E501

        This route's sub-type (1 for road, 2 for mountain bike, 3 for cross, 4 for trail, 5 for mixed)  # noqa: E501

        :return: The sub_type of this Route.  # noqa: E501
        :rtype: int
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this Route.

        This route's sub-type (1 for road, 2 for mountain bike, 3 for cross, 4 for trail, 5 for mixed)  # noqa: E501

        :param sub_type: The sub_type of this Route.  # noqa: E501
        :type: int
        """

        self._sub_type = sub_type

    @property
    def created_at(self):
        """Gets the created_at of this Route.  # noqa: E501

        The time at which the route was created  # noqa: E501

        :return: The created_at of this Route.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Route.

        The time at which the route was created  # noqa: E501

        :param created_at: The created_at of this Route.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Route.  # noqa: E501

        The time at which the route was last updated  # noqa: E501

        :return: The updated_at of this Route.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Route.

        The time at which the route was last updated  # noqa: E501

        :param updated_at: The updated_at of this Route.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def estimated_moving_time(self):
        """Gets the estimated_moving_time of this Route.  # noqa: E501

        Estimated time in seconds for the authenticated athlete to complete route  # noqa: E501

        :return: The estimated_moving_time of this Route.  # noqa: E501
        :rtype: int
        """
        return self._estimated_moving_time

    @estimated_moving_time.setter
    def estimated_moving_time(self, estimated_moving_time):
        """Sets the estimated_moving_time of this Route.

        Estimated time in seconds for the authenticated athlete to complete route  # noqa: E501

        :param estimated_moving_time: The estimated_moving_time of this Route.  # noqa: E501
        :type: int
        """

        self._estimated_moving_time = estimated_moving_time

    @property
    def segments(self):
        """Gets the segments of this Route.  # noqa: E501

        The segments traversed by this route  # noqa: E501

        :return: The segments of this Route.  # noqa: E501
        :rtype: list[SummarySegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this Route.

        The segments traversed by this route  # noqa: E501

        :param segments: The segments of this Route.  # noqa: E501
        :type: list[SummarySegment]
        """

        self._segments = segments

    @property
    def waypoints(self):
        """Gets the waypoints of this Route.  # noqa: E501

        The custom waypoints along this route  # noqa: E501

        :return: The waypoints of this Route.  # noqa: E501
        :rtype: list[Waypoint]
        """
        return self._waypoints

    @waypoints.setter
    def waypoints(self, waypoints):
        """Sets the waypoints of this Route.

        The custom waypoints along this route  # noqa: E501

        :param waypoints: The waypoints of this Route.  # noqa: E501
        :type: list[Waypoint]
        """

        self._waypoints = waypoints

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Route, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Route):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
