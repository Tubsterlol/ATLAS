# ATLAS Validation Report

This page lists a few simple reference checks for the current model. The values are meant to show that the code is in the right range, not to certify the simulator.

## Gravity

| Test | Expected | Actual |
| --- | --- | --- |
| Surface gravity | 9.81 m/s² | 9.81997 m/s² |

## Atmosphere

| Test | Expected | Actual |
| --- | --- | --- |
| Density at sea level | 1.225 kg/m³ | 1.225 kg/m³ |
| Density at 10 km | about 0.38 kg/m³ | 0.37775 kg/m³ |

## Orbital mechanics

| Test | Expected | Actual |
| --- | --- | --- |
| ISS circular-orbit speed at 408 km | about 7660 m/s | 7668.07 m/s |
| ISS orbital period at 408 km | about 92.5 min | 92.58 min |
| Semi-major axis at 408 km | Earth radius + altitude | 6,779,000 m |

## Aircraft

| Test | Expected | Actual |
| --- | --- | --- |
| F-16 thrust-to-weight ratio | about 1.1 | 1.10 |
| Boeing 737-800 stall speed | realistic positive value | 82.27 m/s |
| Lift at sea level, 100 m/s, CL 1.2, 20 m² | positive | 147,000 N |
| Drag at sea level, 100 m/s, CD 0.02, 20 m² | positive | 2,450 N |

## Reference checks in the test suite

The test suite also checks the following behavior:

- gravity decreases with altitude
- atmospheric density decreases with altitude
- ISS-like orbital speed stays in the expected low-Earth-orbit range
- stall speed stays positive
- lift and drag stay positive under normal conditions

## What this means

The models are behaving in the expected range for the examples and unit tests we ship today.

They are still simplified models:

- gravity is a basic inverse-square model
- atmosphere is a single-lapse-rate approximation
- satellite decay is simplified
- aircraft motion is point-mass performance, not full rigid-body flight dynamics

Use the validation cases as a sanity check, not as proof of real-world accuracy.
