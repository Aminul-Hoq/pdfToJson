import re


def formatValue(value):
    line_value = str(value).split('\n')
    desc = ''
    water_relevance = ''
    quality = ''
    for line in line_value:
        if 'Relevance' in line:
            water_relevance += line[line.index('Relevance'): len(line)]
        elif 'Water quality' in line:
            quality += line[line.index('Water quality'): len(line)]
        else:
            desc += line
    if water_relevance == '' and quality == '':
        return {'relevance': water_relevance, 'riskAssessments': {'waterQuality': quality, 'desc': desc}}
    else:
        return value
