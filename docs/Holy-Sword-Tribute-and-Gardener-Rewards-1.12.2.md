# Holy Sword and event-driven weapon rewards

**Minecraft 1.12.2 · AoA 3.3.6.** Some weapons are awarded by event code rather than recipes, traders or item entries in loot JSON. This guide joins the Holy Sword’s nightfall predicate with the existing Gardener harvesting route.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-holy_sword.webp" width="150" height="150" alt="Holy Sword"> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-gardener.webp" width="150" height="150" alt="Gardener">

## Holy Sword: satisfy all four meters at the check

The caller runs on **server END world ticks in dimension ID 0**. The reward check is reached only after total world time is **greater than 24,000**, at **world time modulo 24,000 = 12,500**. All four tribute getters must return **exactly 200**: Erebon, Luxon, Pluton and Selyan.

At that point the code creates one Holy Sword stack and uses the give-to-inventory-or-drop helper. Keep inventory space and check nearby ground. The separate all-four-at-least-100 branch grants a Night Vision effect; reaching 100 in each meter is not enough for the sword.

### A practical order to plan around

1. **Prepare in the Overworld before the check.** Avoid changing dimensions or dying during the preparation cycle; those server callbacks reset tribute. The Overworld sunrise case at tick 23,031 also resets all tribute.
2. **Build Erebon before topping off Luxon.** The selected daytime Overworld non-player living-death branch, when the true damage source is a player, requests **+8 Erebon and −8 Luxon**. Doing more qualifying combat after filling Luxon can spoil your preparation. Pet-owner and unrelated kill-credit paths are not assumed equivalent.
3. **Restore Luxon through eligible daytime Pixon harvesting.** The Infusion Bowl requests **4 × actual harvestCount** in dimension 0 during daytime. Harvest units are loop iterations, not a count of unique Pixons or an unconditional number of clicks. Read the [Pixon harvesting and bowl guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2) for eligibility and equipment details.
4. **Fill Selyan with eligible mature crops during daytime.** The checked harvesting branch requests **+2 Selyan**. Its separate Gardener roll is described below.
5. **Fill Pluton using the checked skill routes.** [Foraging and Logging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2) have different loot and day/night gates; their requested base gain is **11 − integer(level / 10)**. Not every mined block or chopped log awards tribute.
6. **Read the meters and be present for the 12,500 check.** Do not travel into Ancient Cavern and expect its tribute to carry back: dimension changes reset it. Do not treat the number of actions as more authoritative than the current meters.

From zero, with no multipliers or intervening losses, the raw request arithmetic is 25 eligible +8 gains, 50 eligible +4 harvest units and 100 eligible +2 crop gains. These are planning examples, not a guarantee that all activities fit into one day or that every attempted action passes its event gates.

## Existing Holy Sword changes tribute arithmetic

The shared helper doubles **signed** tribute changes when its Holy Sword holding check applies, then clamps the stored meter to 0–200. Negative costs and losses are doubled too. This is why using the sword while paying deity-shrine costs needs separate consideration; see [Ancient Cavern and deity shrines](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2).

When resources are disabled, getTribute returns 200 independently of the stored meters. That configuration can satisfy the reward predicate without normal tribute preparation. It is a configuration-semantic difference, not proof that the visible stored data reached 200 or that ordinary survival progression was completed.

## Gardener: an independent crop-harvest reward

The harvesting event rejects a missing harvester and FakePlayer, then its reward logic runs on the server. For an eligible mature BlockCrops harvest during daytime, it requests the Selyan gain and checks **nextInt(2000) == 0** before attempting to drop a Gardener at the player.

That is a **1-in-2,000 random gate per qualifying event**, not a promise of one weapon after 2,000 harvests. Flowers, vines and leaves participate in other Anima logic but do not satisfy this crop-specific Gardener branch. A modded crop’s appearance alone does not prove it inherits BlockCrops or passes the maturity check. The selected branch does not explicitly restrict this reward to dimension 0.

[Full Anima harvesting walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) · [Gardener firing inputs and ammunition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2)

## Restoration test targets

- [ ] Compare 199/200 in each meter and total world time 24,000/24,001.
- [ ] Check time-of-day 12,499/12,500/12,501 and the 23,031 reset.
- [ ] Verify server END/dimension-0 caller gates, inventory-full delivery and dimension/death resets.
- [ ] Keep Erebon gain/Luxon loss ordering and the signed Holy Sword multiplier explicit.
- [ ] Test resources-enabled and resources-disabled behavior separately.
- [ ] Review repeated time-of-day ticks: the selected 12,500 reward branch has no per-day claim marker. If a time-control mechanism repeats that tick while the predicates remain true, repeated reward attempts are possible in the static model. Decide and test an idempotence policy before changing it; this is not a reproduced duplication test.
- [ ] Test genuine crop classes, maturity, FakePlayer exclusion and daylight transitions for Gardener.

## Evidence and limits

[Released event/caller/helper evidence and predicate models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tribute-reward-evidence-1.12.2.json) · [Weapon acquisition atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Weapon-Acquisition-1.12.2)

The event gates are read from the released artifact. No game was executed, no item was awarded and no in-game timing or drop-rate measurement was performed. Time-changing mods, event cancellation and modpack overrides need their own tests. Models and textures are by Tslat and contributors.
