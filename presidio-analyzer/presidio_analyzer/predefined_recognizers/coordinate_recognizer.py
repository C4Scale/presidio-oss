from typing import Optional, List, Tuple

from presidio_analyzer import Pattern, PatternRecognizer


class InPanRecognizer(PatternRecognizer):
    """
    Recognizes coordinates.

    
    Coordinates are a means of specifying a location's precise position on Earth's surface. 
    They comprise two primary values: latitude, which measures north-south position, and longitude, which indicates east-west position.
    Latitude ranges from -90° at the South Pole to 90° at the North Pole, with the equator at 0°. 
    Longitude ranges from -180° to 180°, with the Prime Meridian at 0°.
    These coordinates can be represented in various formats, including decimal degrees and degrees, minutes, seconds, 
    and are used in fields such as navigation, cartography, and geographic information systems (GIS).

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [

        Pattern(
            "Latitude (degrees, decimal) (low)",
            r"\b(-?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?)[°]?\s*[NnSs]|(?i)L(at)?|T)\b",
            0.3,
        ),

        Pattern(
            "Latitude (DMS) (low)",
            r"\b(-?(?:[0-8]\d|90)(?:[° ](?:[0-5]\d|[0-9])(?:'[0-5]\d(?:\.\d+)?\"[NSns]?)?))\b",
            0.3,
        ),

        Pattern(
            "Longitude (degrees, decimal) (low)",
            r"\b(-?(?:\d{1,2}(?:\.\d+)?|1[0-7]\d(?:\.\d+)?|180(?:\.0+)?)[°]?[EWew]?)\b",
            0.3,
        ),
        

        Pattern(
            "Longitude (DMS) (low)",
            r"\b(-?(?:\d{1,2}|1[0-7]\d|180)(?:[° ](?:[0-5]\d|[0-9])(?:'[0-5]\d(?:\.\d+)?\"[EWew]?)?))\b",
            0.3,
        ),

    ]

    CONTEXT = [
        "coordinates",
        "latitude",
        "longitude",
        "GPS coordinates",
        "GPS",
        "location",
        "adress",
        "mapping coordinates",
        "geographical positions",
    ]


    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "IN_PAN",
        replacement_pairs: Optional[List[Tuple[str, str]]] = None,
    ):
        self.replacement_pairs = (
            replacement_pairs if replacement_pairs else [("-", ""), (" ", "")]
        )
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
