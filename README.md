# ATLAS

ATLAS is a modular aerospace simulation framework for modeling aircraft and satellite dynamics. It combines aerodynamic, atmospheric, and orbital physics with time-stepped simulation systems to support engineering analysis, education, and research.

The project provides reusable physics models, simulation runtimes, mission profiles, scenario execution, and analytics tools for studying aerospace systems under realistic operating conditions.

---

## Features

### Aircraft Simulation

ATLAS includes a physics-based aircraft performance simulator capable of modeling:

* Lift generation
* Aerodynamic drag
* Stall speed estimation
* Thrust-to-weight ratio
* Mach number calculation
* Reynolds number calculation
* ISA atmosphere modeling
* Fuel consumption and effective mass tracking
* Altitude and climb rate simulation
* Position and heading tracking
* Mission profile support
* Time-stepped flight simulation

### Satellite Simulation

ATLAS includes orbital and atmospheric models for Low Earth Orbit (LEO) satellites:

* Orbital velocity calculation
* Atmospheric density modeling
* Satellite drag force calculation
* Orbital altitude tracking
* Orbital decay estimation
* Time-stepped propagation
* Satellite state management

### Atmosphere & Physics

Shared physics modules provide:

* International Standard Atmosphere (ISA)
* Atmospheric density models
* Orbital density models
* Gravity calculations
* Aerodynamic force equations
* Orbital mechanics utilities
* Aerospace constants and unit systems

### Analytics

Simulation outputs can be exported and analyzed through:

* CSV export
* JSON export
* Performance graphs
* Decay graphs
* Simulation result logging

### Scenario System

ATLAS supports reusable simulation scenarios:

* Aircraft scenarios
* Satellite scenarios
* Mission profiles
* Batch simulation execution

---

## Applications

* Aerospace engineering education
* Aircraft performance analysis
* Satellite mission analysis
* Orbital lifetime estimation
* Flight profile evaluation
* Physics-based simulation studies
* Research and experimentation

---

## Current Aircraft Capabilities

* Lift calculation
* Drag calculation
* Stall speed estimation
* Thrust-to-weight ratio
* Mach number
* Reynolds number
* ISA atmosphere integration
* Fuel burn simulation
* Effective mass calculation
* Altitude propagation
* Position tracking
* Heading tracking
* Mission profile execution

---

## Current Satellite Capabilities

* Orbital velocity calculation
* Atmospheric drag modeling
* Orbital decay simulation
* Altitude propagation
* Time-stepped orbital simulation

---

## Project Goals

### Near-Term

* Aircraft flight envelopes
* Autopilot systems
* Waypoint navigation
* Orbital element propagation
* Ground track generation
* Satellite maneuver modeling

### Long-Term

* Unified aerospace simulation engine
* Advanced atmospheric models
* Multi-vehicle simulations
* Visualization tools
* High-performance Rust simulation runtime

---

## Output

ATLAS generates structured simulation data that can be exported for further analysis and visualization.

Example outputs include:

* Aircraft performance datasets
* Fuel consumption profiles
* Flight trajectory data
* Satellite decay datasets
* Orbital propagation results
