# BDP Kossel Mini

<img src="bdp-kossel.jpg" alt="BDP Kossel Mini delta printer" style="max-height: 500px;">

A modern take on the Kossel Mini delta printer using 2020 extrusions, running on an SKR Pico, and a Raspberry Pi Zero, powered by a meanwell UHP-350-24 PSU.

## Assembly

The major components of the printer are split into separate folders. Follow the instructions contained in each of them:
- [Chassis](./models/chassis/README.md)
- [Effector](./models/effector/README.md)
- [Extruder](./models/extruder/sherpa-extra-lovely/README.md)
- [Motion](./models/motion/README.md)
- [PSU](./models/PSU/README.md)

## Bill of Materials

The full bill of materials is compiled from component BOM CSV files in [`bom/`](./bom/).

See the generated [compiled BOM](./bom/README.md) or [combined CSV](./bom/combined.csv).

## Design Source and Exports

The canonical CAD source for this project is the linked Tinkercad design in each component README.

The STL files in this repository are exported from those Tinkercad designs and included for convenience so a known buildable version is available without needing to re-export the CAD.

To modify a part, update the relevant Tinkercad design, export new STL files, replace the files in this repository, and update the component README if the change affects print count, assembly, or the BOM.

## License

Original BDP Kossel Mini content is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](./LICENSE).

Some included models are remixes or reused parts with their own license terms. See [THIRD_PARTY_LICENSES.md](./THIRD_PARTY_LICENSES.md) for attribution and per-file licensing.
