def formatValue(value, data):
    value = value.replace('. .', '')
    if 'Direct Use' in value:
        return table_1(value, data)
    else:
        return table_2(value)


def table_1(value, data):
    water_quality = {}
    fresh= {}
    recycle = {}
    line_value = str(value).split('\n')
    direct_use = ''
    details = ''
    for line in line_value:
        line = line.strip()
        print(line)
        if 'Vital' in line:
            if direct_use == '':
                direct_use += "Vital"
            else:
                direct_use += '\n'
                direct_use += 'Vital'
        if 'Neutral' in line:
            if direct_use == '':
                direct_use += 'Neutral'
            else:
                direct_use += '\n'
                direct_use += 'Neutral'
        if 'Direct Use:' in line:
            # if 'Direct Use:' not in details:
            #     details += " "
            #     details += line
            # else:
                details += ' '
                details += line
    fresh["directUse"] = direct_use.split('\n')[0]
    fresh["indirectUse"] = 'Important'
    fresh["details"] = str(data)[str(data).index("Direct Use: As a be"): str(data).index("and water efficiency.")]
    recycle["directUse"] = direct_use.split('\n')[1]
    recycle["indirectUse"] = 'Important'
    recycle["details"] = str(data)[str(data).index("Direct use: Our direct use"): str(data).index("water management practices and improve\nwater efficiency")]
    water_quality["freshWater"] = fresh
    water_quality["recycledWater"] = recycle
    return water_quality


def table_2(value):
    table = {}
    line_value = str(value).split('\n')
    desc = ''
    water_relevance = ''
    quality = ''
    for line in line_value:
        line.replace("\n", "")
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
    if water_relevance != '' and quality != '':
        table['relevance'] = water_relevance
        table['riskAssessments'] = {'waterQuality': quality, 'desc': desc}
        return table
    else:
        return value
