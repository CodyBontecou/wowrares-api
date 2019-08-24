from django.db import models
from django.urls import reverse


class Zone(models.Model):
    """
    Object representing the zone that each mob resides in
    """
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True)
    image = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Method that returns the Zone objects url pattern.
        """
        return reverse('zone', kwargs=self.name)


class Mob(models.Model):
    """
    Object representing each rare mob that resides within a zone.
    """
    name = models.TextField(blank=True)
    image = models.TextField(blank=True)
    level = models.TextField(blank=True)
    health = models.TextField(blank=True)
    damage = models.TextField(blank=True)
    armor = models.TextField(blank=True)
    model_id = models.TextField(blank=True)
    faction = models.TextField(blank=True)
    x_coordinate = models.TextField(blank=True)
    y_coordinate = models.TextField(blank=True)
    coordinates = models.TextField(blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', blank=True)
    websites_id = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Object representing the items that drop off of a mob
    """
    entry = models.TextField(blank=True)
    item = models.TextField(blank=True)
    ChanceOrQuestChance = models.TextField(blank=True)
    groupid = models.TextField(blank=True)
    mincountOrRef = models.TextField(blank=True)
    maxcount = models.TextField(blank=True)
    condition_id = models.TextField(blank=True)
    patch_min = models.TextField(blank=True)
    patch_max = models.TextField(blank=True)

    def __str__(self):
        return self.entry


class ItemInfo(models.Model):
    """
    Object that contains the data returned by the item_template query.
    """
    allowable_class = models.TextField(blank=True)
    allowable_race = models.TextField(blank=True)
    ammo_type = models.TextField(blank=True)
    arcane_res = models.TextField(blank=True)
    area_bound = models.TextField(blank=True)
    armor = models.TextField(blank=True)
    bag_family = models.TextField(blank=True)
    block = models.TextField(blank=True)
    bonding = models.TextField(blank=True)
    buy_count = models.TextField(blank=True)
    buy_price = models.TextField(blank=True)
    _class = models.TextField(blank=True)
    container_slots = models.TextField(blank=True)
    delay = models.TextField(blank=True)
    description = models.TextField(blank=True)
    disenchant_id = models.TextField(blank=True)
    display_id = models.TextField(blank=True)
    dmg_max1 = models.TextField(blank=True)
    dmg_max2 = models.TextField(blank=True)
    dmg_max3 = models.TextField(blank=True)
    dmg_max4 = models.TextField(blank=True)
    dmg_max5 = models.TextField(blank=True)
    dmg_min1 = models.TextField(blank=True)
    dmg_min2 = models.TextField(blank=True)
    dmg_min3 = models.TextField(blank=True)
    dmg_min4 = models.TextField(blank=True)
    dmg_min5 = models.TextField(blank=True)
    dmg_type1 = models.TextField(blank=True)
    dmg_type2 = models.TextField(blank=True)
    dmg_type3 = models.TextField(blank=True)
    dmg_type4 = models.TextField(blank=True)
    dmg_type5 = models.TextField(blank=True)
    duration = models.TextField(blank=True)
    entry = models.TextField(blank=True)
    extra_flags = models.TextField(blank=True)
    fire_res = models.TextField(blank=True)
    flags = models.TextField(blank=True)
    food_type = models.TextField(blank=True)
    frost_res = models.TextField(blank=True)
    holy_res = models.TextField(blank=True)
    inventory_type = models.TextField(blank=True)
    item_level = models.TextField(blank=True)
    lock_id = models.TextField(blank=True)
    map_bound = models.TextField(blank=True)
    material = models.TextField(blank=True)
    max_count = models.TextField(blank=True)
    max_durability = models.TextField(blank=True)
    max_money_loot = models.TextField(blank=True)
    min_money_loot = models.TextField(blank=True)
    name = models.TextField(blank=True)
    nature_res = models.TextField(blank=True)
    other_team_entry = models.TextField(blank=True)
    page_language = models.TextField(blank=True)
    page_material = models.TextField(blank=True)
    page_text = models.TextField(blank=True)
    patch = models.TextField(blank=True)
    quality = models.TextField(blank=True)
    random_property = models.TextField(blank=True)
    range_mod = models.TextField(blank=True)
    required_city_rank = models.TextField(blank=True)
    required_honor_rank = models.TextField(blank=True)
    required_level = models.TextField(blank=True)
    required_reputation_faction = models.TextField(blank=True)
    required_reputation_rank = models.TextField(blank=True)
    required_skill = models.TextField(blank=True)
    required_skill_rank = models.TextField(blank=True)
    required_spell = models.TextField(blank=True)
    sell_price = models.TextField(blank=True)
    set_id = models.TextField(blank=True)
    shadow_res = models.TextField(blank=True)
    sheath = models.TextField(blank=True)
    spellcategory_1 = models.TextField(blank=True)
    spellcategory_2 = models.TextField(blank=True)
    spellcategory_3 = models.TextField(blank=True)
    spellcategory_4 = models.TextField(blank=True)
    spellcategory_5 = models.TextField(blank=True)
    spellcategorycooldown_1 = models.TextField(blank=True)
    spellcategorycooldown_2 = models.TextField(blank=True)
    spellcategorycooldown_3 = models.TextField(blank=True)
    spellcategorycooldown_4 = models.TextField(blank=True)
    spellcategorycooldown_5 = models.TextField(blank=True)
    spellcharges_1 = models.TextField(blank=True)
    spellcharges_2 = models.TextField(blank=True)
    spellcharges_3 = models.TextField(blank=True)
    spellcharges_4 = models.TextField(blank=True)
    spellcharges_5 = models.TextField(blank=True)
    spellcooldown_1 = models.TextField(blank=True)
    spellcooldown_2 = models.TextField(blank=True)
    spellcooldown_3 = models.TextField(blank=True)
    spellcooldown_4 = models.TextField(blank=True)
    spellcooldown_5 = models.TextField(blank=True)
    spellid_1 = models.TextField(blank=True)
    spellid_2 = models.TextField(blank=True)
    spellid_3 = models.TextField(blank=True)
    spellid_4 = models.TextField(blank=True)
    spellid_5 = models.TextField(blank=True)
    spellppmrate_1 = models.TextField(blank=True)
    spellppmrate_2 = models.TextField(blank=True)
    spellppmrate_3 = models.TextField(blank=True)
    spellppmrate_4 = models.TextField(blank=True)
    spellppmrate_5 = models.TextField(blank=True)
    spelltrigger_1 = models.TextField(blank=True)
    spelltrigger_2 = models.TextField(blank=True)
    spelltrigger_3 = models.TextField(blank=True)
    spelltrigger_4 = models.TextField(blank=True)
    spelltrigger_5 = models.TextField(blank=True)
    stackable = models.TextField(blank=True)
    start_quest = models.TextField(blank=True)
    stat_type1 = models.TextField(blank=True)
    stat_type10 = models.TextField(blank=True)
    stat_type2 = models.TextField(blank=True)
    stat_type3 = models.TextField(blank=True)
    stat_type4 = models.TextField(blank=True)
    stat_type5 = models.TextField(blank=True)
    stat_type6 = models.TextField(blank=True)
    stat_type7 = models.TextField(blank=True)
    stat_type8 = models.TextField(blank=True)
    stat_type9 = models.TextField(blank=True)
    stat_value1 = models.TextField(blank=True)
    stat_value10 = models.TextField(blank=True)
    stat_value2 = models.TextField(blank=True)
    stat_value3 = models.TextField(blank=True)
    stat_value4 = models.TextField(blank=True)
    stat_value5 = models.TextField(blank=True)
    stat_value6 = models.TextField(blank=True)
    stat_value7 = models.TextField(blank=True)
    stat_value8 = models.TextField(blank=True)
    stat_value9 = models.TextField(blank=True)
    subclass = models.TextField(blank=True)

    def __str__(self):
        return self.name
