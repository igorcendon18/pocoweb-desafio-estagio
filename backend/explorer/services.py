def process_data_challenge1(opunits, oilfields, wells):
    """
    Função que processa os dados para a estrutura solicitada
    """
    result = []

    for opunit in opunits:
        opunit_entry = [["opunit/{}".format(opunit.id)]]
        result.append(opunit_entry)

    for oilfield in oilfields:
        oilfield_entry = [["opunit/{}".format(oilfield.operational_unit.id)],["oilfield/{}".format(oilfield.id)]]
        result.append(oilfield_entry)

    for well in wells:
        well_entry = [["opunit/{}".format(well.oilfield.operational_unit.id)],["oilfield/{}".format(well.oilfield.id)],["well/{}".format(well.id)]]
        result.append(well_entry)

    return result


def process_data_challenge2(opunits, oilfields, wells):
    """
    Função que processa os dados para a estrutura solicitada
    """
    result = []

    for opunit in opunits:
        opunit_info = {
            'id': opunit.id,
            'name': opunit.name,
            'children': [],
        }

        for oilfield in oilfields:
            if oilfield.operational_unit_id == opunit.id:
                oilfield_info = {
                    'id': oilfield.id,
                    'name': oilfield.name,
                    'children': [],
                }

                for well in wells:
                    if well.oilfield_id == oilfield.id:
                        well_info = {
                            'id': well.id,
                            'name': well.name,
                        }
                        
                        oilfield_info['children'].append(well_info)

                opunit_info['children'].append(oilfield_info)

        if opunit_info['children']:
            result.append(opunit_info)

    return result
