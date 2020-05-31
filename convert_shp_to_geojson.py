import geopandas as gpd
import json


def convert():
    gdf = gpd.read_file(f"IneShapeFiles/ine_depto.shp", encoding='utf-8')
    gdf.head()
    gdf.to_file('geojsons/ine_depto.json', driver='GeoJSON')


if __name__ == '__main__':
    convert()
