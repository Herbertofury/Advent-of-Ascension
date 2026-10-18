# Per-weapon feature status

The [complete weapon standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard) applies all 31 feature groups to every weapon. Each row has independent concept, implementation and QA states. These first reconciled manifests cover exact published prototype revisions; later local experiments do not silently change their claims.

- [Soul Storm, published v16 authoring study](soul-storm-feature-status.json)
- [Discharge Shotgun, published v3 authoring study](discharge-shotgun-feature-status.json)

Both manifests explicitly reject full acceptance. Discharge's selected concept is approved; its model, animation, effects and gameplay are not thereby approved. Soul Storm has source-level sight and recoil work, but native integration and full visual quality remain open. Other feature rows remain visible even where not started.

The source ZIPs and reference files are linked by repository-relative path and SHA-256. To reproduce structural checks, obtain the validator from the completeness package and run it against a clone of this repository as the evidence root. `--release` must reject both of these incomplete manifests. Structural validity is not a beauty or gameplay judgment.

The all-228 first-target assignment register remains separate from these individually reviewed manifests. A registered requirement is not a completed feature. Historical/version-exclusive weapons and other weapon families still require their own reconciled scope.
