# Standard library imports
import configparser


class ConfigLoader:
    """ A class that loads a specific configuration file.

        Any instance of this class provides a public
        get_item function that retrieves the values of
        a requested configuration item.
    """

    def __init__(self, config_file):
        self.config = self._load_configuration(config_file)

    def _load_configuration(self, config_file):
        """ Load the configuration file.

            Args:
                config_file: The path to the config file.

            Returns:
                A ConfigParser object.

            Raises:
                FileNotFoundError: If config_file was not found.
        """

        config = configparser.ConfigParser()

        dataset = config.read(config_file)

        # If the config_file is not found, dataset will be empty
        if not dataset:
            raise FileNotFoundError("Failed to open file: " + config_file)

        return config

    def get_item(self, config_item):
        """ Get the value of an item from the config file.
            Values can be separated by commas.

            Args:
                config_item: Name of the item to look up.

            Returns:
                A list of one or more values for the requested item.
        """

        config_item = self.config.get('parameters', config_item)

        if config_item.find(',') != -1:
            # This is a string with comma separated items.
            # Convert to a list
            config_item = config_item.split(',')
            # Strip spaces in case of multiline values.
            config_item = [item.strip() for item in config_item]

        return config_item