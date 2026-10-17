# Crystal Extension: Rainbow Druse, dropped crystals and release differences

**Check your release before activating the shrine.** The released 1.12.2 consumption loop can exhaust its list after shrinking the ingredients and before reaching the output branch. The released 1.16.5 loop can under-consume split stacks. The inspected 1.20.1 and 1.21.1 arithmetic handles the tested stack partitions correctly, but that does not certify acquisition, world availability or live-game compatibility.

[Crafting and recipes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes) · [Worlds and travel](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

![Rainbow Druse recipe and Crystal Extension input workflow](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crystal-extension-input-workflow.webp)

## Two different ingredients, two different steps

Do not confuse **Druse** with **Crystal** items.

1. In the inspected 1.12.2, 1.16.5 and 1.20.1 resources, craft **one Rainbow Druse** with a shapeless recipe containing one each of Red, Green, Purple, Blue, White and Yellow Druse.
2. The Crystal Extension Shrine's use callback looks for **ten dropped Crystal items in total**, accepting Blue, Green, Purple, Red, White and Yellow Crystals. Any mixture passes the selected item-type filter; it does not require ten of each color or one of every color.
3. The player uses Rainbow Druse on the shrine. After the ingredient loop, the callback consumes one Rainbow Druse outside Creative and requests one Giant Crystal through the release's item-delivery helper.

This is a block-interaction workflow, not an ordinary Giant Crystal crafting-table recipe. The 1.21.1 selected recipe scan did not find the Rainbow Druse recipe that exists in the earlier artifacts.

## Release matrix

| Minecraft / AoA artifact | Checked loop behavior | How to read the result |
|---|---|---|
| 1.12.2 / 3.3.6 | Subtracts the processed stack size, then increments the remaining counter | Exact-ten examples reach an empty-list access before the output branch |
| 1.16.5 / 3.6.11 | Subtracts the processed stack size, then decrements the remaining counter again | Split stacks can consume fewer than ten while reaching output |
| 1.20.1 / 3.7.1 | Subtracts size minus one, then decrements once | Net subtraction is exactly the processed stack size in the modeled loop |
| 1.21.1 / 3.7.16.1 | Same net arithmetic as 1.20.1, using first-element list methods | Tested partitions consume exactly ten; modern acquisition remains a separate question |

These differences were checked in the released class bytes, not inferred solely from similar source filenames. The examples below are independent Python arithmetic models, not Java execution or reports of a live item-loss session.

## Preparing the area on a validated build

The item query is an axis-aligned box from **(block X−5, Y−1, Z−5)** to **(block X+5, Y+1, Z+5)**. It is not a five-block spherical radius and is not centered on the player's inventory. Put the intended dropped items near the shrine and avoid guessing at boundary behavior from the diagram.

The selected predicate checks the dropped item's type. It does not filter by the item's owner or prove that the items belong to the activating player. Keep other players' valuable crystals out of the interaction area and test ownership behavior before using a restored shrine on a shared server.

The count precheck stops once the accepted stack counts total at least ten. Item entities can merge or appear in a different query order, so a carefully arranged pile is not a stable substitute for fixing an unsafe consumption loop.

Creative mode skips the Rainbow Druse payment, but the selected crystal-consumption loop still runs. Do not assume Creative testing leaves nearby dropped ingredients untouched.

## What the stack examples actually show

| Dropped stack sizes | 1.12.2 model | 1.16.5 model | 1.20.1 / 1.21.1 model |
|---|---|---|---|
| 9 | Precheck rejects; consumes 0 | Same | Same |
| 10 in one stack | Consumes 10, then empty-list access | Reaches output; consumes 10 | Reaches output; consumes 10 |
| 5 + 5 | Consumes 10, then empty-list access | Reaches output; consumes 9 | Reaches output; consumes 10 |
| Ten separate stacks of 1 | Consumes 10, then empty-list access | Reaches output; consumes 5 | Reaches output; consumes 10 |
| 11 in one stack | Reaches output; consumes 10 | Reaches output; consumes 10 | Reaches output; consumes 10 |
| 6 + 7 | Reaches output; consumes 11 | Reaches output; consumes 9 | Reaches output; consumes 10 |

The test set additionally enumerates **all 512 ordered positive stack partitions totaling ten**. The selected 1.12.2 model reaches the empty-list access for all 512; the 1.16.5 model reaches output but consumes exactly ten only for the single-stack partition; the 1.20.1 and 1.21.1 models reach output and consume exactly ten for all 512.

“Reaches output” means the modeled ingredient loop reaches the following branch. It does not certify successful inventory delivery, protection-mod compatibility or a whole working gameplay route. The larger-stack examples are diagnostic cases, not a recommendation to risk an original save on a workaround.

## Availability and downstream uses

The selected resources contain Rainbow Druse crafting recipes in 1.12.2, 1.16.5 and 1.20.1. They also retain Rainbow Druse references in Infusion recipes, including Crystallis armor, Crystal Carver and Crystaneer. This does not make Rainbow Druse and Giant Crystal interchangeable.

For 1.21.1, the inspected recipe/loot scan found a Crystal Extension Shrine block-drop table but no matching Rainbow Druse or Giant Crystal recipe/loot reference. The shipped recipe-viewer hiding tag includes Rainbow Druse and the six colored Crystal items. A block-drop table says what can drop from an existing block; it does not establish where the player obtains that block or its inputs. Existing code, names and textures are not sufficient to advertise a restored survival progression route.

Use the exact release filters:

- [1.12.2 Rainbow Druse recipe references](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Arainbow_druse)
- [1.16.5 Rainbow Druse recipe references](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3%3Arainbow_druse)
- [1.20.1 Rainbow Druse recipe references](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=aoa3%3Arainbow_druse)
- [Modern shrine item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&q=aoa3%3Acrystal_extension_shrine)

## Restoration requirements

1. Plan consumption before mutating stacks. Use an explicit remaining amount, subtract only the actual count taken, and stop at zero without an extra loop-counter adjustment.
2. Reject safely when the query or inventory changes. Do not leave partially consumed ingredients if output cannot be completed under the intended transaction rules.
3. Test every color, mixed colors, wrong items, wrong held item, empty hand, counts 9/10/11/64, split stacks, merged entities and reordered query results.
4. Test Creative explicitly: document whether ground ingredients are consumed, independently of the held-item cost.
5. Define ownership and protection behavior for other players' items, item pickup, despawn and protected areas.
6. Check full inventories and the actual delivery helper. A returned boolean alone may not describe whether a helper used a ground-drop fallback.
7. Restore acquisition, structure placement, recipes and downstream uses separately from the interaction arithmetic. Do not label a retained method as a complete restored system.
8. Keep discovery on interaction rather than introducing a repeated global item scan. Measure the target build before claiming a performance improvement.

## Evidence and credits

[Four released classes, selected callbacks, resource hashes and arithmetic cases](https://herbertofury.github.io/Advent-of-Ascension/crystal-extension-evidence.json) · [Exact 1.20.1 artwork crops and hashes](https://herbertofury.github.io/Advent-of-Ascension/crystal-extension-art-evidence.json).

AoA systems and source assets: Tslat and contributors. Original diagram, documentation and independent test models. No game or mod code was executed, and no runtime fix is claimed by this page.
