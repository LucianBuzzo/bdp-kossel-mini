# Contributing

Thanks for helping improve the BDP Kossel Mini.

## Design Workflow

The canonical CAD source for this project is the linked Tinkercad design in each component README.

The STL files in this repository are exported from those Tinkercad designs and included for convenience. If you change a part, update the relevant Tinkercad design first, export updated STL files, replace the files in this repository, and update the component README if the change affects print count, assembly, or the bill of materials.

Do not add STEP exports unless there is a specific project need. The repository should stay focused on Tinkercad source links and build-ready STL exports.

## Commit Messages

This repository uses [release-please](https://github.com/googleapis/release-please) to generate releases and changelogs from Conventional Commits.

Use Conventional Commit messages for all changes:

- `fix: correct belt tensioner mounting note`
- `feat: add bowden extruder mount`
- `docs: clarify effector assembly order`
- `chore: update release workflow`

Release impact:

- `fix:` creates a patch release.
- `feat:` creates a minor release.
- A breaking change creates a major release. Mark it with `!`, such as `feat!: change frame extrusion length`, or include a `BREAKING CHANGE:` footer.

Documentation-only and maintenance commits may still appear in the changelog depending on release-please configuration and commit type, so keep messages clear and user-facing.

## Bill of Materials

The BOM is maintained as component CSV files in `bom/`.

To update the BOM, edit the relevant component CSV and regenerate the compiled outputs:

```sh
python3 scripts/generate-bom.py
```

Commit the edited component CSV plus the regenerated `bom/README.md` and `bom/combined.csv`.
