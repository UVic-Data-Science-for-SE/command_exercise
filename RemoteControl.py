class RemoteControl:
    """
    RemoteControl sends Commands via the Command Pattern to the ColorChangingLightPanels.
    """

    def __init__(self):
        ColorChangingLightPanels = ColorChangingLightPanels(0.0, "white")


if __name__ == "__main__":
    # Create a RemoteControl
    remoteControl = RemoteControl()

    # Create a Command
    command = None

    # Set the Command for the RemoteControl
    remoteControl.setCommand(command)

    # Invoke the Command
    
