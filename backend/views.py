''' View functions that manage the data going to and from urls and templates '''

import os
import pprint

import requests
from time import sleep
import mysql.connector

from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .models import Zone, Mob, Item


def home(request):
    '''
    Homepage view showing little more than
    the site structure and sidebar navigation to each Zone
    '''
    context = {
        'zones': Zone.objects.all()
    }
    return render(request, 'grid-template-areas.html', context)


def update(request):
    # generate_mob_name_and_id_array()
    # get_item_information()
    # scrape_zone_images()
    query_creature_loot()
    context = {
        'zones': Zone.objects.all()
    }
    return render(request, 'index.html', context)


def zone_view(request, zone):
    '''
    Zone view showing the zone, its map,
    and the mobs that reside within the Zone.
    '''
    context = {
        'zones': Zone.objects.all(),
        'zone': Zone.objects.filter(name=zone.title()).first,
        'mobs': Mob.objects.filter(zone__name=zone.title())
    }
    return render(request, 'grid-template-areas.html', context)


def mob_view(request, zone, mob):
    '''
    Mob view showing the Zone view information,
    as well as more specific information on the individual mob.
    '''
    context = {
        'zones': Zone.objects.all(),
        'zone': Zone.objects.filter(name=zone.title()).first,
        'mobs': Mob.objects.filter(zone__name=zone.title()),
        'mob': Mob.objects.filter(name=mob.title()).first(),
    }
    return render(request, 'grid-template-areas.html', context)


def get_mob_coordinates(browser):
    '''
    Mob location coordinates are stored in a style tag.
    This function is grabbing that tag, and splitting off
    the unimportant text, leaving us with only the two coordinate numbers.
    '''
    try:
        mob_coordinates_style_tag = browser.find_element(By.XPATH,
                                                         '//*[@id="mapper-generic"]/span[1]/div/div').get_attribute(
            'style')
        mob_coordinates = mob_coordinates_style_tag[:-1].split(';')
        mob_coordinates[0] = mob_coordinates[0][6:-1]
        mob_coordinates[1] = mob_coordinates[1][6:-1]
        return mob_coordinates
    except NoSuchElementException:
        return []


def split_on_new_line(raw_values):
    array = []
    for item in raw_values:
        array.append(item.text.split('\n'))
    return array


def append_list_of_attributes_to_other_list(appendedList, attributeItems):
    for i in range(len(attributeItems)):
        appendedList[i].append(attributeItems[i].get_attribute('href'))
    return appendedList


def generate_zones(browser):
    """
    Creates a list of all zones.
    Goes to `'https://classicdb.ch/?zones=' + str(i)` to get Kalimdor and Eastern Kingdom.
    Each page contains a list of zones that I scrape and create Zone objects of.
    """
    zones = []
    for i in range(2):
        browser.get(
            'https://classicdb.ch/?zones=' + str(i)
        )
        zone_urls = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[4]/div[2]/div/table/tbody/tr/td[1]/a')
        for url in zone_urls:
            zone_id = url.get_attribute('href').split('=')[1]
            zones.append(Zone(
                id=zone_id,
                name=url.text,
                image='https://classicdb.ch/images/maps/enus/normal/' + zone_id + '.jpg'
            ))
    Zone.objects.bulk_create(zones)
            # zone.id = url.get_attribute('href').split('=')[1]
            # zone.name = url.text
            # zone.image = 'https://classicdb.ch/images/maps/enus/normal/' + zone.id + '.jpg'
            # zone.save()


def generate_mob_name_and_id_array():
    delay = 5
    browser = webdriver.Chrome(os.environ.get("CHROMEDRIVER"))
    # generate_zones(browser)

    for zone in Zone.objects.all():
        print('********************* ' + zone.name + ' *****************************')
        browser.get(
            "https://vanilla-twinhead.twinstar.cz/?zone=" + zone.id
        )
        search_input = browser.find_element(By.XPATH, '//*[@id="tab-npcs"]/div[1]/span/input')
        search_input.send_keys('rare')
        sleep(delay)

        rare_mob_rows = browser.find_elements(By.XPATH, '//*[@id="tab-npcs"]/table/tbody/tr')
        rare_mobs_array = split_on_new_line(rare_mob_rows)
        rare_mobs_a_tag = browser.find_elements(By.XPATH, '//*[@id="tab-npcs"]/table/tbody/tr/td[1]/a')
        arr = append_list_of_attributes_to_other_list(rare_mobs_array, rare_mobs_a_tag)
        arr = split_last_index_on_equals(arr)
        arr = delete_all_but_first_and_last_index(arr)
        arr = clean_first_index_trailing_digits(arr)
        arr = add_items_from_npc_page(browser, arr)
        # create_new_mob_objects(arr, zone)
    browser.quit()


def clean_first_index_trailing_digits(array):
    for arr in array:
        while arr[0][-1] in " 0123456789":
            arr[0] = arr[0][:-1]
    return array


def delete_all_but_first_and_last_index(array):
    returned_array = []
    for arr in array:
        mob_name = arr[0]
        mob_id = arr[-1]
        temp_array = []
        temp_array.append(mob_name)
        temp_array.append(mob_id)
        returned_array.append(temp_array)
    return returned_array


def add_items_from_npc_page(browser, array):
    for mob in array:
        browser.get(
            "https://classicdb.ch/?npc=" + mob[1]
        )
        # img_tag = mob_img_classicdb(browser)
        # mob_coordinates = get_mob_coordinates(browser)
        # mob_information = get_mob_information(browser)
        get_item_information(browser)
        # mob.append(img_tag)
        # mob.append(mob_coordinates)
        # mob.append(mob_information)
    return array


def get_item_information():
    browser = webdriver.Chrome(os.environ.get("CHROMEDRIVER"))
    for mob in Mob.objects.all():
        browser.get(
            "https://classicdb.ch/?npc=" + mob.websites_id
        )
        item = Item()
        tds = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/table/tbody/tr')
        for td in tds[:4]:
            if '-' not in td.text:
                print(td.text)


def split_last_index_on_equals(array):
    for items in array:
        items[-1] = items[-1].split('=')[1]
    return array


def mob_img_classicdb(browser):
    mob_img_tag = browser.find_element(By.XPATH, '//*[@id="modelv"]')
    return mob_img_tag.get_attribute('src')


def get_mob_information(browser):
    '''
    Example Mob:
    ['Level': '22']
    ['Class': 'Rare-Elite']
    ['React': 'A H']
    ['Faction': 'Undercity']
    ['Health': '471']
    ['Wealth': '32']
    ['Damage': '179 - 214 (Physical)']
    ['Armor': '499']
    ['Model': '4156']
    '''
    mob_information_tag = browser.find_elements(By.XPATH,
                                                '/html/body/div[3]/div[2]/div[4]/div[2]/table/tbody/tr[2]/td/div[2]/ul/li')
    mob_information = {}
    for tag in mob_information_tag:
        key = tag.text.split(':')[0]
        value = tag.text.split(':')[1][1:]
        mob_information[key] = value
    return mob_information


def create_new_mob_objects(array, zone):
    mobs = []
    for item in array:
        mobs.append(Mob(
            zone=zone,
            name=item[0],
            websites_id=item[1],
            image=item[2],
            coordinates=item[3],
            level=item[4]['Level'],
            faction=item[4]['Faction'],
            health=item[4]['Health'],
            damage=item[4]['Damage'],
            model_id=item[4]['Model']
        ))
    Mob.objects.bulk_create(mobs)


def scrape_zone_images():
    browser = webdriver.Chrome(os.environ.get("CHROMEDRIVER"))
    for zone in Zone.objects.all():
        saved_file_name = zone.name.replace(' ', '-').lower() + '-map-picture.png'
        browser.get(zone.image)
        img_src = browser.find_element(By.TAG_NAME, 'img').get_attribute('src')

        with open('../wow-rares/wow-rares/static/' + saved_file_name, 'wb') as handle:
            response = requests.get(img_src, stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)


def query_all_creatures(connection):
    cursor = connection.cursor()
    query = ("SELECT * from creature;")
    cursor.execute(query)
    cursor.close()
    return [creature for creature in cursor]


def query_creature_loot():
    connection = mysql.connector.connect(user='root', password='Hhtpqrs1234!', host='127.0.0.1', database='wow_classic')
    for mob in Mob.objects.all():
        print(mob.name)
        cursor = connection.cursor()
        query = (f"SELECT * FROM creature_loot_template WHERE entry={mob.websites_id};")
        cursor.execute(query)
        fields = [i[0] for i in cursor.description]
        result = [dict(zip(fields, row)) for row in cursor.fetchall()]

        mob_items = []
        for item in result:
            item_model = Item.objects.create(drop_rate=item['ChanceOrQuestChance'])
            mob_items.append({item_model: item})
            # item['ChanceOrQuestChance']

        for item in mob_items:
            print(item)
        # query_item_info(result, connection)
    connection.close()


def query_item_info(items, connection):
    for item in items:
        cursor = connection.cursor()
        query = (f"SELECT * FROM item_template WHERE entry={item['item']};")
        cursor.execute(query)
        fields = [i[0] for i in cursor.description]
        result = [dict(zip(fields, row)) for row in cursor.fetchall()]
        for item_info in result:
            pprint.pprint(item_info)
            break

