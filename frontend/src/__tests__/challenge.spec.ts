import { expect, test } from "vitest";
import { processData } from "../utils/challenge";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";
import { DataNode } from "antd/es/tree";

test("Teste para retorna a estrutura de árvore com base em todos os dados abaixo", () => {
  const opunits: OperationalUnitType[] = 
  [{
    id: 1,
    name: "Unidade Operacional 1"
  },
  {
    id: 2,
    name: "Unidade Operacional 2"
  },
  {
    id: 3,
    name: "Unidade Operacional 3"
  },
  {
    id: 4,
    name: "Unidade Operacional 4"
  },
  { id: 5,
    name: "Unidade Operacional 5"
  }
  ];

  const oilfields: OilfieldType[] = 
  [{
    id: 1,
    name: "Campo 1",
    operational_unit: 1
  },
  {
    id: 2,
    name: "Campo 2",
    operational_unit: 1
  },
  {
    id: 3,
    name: "Campo 3",
    operational_unit: 1
  },
  {
    id: 4,
    name: "Campo 4",
    operational_unit: 4
  },
  {
    id: 5,
    name: "Campo 5",
    operational_unit: 4
  },
  {
    id: 6,
    name: "Campo 6",
    operational_unit: 4
  }
];
  const wells: WellType[] = 
  [{
    id: 1,
    name: "Poço 1",
    oilfield: 1
  },
  {
    id: 2,
    name: "Poço 2",
    oilfield: 1
  },
  {
    id: 3,
    name: "Poço 3",
    oilfield: 2
  },
  {
    id: 4,
    name: "Poço 4",
    oilfield: 2
  },
  {
    id: 5,
    name: "Poço 5",
    oilfield: 3
  },
  {
    id: 6,
    name: "Poço 6",
    oilfield: 3
  },
  {
    id: 7,
    name: "Poço 7",
    oilfield: 3
  },
  {
    id: 8,
    name: "Poço 8",
    oilfield: 6
  }


];

  const result: DataNode[] = [
    {
      title: "Unidade Operacional 1",
      key: "opunit-1",
      children: [
          {
              title: "Campo 1",
              key: "oilfield-1",
              children: [
                  {
                      title: "Poço 1", 
                      key: "well-1"
                  },
                  {
                      title: "Poço 2",
                      key: "well-2"
                  }
              ]
          },
          {
            title: "Campo 2",
              key: "oilfield-2",
              children: [
                  {
                      title: "Poço 3", 
                      key: "well-3"
                  },
                  {
                      title: "Poço 4",
                      key: "well-4"
                  }
              ]
          },
          {
            title: "Campo 3",
              key: "oilfield-3",
              children: [
                  {
                      title: "Poço 5", 
                      key: "well-5"
                  },
                  {
                      title: "Poço 6",
                      key: "well-6"
                  },
                  {
                    title: "Poço 7",
                    key: "well-7"
                  }
              ]
          }
      ]
    },
    {
        title: "Unidade Operacional 2",
        key: "opunit-2",
        children: []
    },
    {
        title: "Unidade Operacional 3",
        key: "opunit-3",
        children: []
    },
    {
      title: "Unidade Operacional 4",
      key: "opunit-4",
      children: [
          {
              title: "Campo 4",
              key: "oilfield-4",
              children: []
          },
          {
            title: "Campo 5",
              key: "oilfield-5",
              children: []
          },
          {
            title: "Campo 6",
              key: "oilfield-6",
              children: [
                  {
                      title: "Poço 8", 
                      key: "well-8"
                  }
              ]
          }
      ]
    },
    {
        title: "Unidade Operacional 5",
        key: "opunit-5",
        children: []
    }


]
  const a = processData(opunits, oilfields, wells) 
  console.log(a);
  expect(processData(opunits, oilfields, wells)).toEqual(result);
});