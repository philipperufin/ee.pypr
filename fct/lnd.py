import ee
import datetime
import fct.cld

# todo: make roi optional, if null don´t filter
def LND_roi(roi, startDate, endDate):

    l4 = ee.ImageCollection('LANDSAT/LT04/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .filterBounds(roi) \
        .select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    l5 = ee.ImageCollection('LANDSAT/LT05/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .filterBounds(roi) \
        .select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    l7 = ee.ImageCollection('LANDSAT/LE07/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .filterBounds(roi) \
        .select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .filterBounds(roi) \
        .select(['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    lnd = l8.merge(l7).merge(l5).merge(l4)
    lnd = lnd.map(fct.cld.maskQuality)

    return lnd

def LND_glob(startDate, endDate):
    l4 = ee.ImageCollection('LANDSAT/LT04/C01/T1_SR') \
        .filterDate(startDate, endDate) \
        .select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    l5 = ee.ImageCollection('LANDSAT/LT05/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    l7 = ee.ImageCollection('LANDSAT/LE07/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .select(['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')\
        .filterDate(startDate, endDate)\
        .select(['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'pixel_qa'],
                ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'pixel_qa'])

    lnd = l8.merge(l7).merge(l5).merge(l4)
    lnd = lnd.map(fct.cld.maskQuality)

    return lnd


