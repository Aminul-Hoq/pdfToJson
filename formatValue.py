def formatValue(value):
    table = {}
    line_value = str(value).split('\n')
    desc = ''
    water_relevance = ''
    quality = ''
    for line in line_value:
        line = line.strip()
        if 'Relevance' in line:
            if water_relevance == '':
                water_relevance += line[line.index('Relevance'): len(line)]
            else:
                desc += line
        elif 'Water' in line:
            if water_relevance == '':
                quality += line[line.index('Water'): len(line)]
            else:
                desc += line
        else:
            desc += line
    print(water_relevance)
    if water_relevance != '' and quality != '':
        table['relevance'] = water_relevance
        table['riskAssessments'] = {'waterQuality': quality, 'desc': desc}
        return table
    else:
        return value
