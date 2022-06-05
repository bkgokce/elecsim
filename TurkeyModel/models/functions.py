#from elecsim
def _plant_type_synchronisation(self):
        """
        Function to match the power plant type plant_type of the UK power plant database with the UK power plant cost database
        :return: Returns modified power plant database
        """
        self.plant_db['Simplified_Type'] = self.plant_db['Fuel'].map(lambda x:
                                                             "Biomass" if "Meat" == x
                                                             else "Offshore" if "Wind (offshore)" == x
                                                             else "Biomass" if "Biomass_poultry_litter" == x
                                                             else "Biomass" if "Straw" == x
                                                             else "Recip_diesel" if "Diesel" == x
                                                             else "Biomass" if "Biomass_wood" == x
                                                             else "Recip_gas" if "Gas" == x
                                                             else "PV" if "Solar" == x
                                                             else "OCGT" if "Gas oil" == x
                                                             else "EfW" if "Waste" == x
                                                             else "Hydro_Store" if "Pumped storage" == x
                                                             else "Onshore" if "Wind" == x
                                                             else x)

