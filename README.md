# Delta II Simulator

## Summary
The project explores basic methods in computational physics by modeling the physics of rocket flight. The rocket is modelled loosely on the now retired Delta II launch vehicle. The simulation 
includes the basic Forward Eular approach to evolving a system of differential equations and takes takes drag, the changing mass of the vehicle as it consumes fuel and jettisons boosters and 
stages, and the changing density of the atmosphere. A flexible "flight plan", created using a JSON file, serves as a configuration file that allows for the number of boosters, the length of stages, 
and the mass of the payload to be specified. A custom Vector class was created to make vectors easy and intuitive to including in the coding effort.
