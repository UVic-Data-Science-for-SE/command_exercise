class ColorChangingLightPanels:
    """
    Represents a color-changing device that can be controlled using Commands.
    :param brightness: brightness of the light panels; larger is brighter
    :param color: color of the light panels
    """ 
    def __init__(self, brightness: float, color: str):
        self.brightness = brightness
        self.color = color
        self.on = False

    def getBrightness(self) -> float:
        return self.brightness

    def setBrightness(self, brightness: float):
        self.brightness = brightness

    def getColor(self) -> str:
        return self.color

    def setColor(self, color: str):
        self.color = color

    def isOn(self) -> bool:
        return self.on

    def setOn(self, on: bool):
        self.on = on