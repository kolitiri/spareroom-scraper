# Standard library imports
from calendar import monthrange
import datetime
import time

# Local imports
from spareroomScraper.config_loader import ConfigLoader


class Payload:
    """ A class that sets up the payload in the form
        of a dictionary, on initialization.

        The dictionary can be accessed by instantiating
        the class and calling the public function:
        get_advanced_search_payload
    """

    def __init__(self, config_file):
        """ Load the configuration file and initialise the payload.

            Initialisation has been split in several 'private' functions.
            Each one is setting up a specific category of the search
            attributes. The private functions also perform validation
            of the config items and set up default values.

            Args:
                config_file: The path to the config file.
        """

        # Create a new instance of the ConfigLoader class
        self.config_loader = ConfigLoader(config_file)

        # Set up the payload values by category
        self._set_search_and_location_details()
        self._set_property_preferences()
        self._set_sharing_preferences()
        self._set_other_search_options()
        self._set_additional_details()

    def _get_item(self, config_item):
        """ Get the value of an item from the config file.
            Calls get_item of ConfigLoader class.

            Args:
                config_item: Name of the item to look up.

            Returns:
                A list of one or more values for the requested item.
        """

        config_item = self.config_loader.get_item(config_item)

        return config_item

    def _set_search_and_location_details(self):
        """ Initialise the payload attributes for the
            "Search and Location details" section.
        """

        flatshare_type = self._get_item('flatshare_type')
        flatshare_type_options = self._get_item('flatshare_type_options')
        flatshare_type_default = self._get_item('flatshare_type')

        search = self._get_item('search')

        location_type = self._get_item('location_type')
        location_type_options = self._get_item('location_type_options')
        location_type_default = self._get_item('location_type_default')

        min_zone = self._get_item('min_zone')
        min_zone_options = self._get_item('min_zone_options')
        min_zone_default = self._get_item('min_zone_default')
        max_zone = self._get_item('max_zone')
        max_zone_options = self._get_item('max_zone_options')
        max_zone_default = self._get_item('max_zone_default')

        tube_line = self._get_item('tube_line')
        tube_line_options = self._get_item('tube_line_options')
        tube_line_default = self._get_item('tube_line_default')

        max_commute_time = self._get_item('max_commute_time')
        max_commute_time_options = self._get_item('max_commute_time_options')
        max_commute_time_default = self._get_item('max_commute_time_default')

        station_id = self._get_item('station_id')
        station_id_options = self._get_item('station_id_options')
        station_id_default = self._get_item('station_id_default')

        miles_from_max = self._get_item('miles_from_max')
        miles_from_max_options = self._get_item('miles_from_max_options')
        miles_from_max_default = self._get_item('miles_from_max_default')

        showme_rooms = self._get_item('showme_rooms')
        showme_rooms_options = self._get_item('showme_rooms_options')
        showme_rooms_default = self._get_item('showme_rooms_default')

        showme_1beds = self._get_item('showme_1beds')
        showme_1beds_options = self._get_item('showme_1beds_options')
        showme_1beds_default = self._get_item('showme_1beds_default')

        showme_buddyup_properties = self._get_item('showme_buddyup_properties')
        showme_buddyup_properties_options = self._get_item('showme_buddyup_properties_options')
        showme_buddyup_properties_default = self._get_item('showme_buddyup_properties_default')

        # Validate and set up the values. Some values can only be
        # present on specific circumstances.
        if flatshare_type in flatshare_type_options:
            self.flatshare_type = flatshare_type
        else:
            self.flatshare_type = flatshare_type_default

        if self.flatshare_type == 'offered':
            if location_type in location_type_options:
                self.location_type = location_type
            else:
                self.location_type = location_type_default

            if self.location_type == 'zone':
                if min_zone in min_zone_options:
                    self.min_zone = min_zone
                else:
                    self.min_zone = min_zone_default

                if max_zone in max_zone_options:
                    self.max_zone = max_zone
                else:
                    self.max_zone = max_zone_default

            elif self.location_type == 'tube':
                if tube_line in tube_line_options:
                    self.tube_line = tube_line
                else:
                    self.tube_line = tube_line_default

            elif self.location_type == 'commuter':
                if max_commute_time in max_commute_time_options:
                    self.max_commute_time = max_commute_time
                else:
                    self.max_commute_time = max_commute_default

                if station_id in station_id_options:
                    self.station_id = station_id
                else:
                    self.station_id = station_id_default

            elif self.location_type == 'area':
                if miles_from_max in miles_from_max_options:
                    self.miles_from_max = miles_from_max
                else:
                    self.miles_from_max = miles_from_max_default

                if search:
                    self.search = search
                else:
                    print('Please provide a postcode (SEARCH variable)')

            if showme_rooms in showme_rooms_options:
                self.showme_rooms = showme_rooms
            else:
                self.showme_rooms = showme_rooms_default

            if showme_1beds in showme_1beds_options:
                self.showme_1beds = showme_1beds
            else:
                self.showme_1beds = showme_1beds_default

            if showme_buddyup_properties in showme_buddyup_properties_options:
                self.showme_buddyup_properties = showme_buddyup_properties
            else:
                self.showme_buddyup_properties = showme_buddyup_properties_default

        else:
            if search:
                self.search = search
            else:
                print('Please provide a postcode (SEARCH variable)')

    def _set_property_preferences(self):
        """ Initialise the payload attributes for the
            "Property Preferences" section.
        """

        min_rent = self._get_item('min_rent')
        min_rent_default = self._get_item('min_rent_default')

        max_rent = self._get_item('max_rent')
        max_rent_default = self._get_item('max_rent_default')

        per = self._get_item('per')
        per_options = self._get_item('per_options')
        per_default = self._get_item('per_default')

        bills_inc = self._get_item('bills_inc')
        bills_inc_options = self._get_item('bills_inc_options')
        bills_inc_default = self._get_item('bills_inc_default')

        rooms_for = self._get_item('rooms_for')
        rooms_for_options = self._get_item('rooms_for_options')
        rooms_for_default = self._get_item('rooms_for_default')

        room_types = self._get_item('room_types')
        room_types_options = self._get_item('room_types_options')
        room_types_default = self._get_item('room_types_default')

        ensuite = self._get_item('ensuite')
        ensuite_options = self._get_item('ensuite_options')
        ensuite_default = self._get_item('ensuite_default')

        living_room = self._get_item('living_room')
        living_room_options = self._get_item('living_room_options')
        living_room_default = self._get_item('living_room_default')

        smoking = self._get_item('smoking')
        smoking_options = self._get_item('smoking_options')
        smoking_default = self._get_item('smoking_default')

        min_term = self._get_item('min_term')
        min_term_options = self._get_item('min_term_options')
        min_term_default = self._get_item('min_term_default')

        max_term = self._get_item('max_term')
        max_term_options = self._get_item('max_term_options')
        max_term_default = self._get_item('max_term_default')

        available_search = self._get_item('available_search')
        available_search_options = self._get_item('available_search_options')
        available_search_default = self._get_item('available_search_default')

        now = datetime.datetime.now()
        year_avail = int(self._get_item('year_avail'))
        year_avail_default = now.year

        month_avail = int(self._get_item('month_avail'))
        month_avail_default = now.month

        day_avail = int(self._get_item('day_avail'))
        day_avail_default = now.day

        # Validate and set up the values. Some values can only be
        # present on specific circumstances.
        if int(min_rent) in range(1, 10000):
            self.min_rent = min_rent
        else:
            self.min_rent = min_rent_default

        if int(max_rent) in range(1, 10000):
            self.max_rent = max_rent
        else:
            self.max_rent = max_rent_default

        if per in per_options:
            self.per = per
        else:
            self.per = per_default

        if bills_inc in bills_inc_options:
            self.bills_inc = bills_inc
        else:
            self.bills_inc = bills_inc_default

        if rooms_for in rooms_for_options:
            self.rooms_for = rooms_for
        else:
            self.rooms_for = rooms_for_default

        if room_types in room_types_options:
            self.room_types = room_types
        else:
            self.room_types = room_types_default        

        if ensuite in ensuite_options:
            self.ensuite = ensuite
        else:
            self.ensuite = ensuite_default  

        if living_room in living_room_options:
            self.living_room = living_room
        else:
            self.living_room = living_room_default

        if smoking in smoking_options:
            self.smoking = smoking
        else:
            self.smoking = smoking_default  

        if min_term in min_term_options:
            self.min_term = min_term
        else:
            self.min_term = min_term_default    

        if max_term in max_term_options:
            self.max_term = max_term
        else:
            self.max_term = max_term_default    

        if available_search in available_search_options:
            self.available_search = available_search

            if year_avail in range(now.year, 2200):
                self.year_avail = year_avail
            else:
                self.year_avail = year_avail_default

            if month_avail in range(1, 13):
                self.month_avail = month_avail
            else:
                self.month_avail = month_avail_default

            if day_avail in range(1, monthrange(self.year_avail, self.month_avail)[1]):
                self.day_avail = day_avail
            else:
                self.day_avail = day_avail_default
        else:
            self.available_search = available_search_default

    def _set_sharing_preferences(self):
        """ Initialise the payload attributes for the
            "Sharing Preferences" section.
        """

        share_type = self._get_item('share_type')
        share_type_options = self._get_item('share_type_options')
        share_type_default = self._get_item('share_type_default')

        genderfilter = self._get_item('genderfilter')
        genderfilter_options = self._get_item('genderfilter_options')
        genderfilter_default = self._get_item('genderfilter_default')

        min_age_req = self._get_item('min_age_req')
        min_age_req_default = self._get_item('min_age_req_default')

        max_age_req = self._get_item('max_age_req')
        max_age_req_default = self._get_item('max_age_req_default')

        min_beds = self._get_item('min_beds')
        min_beds_options = self._get_item('min_beds_options')
        min_beds_default = self._get_item('min_beds_default')

        max_beds = self._get_item('max_beds')
        max_beds_options = self._get_item('max_beds_options')
        max_beds_default = self._get_item('max_beds_default')

        landlord = self._get_item('landlord')
        landlord_options = self._get_item('landlord_options')
        landlord_default = self._get_item('landlord_default')

        lgbtShare = self._get_item('lgbtShare')
        lgbtShare_options = self._get_item('lgbtShare_options')
        lgbtShare_default = self._get_item('lgbtShare_default')

        # Validate and set up the values. Some values can only be
        # present on specific circumstances.
        if share_type in share_type_options:
            self.share_type = share_type
        else:
            self.share_type = share_type_default

        if genderfilter in genderfilter_options:
            self.genderfilter = genderfilter
        else:
            self.genderfilter = genderfilter_default

        if int(min_age_req) in range(1,999):
            self.min_age_req = min_age_req
        else:
            self.min_age_req = min_age_req_default

        if int(max_age_req) in range(1,999):
            self.max_age_req = max_age_req
        else:
            self.max_age_req = max_age_req_default

        if min_beds in min_beds_options:
            self.min_beds = min_beds
        else:
            self.min_beds = min_beds_default

        if max_beds in max_beds_options:
            self.max_beds = max_beds
        else:
            self.max_beds = max_beds_default

        if landlord in landlord_options:
            self.landlord = landlord
        else:
            self.landlord = landlord_default

        if lgbtShare in lgbtShare_options:
            self.lgbtShare = lgbtShare
        else:
            self.lgbtShare = lgbtShare_default


    def _set_other_search_options(self):
        """ Initialise the payload attributes for the
            "Other Search Options" section.
        """

        pets_req = self._get_item('pets_req')
        pets_req_options = self._get_item('pets_req_options')
        pets_req_default = self._get_item('pets_req_default')

        parking = self._get_item('parking')
        parking_options = self._get_item('parking_options')
        parking_default = self._get_item('parking_default')

        photoadsonly = self._get_item('photoadsonly')
        photoadsonly_options = self._get_item('photoadsonly_options')
        photoadsonly_default = self._get_item('photoadsonly_default')

        vegetarians = self._get_item('vegetarians')
        vegetarians_options = self._get_item('vegetarians_options')
        vegetarians_default = self._get_item('vegetarians_default')

        short_lets_considered = self._get_item('short_lets_considered')
        short_lets_considered_options = self._get_item('short_lets_considered_options')
        short_lets_considered_default = self._get_item('short_lets_considered_default')

        dss = self._get_item('dss')
        dss_options = self._get_item('dss_options')
        dss_default = self._get_item('dss_default')

        disabled_access = self._get_item('disabled_access')
        disabled_access_options = self._get_item('disabled_access_options')
        disabled_access_default = self._get_item('disabled_access_default')

        days_of_wk_available = self._get_item('days_of_wk_available')
        days_of_wk_available_options = self._get_item('days_of_wk_available_options')
        days_of_wk_available_default = self._get_item('days_of_wk_available_default')

        posted_by = self._get_item('posted_by')
        posted_by_options = self._get_item('posted_by_options')
        posted_by_default = self._get_item('posted_by_default')

        # Validate and set up the values. Some values can only be
        # present on specific circumstances.
        if pets_req in pets_req_options:
            self.pets_req = pets_req
        else:
            self.pets_req = pets_req_default

        if parking in parking_options:
            self.parking = parking
        else:
            self.parking = parking_default

        if photoadsonly in photoadsonly_options:
            self.photoadsonly = photoadsonly
        else:
            self.photoadsonly = photoadsonly_default

        if vegetarians in vegetarians_options:
            self.vegetarians = vegetarians
        else:
            self.vegetarians = vegetarians_default

        if short_lets_considered in short_lets_considered_options:
            self.short_lets_considered = short_lets_considered
        else:
            self.short_lets_considered = short_lets_considered_default

        if dss in dss_options:
            self.dss = dss
        else:
            self.dss = dss_default

        if disabled_access in disabled_access_options:
            self.disabled_access = disabled_access
        else:
            self.disabled_access = disabled_access_default

        if days_of_wk_available in days_of_wk_available_options:
            self.days_of_wk_available = days_of_wk_available
        else:
            self.days_of_wk_available = days_of_wk_available_default

        if posted_by in posted_by_options:
            self.posted_by = posted_by
        else:
            self.posted_by = posted_by_default

    def _set_additional_details(self):
        """ Initialise a few additional payload attributes. """

        self.searchtype = 'advanced'
        self.action = 'search'
        self.show_results = ''
        self.max_per_page = ''
        self.keyword = ''
        self.editing = ''
        self.mode = ''
        self.nmsq_mode = ''
        self.templateoveride = ''
        self.show_results = ''
        self.max_per_page = ''
        self.submit = ''

    def get_advanced_search_payload(self):
        """ Get the payload for a specific search.

            Returns:
                payload: The payload in the form of a dictionary. 
        """

        payload = self.__dict__

        # We don't need config_loader attribute in the actual payload
        payload.pop('config_loader')

        for p in payload:
            print('{} : {}'.format(p, payload[p]))

        return payload
