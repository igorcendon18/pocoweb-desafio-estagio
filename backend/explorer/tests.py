from django.test import TestCase
from explorer.models import Oilfield, OperationalUnit, Well

from explorer.services import process_data_challenge1, process_data_challenge2

class Challenge1TestCase(TestCase):
    def setUp(self):
        self.opunit1 = OperationalUnit.objects.create(id=1, name="Unidade 1")
        self.opunit2 = OperationalUnit.objects.create(id=2, name="Unidade 2")

        self.oilfield1 = Oilfield.objects.create(id=1, name="Campo 1", operational_unit=self.opunit1)
        self.oilfield2 = Oilfield.objects.create(id=2, name="Campo 2", operational_unit=self.opunit1)
        self.oilfield3 = Oilfield.objects.create(id=3, name="Campo 3", operational_unit=self.opunit1)
        self.oilfield4 = Oilfield.objects.create(id=4, name="Campo 4", operational_unit=self.opunit2)

        self.well1 = Well.objects.create(id=1, name="Poço 1", oilfield=self.oilfield1)
        self.well2 = Well.objects.create(id=2, name="Poço 2", oilfield=self.oilfield1)
        self.well3 = Well.objects.create(id=3, name="Poço 3", oilfield=self.oilfield2)
        self.well4 = Well.objects.create(id=4, name="Poço 4", oilfield=self.oilfield2)
        self.well5 = Well.objects.create(id=5, name="Poço 5", oilfield=self.oilfield3)
        self.well6 = Well.objects.create(id=6, name="Poço 6", oilfield=self.oilfield3)
        self.well7 = Well.objects.create(id=7, name="Poço 7", oilfield=self.oilfield3)
        self.well8 = Well.objects.create(id=8, name="Poço 8", oilfield=self.oilfield4)
        

    def test_process_data_challenge1(self):
        opunits = OperationalUnit.objects.all()
        oilfields = Oilfield.objects.all()
        wells = Well.objects.all()
        result = process_data_challenge1(opunits, oilfields, wells)

        expected_result = [[["opunit/1"]],[["opunit/2"]],[["opunit/1"], ["oilfield/1"]],[["opunit/1"], ["oilfield/2"]],[["opunit/1"], ["oilfield/3"]],[["opunit/2"], ["oilfield/4"]],[["opunit/1"], ["oilfield/1"], ["well/1"]],[["opunit/1"], ["oilfield/1"], ["well/2"]],[["opunit/1"], ["oilfield/2"], ["well/3"]],[["opunit/1"], ["oilfield/2"], ["well/4"]],[["opunit/1"], ["oilfield/3"], ["well/5"]],[["opunit/1"], ["oilfield/3"], ["well/6"]],[["opunit/1"], ["oilfield/3"], ["well/7"]],[["opunit/2"], ["oilfield/4"], ["well/8"]]]
        self.assertEqual(result, expected_result)


class Challenge2TestCase(TestCase):
    def setUp(self):
        
        opunit1 = OperationalUnit.objects.create(name="Unidade operacional 1")
        oilfield1 = Oilfield.objects.create(name="Campo 1", operational_unit=opunit1)
        well1 = Well.objects.create(name="Poço 1", oilfield=oilfield1)
        well2 = Well.objects.create(name="Poço 2", oilfield=oilfield1)

        opunit2 = OperationalUnit.objects.create(name="Unidade operacional 2")
        oilfield2 = Oilfield.objects.create(name="Campo 2", operational_unit=opunit2)
        well3 = Well.objects.create(name="Poço 3", oilfield=oilfield2)


    def test_process_data_challenge2(self):
        opunits = OperationalUnit.objects.all()
        oilfields = Oilfield.objects.all()
        wells = Well.objects.all()

        result = process_data_challenge2(opunits, oilfields, wells)

        expected_result = [
            {
                "id": 1,
                "name": "Unidade operacional 1",
                "children": [
                    {
                        "id": 1,
                        "name": "Campo 1",
                        "children": [
                            {"id": 1, "name": "Poço 1"},
                            {"id": 2, "name": "Poço 2"},
                        ],
                    }
                ],
            },
            {
                "id": 2,
                "name": "Unidade operacional 2",
                "children": [
                    {
                        "id": 2,
                        "name": "Campo 2",
                        "children": [
                            {"id": 3, "name": "Poço 3"},
                        ],
                    }
                ],
            },
        ]

        self.assertEqual(result, expected_result)