from vector import Vector

class Rocket:
    ### TODO: A rocket is a container class that represents a collection of other objects: stages and a payload ###
    def __init__(self, pos, coeff_drag, cross_sec_area):
        self.stages = [] # a list that represents the stages
        self.payloads = []
        
        if isinstance(coeff_drag, float):
            if coeff_drag > 0.0:
                self.coeff_drag = coeff_drag
            else:
                raise ValueError
        else:
            raise TypeError
             
        if isinstance(cross_sec_area, float):
            if cross_sec_area > 0.0:
                self.cross_sec_area = cross_sec_area
            else:
                raise ValueError
        else:
            raise TypeError
        
        if isinstance(pos, Vector):
            self.pos = pos
        else:
            raise TypeError
        
        self.momentum = Vector(0,0,0)
        
    def __repr__(self):
        pass
    
    def __str__(self):
        pass
    
    def add_stage(self, stage):
        if isinstance(stage, Stage):
            self.stages.append(stage)
        else:
            raise TypeError
        
    def add_payload(self, payload):
        if isinstance(payload, Payload):
            self.payloads.append(payload)
        else:
            raise TypeError
        
    def get_total_mass():
        total_mass = 0
        for stage in self.stages:
            total_mass += stage.dry_mass + stage.fuel_mass
            
        for payload in self.payloads:
            total_mass += payload.mass
            
        return total_mass
            
    def separate_active_stage(self):
        ### removes the active stage from the rocket and sets the next stage as the active stage.###
        self.stages.pop(0)
        
    def update_total_mass(self, time_step):
        self.stages[0].fuel_mass -= fuel_consumption_rate*time_step
        
        
class Stage:
    ### 
    ### Stage: this class presents a stage. A stage has a dry mass, a fuel mass, a max thrust, and max fuel burn rate. 
    ### options: {
    ###   dry_mass - float - the unfueled mass of the stage.
    ###    fuel_mass - float - the mass of the fuel + oxidizer carried by the stage
    ###    max_thrust_mag - float - the maximum thrust in newtons.
    ###    max_dmdt - float - the maximum rate at which fuel + oxidizer is consumed in kilograms per second
    ### }
    ###
    def __init__(self, options):
        self.dry_mass = options.get('dry_mass') if 'dry_mass' in options else 0.0
        self.fuel_mass = options.get('fuel_mass') if 'fuel_mass' in options else 0.0
        self.max_thrust_mag = options.get('max_thrust_mag') if 'max_thrust_mag' in options else 0.0
        self.max_dmdt = options.get('max_dmdt') if 'max_dmdt' in options else 0.0
        self.throttle = 100 # percentage of stage's mass thrust produced by the engines
        
        # in type check the data
        if isinstance(self.dry_mass, float):
            if self.dry_mass < 0.0:
                raise ValueError
        else:
            raise TypeError
            
        if isinstance(self.fuel_mass, float):
            if self.fuel_mass < 0.0:
                raise ValueError
        else:
            raise TypeError
            
        if isinstance(self.max_thrust_mag, float):
            if self.max_thrust_mag < 0.0:
                raise ValueError
        else:
            raise TypeError
            
        if isinstance(self.max_dmdt, float):
            if self.max_dmdt < 0.0:
                raise ValueError
        else:
            raise TypeError
        
class Payload:
    ### The payload simply represents a component of a rocket that doesn't contribute to the locomotion. It is simply "dead weight".###
    def __init__(self, mass):
        if isinstance(mass, float):
            if mass > 0.0:
                self.mass = mass
            else:
                raise ValueError
        else:
            raise TypeError