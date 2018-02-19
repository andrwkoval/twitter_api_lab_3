import folium
import folium.plugins
import tw_json_loader as tjl
import json_analysis as ja


def create_map(username, count):
    """
    (str, int) -> (html)
    This function creates map using username and amount of friends
    username: twitter username to get info
    count: number of friends to be displayed
    returns: map with friends markers
    """

    world_map = folium.Map()
    groups = folium.plugins.MarkerCluster().add_to(world_map)

    data = tjl.get_js_data(username, count)
    info_list = ja.analysis("location", data)

    for user in info_list:
        if user[1]:
            icon = folium.features.CustomIcon(user[2], icon_size=(30, 30))
            folium.Marker(location=user[1], popup=user[0],
                          icon=icon).add_to(groups)

    world_map.add_child(folium.LayerControl())

    return world_map.save("templates/Map.html")
