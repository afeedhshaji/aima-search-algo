from constants import GOAL_STATE, MAX_LEN


def misplaced_tiles(tile_value):
    misplaced = 0
    tile_value = tile_value.replace("_", "")
    for i in range(MAX_LEN - 1):
        if tile_value[i] != GOAL_STATE[i]:
            misplaced += 1

    return misplaced
