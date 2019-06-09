class Rocket:
    ### TODO: add decent info here once we know what we need. ###
    def __init__(self, options):
        self.dry_mass = options.get('dry_mass') if 'dry_mass' in options else 0.0
        self.fuel_mass = options.get('fuel_mass') if 'fuel_mass' in options else 0.0
    def __repr__(self):
        pass
    
    def __str__(self):
        pass